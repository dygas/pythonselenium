imie = 'Bartek'
nazwisko = "Kowalski 'Nowak'"
adres = '''dworcowa
           28c/1 00-001 warszawa'''

print(nazwisko)
print('czytam ksiązkę "wladca pierscieni"')
print('czytam\t ksiązkę \n \"wladca pierscieni\"')
#dodaj r nie bedą interpretowane po nawiasie print print(r...
print("male litery".upper())
print("male litery".lower())
print(imie.islower())
print(nazwisko.isupper()) #zapytania jakie są liczery w zmiennych
for char in "Bartek":
    print(char)

print(imie[0])
#wypisze wszystkie litery po polei pionowo
print(imie[0:4])
print(imie.index("a"))
print("ala"in "ala ma kota")
print(" ".join(('ala', 'ma', 'kota')))
print('ala,ma,kota,ale,to,nie, twoja,sprawa'.split(","))
print(imie.startswith("Ba"))
print(imie.endswith("tek"))