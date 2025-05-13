import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
import pyqtgraph as pg
from pyqtgraph import DateAxisItem

#odczyt danych z CSV i parse_dates
dane = pd.read_csv(r"C:\Users\lechowski_sz\Desktop\UP\weather_2024.csv", parse_dates=["date"])

dane.rename(columns={"date": "data", "temperature": "temperatura", "humidity": "wilgotnosc", "precipitation": "opady"}, inplace=True)
dane.set_index("data", inplace=True)

#obliczenie sredniej kroczacej (rolling().mean())
dane["srednia_kroczaca"] = dane["temperatura"].rolling(window=7, center=True).mean()

#wykrywanie outliers (mean(), std(), filtrowanie) w cyklu miesiecznym
dane['miesiac'] = dane.index.month
def wykryj_anomalie(grupa):
    sr = grupa["temperatura"].mean()
    odch = grupa["temperatura"].std()
    return (grupa["temperatura"] > sr + 2 * odch) | (grupa["temperatura"] < sr - 2 * odch)

dane["czy_anomalia"] = dane.groupby("miesiac").apply(wykryj_anomalie).reset_index(level=0, drop=True)

#grupowanie danych (groupby) i sumy miesieczne (resample)


dane_miesieczne = dane.resample('M').sum(numeric_only=True)

#liczenie korelacji (corr())
korelacja_temp_wilg = dane[["temperatura", "wilgotnosc"]].corr().iloc[0,1]
korelacja_temp_opad = dane[["temperatura", "opady"]].corr().iloc[0,1]

#interpolacja brakow (interpolate())

dane_interp = dane.copy()
dane_interp.loc[dane_interp.iloc[::3].index, ["temperatura", "wilgotnosc", "opady"]] = np.nan
dane_interp.interpolate(method='time', inplace=True)

#wykorzystanie QTableView i modelu pandas do wyswietlania tabeli
class ModelPandas(QAbstractTableModel):
    def __init__(self, dane):
        super().__init__()
        self._dane = dane.reset_index()

    def rowCount(self, parent=None):
        return len(self._dane)

    def columnCount(self, parent=None):
        return len(self._dane.columns)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            wartosc = self._dane.iat[index.row(), index.column()]
            if isinstance(wartosc, float):
                return f"{wartosc:.2f}"
            return str(wartosc)
        return None

    def headerData(self, sekcja, orientacja, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientacja == Qt.Horizontal:
                return self._dane.columns[sekcja]
            else:
                return str(sekcja)
        return None

#uzycie PyQtGraph do wykresow
class AplikacjaPogody(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analiza Pogody 2024")
        self.setGeometry(100, 100, 1200, 800)

        layout = QVBoxLayout()

        #tabela z danymi
        self.tabela = QTableView()
        col = ["temperatura", "srednia_kroczaca", "wilgotnosc", "opady", "czy_anomalia"]
        self.model = ModelPandas(dane[col])
        self.tabela.setModel(self.model)
        layout.addWidget(self.tabela)

        #surowe dane i srednia kroczaca, zaznaczenie anomalies
        #wykres liniowy surowe + srednia + anomalie
        os_czasu = DateAxisItem(orientation='bottom')
        wykres_temp = pg.PlotWidget(title="Temperatura vs. Srednia kroczaca", axisItems={'bottom': os_czasu})
        wykres_temp.addLegend()
        wykres_temp.setMouseEnabled(x=True, y=True)

        # konwersja index na timestampy (sekundy)
        x = dane.index.astype(np.int64) // 10**9
        wykres_temp.plot(x, dane["temperatura"], pen=pg.mkPen(color='b', width=1), name="Temperatura")
        wykres_temp.plot(x, dane["srednia_kroczaca"], pen=pg.mkPen(color='r', width=2), name="Srednia 7d")
        anom = dane[dane["czy_anomalia"]]
        x_anom = anom.index.astype(np.int64) // 10**9
        wykres_temp.plot(x_anom, anom["temperatura"], pen=None, symbol='x', symbolBrush='r', name="Anomalie")
        wykres_temp.enableAutoRange()
        layout.addWidget(wykres_temp)

        #Wykres slupkowy: miesieczne opady
        #wykres slupkowy z sumami opadow
        wykres_opad = pg.PlotWidget(title="Suma opadow miesiecznie")
        etykiety = dane_miesieczne.index.strftime('%b')
        slupki = pg.BarGraphItem(x=list(range(len(etykiety))), height=dane_miesieczne["opady"].values, width=0.6, brush='orange')
        wykres_opad.addItem(slupki)
        wykres_opad.getAxis('bottom').setTicks([list(enumerate(etykiety))])
        layout.addWidget(wykres_opad)

        kontener = QWidget()
        kontener.setLayout(layout)
        self.setCentralWidget(kontener)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = AplikacjaPogody()
    okno.show()
    sys.exit(app.exec_())



    # python "C:\Users\lechowski_sz\Desktop\UP\PO_Pogoda.py"

   