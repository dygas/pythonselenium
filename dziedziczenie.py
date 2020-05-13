class Osoba:

    def __init__(self, imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przectaw_sie(self):
        return "Nazywam sie" + self.imie +' ' + self.nazwisko

    class Student(Osoba):

        def __init__( self,imie,nazwisko,numer_indeksu):
            Osoba.__init__(self,imie,nazwisko)
            self.indeks = numer_indeksu

        def podaj_numer_indeksu(self):
            return self.indeks

        def przectaw_sie(self):
            return 'jestem studentem i mam na imie' + self.imie




student = Student('Tomasz', 'Kot',123456)
print(student.przectaw_sie())
print(student.podaj_numer_indeksu())

