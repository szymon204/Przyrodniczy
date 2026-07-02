from osgeo import ogr, osr
import os

ogr.UseExceptions()

# USTAWIENIA

# Sciezka do folderu z danymi
sciezka = os.path.dirname(os.path.abspath(__file__))

wybrane_wojewodztwo = "wielkopolskie"

provinces_path  = os.path.join(sciezka, "provinces.shp")
gauge_path      = os.path.join(sciezka, "gauge_stations.shp")
meteo_path      = os.path.join(sciezka, "stacje_meteo.shp")


# OTWARCIE WARSTW

provinces_ds = ogr.Open(provinces_path)
gauge_ds     = ogr.Open(gauge_path)
meteo_ds     = ogr.Open(meteo_path)

if provinces_ds is None or gauge_ds is None or meteo_ds is None:
    print("Blad: nie mozna otworzyc jednej z warstw.")
    exit()

provinces_layer = provinces_ds.GetLayer()
gauge_layer     = gauge_ds.GetLayer()
meteo_layer     = meteo_ds.GetLayer()

print("Warstwy wczytane poprawnie.")
print("  Liczba wojewodztw :", provinces_layer.GetFeatureCount())
print("  Liczba wodowskazow:", gauge_layer.GetFeatureCount())
print("  Liczba stacji meteo:", meteo_layer.GetFeatureCount())
print()


# WYSZUKANIE WYBRANEGO WOJEWODZTWA

geom_wojewodztwa = None

for feature in provinces_layer:
    nazwa = feature.GetField("name")
    if nazwa is not None and nazwa.lower() == wybrane_wojewodztwo.lower():
        geom_wojewodztwa = feature.GetGeometryRef().Clone()
        print("Znaleziono wojewodztwo:", nazwa)
        break

if geom_wojewodztwa is None:
    print("Nie znaleziono wojewodztwa:", wybrane_wojewodztwo)
    exit()

print()


# WYBOR WODOWSKAZOW LEZACYCH W WOJEWODZTWIE

wodowskazy = []

for feature in gauge_layer:
    geom = feature.GetGeometryRef()
    if geom is None:
        continue
    if geom.Within(geom_wojewodztwa):
        nazwa = feature.GetField("gauge_name")
        wodowskazy.append((nazwa, geom.Clone()))

print("Liczba wodowskazow w wojewodztwie", wybrane_wojewodztwo + ":", len(wodowskazy))


# WYBOR STACJI METEO LEZACYCH W WOJEWODZTWIE

stacje_meteo = []

for feature in meteo_layer:
    geom = feature.GetGeometryRef()
    if geom is None:
        continue
    if geom.Within(geom_wojewodztwa):
        nazwa = feature.GetField("NAZWA_ST")
        stacje_meteo.append((nazwa, geom.Clone()))

print("Liczba stacji meteorologicznych w wojewodztwie", wybrane_wojewodztwo + ":", len(stacje_meteo))
print()


# POROWNANIE LICZEBNOSCI

print("--- PODSUMOWANIE LICZEBNOSCI ---")
if len(wodowskazy) > len(stacje_meteo):
    print("W wojewodztwie", wybrane_wojewodztwo, "jest wiecej wodowskazow niz stacji meteorologicznych.")
elif len(stacje_meteo) > len(wodowskazy):
    print("W wojewodztwie", wybrane_wojewodztwo, "jest wiecej stacji meteorologicznych niz wodowskazow.")
else:
    print("Liczba wodowskazow i stacji meteorologicznych jest taka sama.")
print()


# SZUKANIE NAJBLIZSZEJ STACJI METEO DLA KAZDEGO WODOWSKAZUW
# Jednostka odleglosci = metry (uklad PUWG 1992 / EPSG:2180)

print("--- NAJBLIZSZA STACJA METEO DLA KAZDEGO WODOWSKAZU ---")
print()

for nazwa_ww, geom_ww in wodowskazy:

    najmniejsza_odleglosc = None
    najblizsza_stacja = None

    for nazwa_st, geom_st in stacje_meteo:

        odleglosc = geom_ww.Distance(geom_st)

        if najmniejsza_odleglosc is None or odleglosc < najmniejsza_odleglosc:
            najmniejsza_odleglosc = odleglosc
            najblizsza_stacja = nazwa_st

    odleglosc_km = round(najmniejsza_odleglosc / 1000.0, 2)

    print("Wodowskaz        :", nazwa_ww)
    print("Najblizsza stacja:", najblizsza_stacja)
    print("Odleglosc        :", odleglosc_km, "km")
    print()

print("Obliczenia zakonczone.")