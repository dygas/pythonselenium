def dziennik(klasa, **kwargs):
    print('klasa ' + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
        print(kwargs.get('Kowalski'))
dziennik("3c", Kowalski=1,Nowak=2,Dygas=3);

def paln(dzien, **kwargs):
    print('dzien ' + dzien)
    for zajecia in kwargs.keys():
        print(zajecia)
paln("poniedzialek",Matematyka=1,wf=2,polski=3)