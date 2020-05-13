class Pies:

    gatunek = 'pies domowy'

    def __init__(self,rasa, imie, wiek):# inna definicja nietypowa
        print('wewnatrz metody init ')
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek
    def szczekaj(self):
        print('hau hau')
    def zaprezentuj_psa(self):
        print('rasa to ' + self.rasa)
        print('imie to  '+ self.imie)
        print('wiek  to ' + str(self.wiek))

reksio = Pies('kundelek','reksio',2)
print(reksio.wiek)
print(reksio.imie)
print(reksio.rasa)
print(reksio.gatunek)
print(Pies.gatunek)
reksio.wiek = 3
print(reksio.wiek)
print(reksio.gatunek)
Pies.gatunek ='pies obronny'
print(Pies.gatunek)
print(reksio.szczekaj())
print(reksio.zaprezentuj_psa())





