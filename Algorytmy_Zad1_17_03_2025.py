#https://www.tutorialspoint.com/python/python_hello_world.htm
print ("Hello world")

#https://www.tutorialspoint.com/python/python_interpreter.htm
price = 100
qty = 5
total = price*qty
print("Total", total)

#https://www.tutorialspoint.com/python/python_if_else.htm
age = 21
print("age: ", age)
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")

amount = 2500
print("Amount = ", amount)
if amount > 10000:
    discount = amount * 20 / 100
else:
    if amount > 5000:
        discount = amount * 10 / 100
    else:
        if amount > 1000:
            discount = amount * 5 / 100
        else:
            discount = 0
print("Payable amount = ", amount - discount)

amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0

print('Payable amount = ',amount - discount)

#https://www.tutorialspoint.com/python/python_strings.htm
var1 = 'Hello World!'
var2 = 'Python Programming'

print("var[0]: ", var1[0])
print("var2[1:5]", var2[1:5])
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')
print ("My name is %s and weight is %d kg!" % ('Zara', 60)) 
var = '''Welcome to TutorialsPoint'''
print ("var:", var)
var = """Welcome to TutorialsPoint"""
print ("var:", var)
var = '''
Welcome To
Python Tutorial
from TutorialsPoint
'''
print ("var:", var)
var = "Welcome To TutorialsPoint"
print (type(var))

#https://www.tutorialspoint.com/python/python_while_loops.htm
count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))

print ("End of while loop")

var = '0'
while var.isnumeric() == True:
   var = "test"
   if var.isnumeric() == True:
      print ("Your input", var)
print ("End of while loop")

var = 1
while var == 1 : #Nieskonczona petla
   num = int(input("Enter a number :"))
   print ("You entered: ", num)
print ("Good bye!")

count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))
else:
   print ("While loop over. Now in else block")
print ("End of while loop")

count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))
else:
   print ("While loop over. Now in else block")
print ("End of while loop")

flag = 0
while (flag): print ("Given flag is really true!")
print ("Good bye!")

#https://www.tutorialspoint.com/python/python_lists.htm
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])

#https://www.tutorialspoint.com/python/python_basic_syntax.htm
if True:
    print("To jest wewnątrz ifa")

x = 5      
y = "Hello" 
z = 3.14   
print("Hello, World!")
for i in range(5):
    print(i)

if x > 0:
    print("Liczba dodatnia")
else:
    print("Liczba ujemna")

#https://www.tutorialspoint.com/python/python_variables.htm
counter = 100
miles = 1000.0
name = "John"

print(counter)
print(miles)
print(name)

a = b = c = 1
print(a, b, c)  # Wynik: 1 1 1


x, y, z = 5, 10.5, "Hello"
print(x)
print(y) 
print(z) 

x = 5        # int
y = 3.14     # float
z = "Python" # str
flag = True  # bool

print(type(x))
print(type(y))
print(type(z))
print(type(flag))

x = 10
print(x)
del x


x = 5
y = "10"


x_str = str(x)  
print(x_str, type(x_str))

y_int = int(y)
print(y_int, type(y_int))

x_float = float(x)
print(x_float, type(x_float))

#https://www.codewars.com/kata/59342039eb450e39970000a6

def odd_count(n):
    return n // 2
# Testy
print(odd_count(7))
print(odd_count(10))
print(odd_count(1)) 
print(odd_count(15))

#https://www.codewars.com/kata/57ab2d6072292dbf7c000039
def remove_polish_letters(znak):
    polish_map = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    return ''.join(polish_map.get(char, char) for char in znak)
print(remove_polish_letters("Jędrzej Błądziński"))

#https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
def replace_vowels(znak):
    return ''.join('!' if char in "aeiouAEIOU" else char for char in znak)

print(replace_vowels("Czesc!"))
print(replace_vowels("Witaj"))
print(replace_vowels("aeiou"))
print(replace_vowels("ABCDE"))

#https://www.codewars.com/kata/565f5825379664a26b00007c
#obliczanie pola powierzchni calkowitej:
def get_size(width, height, depth):
    surface_area = 2 * (width * height + width * depth + height * depth)
    volume = width * height * depth
    return [surface_area, volume]

print(get_size(2, 3, 4))
print(get_size(1, 1, 1))

#https://www.codewars.com/kata/59dd3ccdded72fc78b000b25
def whatday(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[num - 1] if 1 <= num <= 7 else "Enter a number between 1 and 7"


print(whatday(1))
print(whatday(5))
print(whatday(-4))

#https://www.tutorialspoint.com/python/python_for_loops.htm
tekst = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated."
for znak in tekst:
   if znak not in 'aeiou':
      print (znak, end='')

liczby = (34,54,67,21,78,97,45,44,80,19)
total = 0
for suma in liczby:
   total += suma
print ("Lacznie =", total)

liczby = [34,54,67,21,78,97,45,44,80,19]
suma = 0
for liczba in liczby:
   if liczba%2 == 0:
      print (liczba)

for liczba in range(5):
   print (liczba, end=' ')
print()
for liczba in range(10, 20):
   print (liczba, end=' ')
print()
for liczba in range(1, 10, 2):
   print (liczba, end=' ')

liczby = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in liczby:
   print (x,":",liczby[x])

liczby = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in liczby.items():
   print (x)

#sprawdzanie liczb pierwszych
for liczba in range(10, 20):  
   for i in range(2,liczba): 
      if liczba%i == 0:      
         j=liczba/i          
         print ("%d rowna sie %d * %d" % (liczba,i,j))
         break 
      else:                  
         print (liczba, "jest liczba pierwsza")
         break
      

#https://www.tutorialspoint.com/python/python_functions.htm
def greetings():
   print ("Hello World")
   return
greetings()

def printme(str):
    print(str)
    return
printme("test drukowania funkcji")


#Kod pokazuje, ze obiekt ma ten sam identyfikator przed i po przekazaniu go do funkcji, bo Python pracuje na tym samym obiekcie.
def testfunction(arg):
   print ("ID w funkcji:", id(arg))

var = "Hello"
print ("ID po przejsciu:", id(var))
testfunction(var)

def greetings(imie):
   print ("Witaj, {}".format(imie))
   return
   
greetings("Maks")
greetings("Jacek")

def printinfo(imie, wiek):
   print ("Name: ", imie)
   print ("Age: ", wiek)
   return
printinfo( wiek=20, imie="Jacek")


def printinfo( imie, wiek = 35 ):
   print ("Imie: ", imie)
   print ("Wiek ", wiek)
   return
   
printinfo( wiek=23, imie="Jacek" )
printinfo( imie="Jacek" )