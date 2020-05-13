imiona = ['bartek','tomek','andzej',1,2,3,4,5,6,7,]
print(imiona[0])
print(imiona[0:4])
print(imiona.index('tomek'))
imiona.append('adam')
imiona.insert(0,'grzegorz')
print(imiona)
print(len(imiona))#jak dluga lista
print(imiona[-1])
imiona.remove('adam')
del imiona[0]
print(imiona)


pierwsza_lista =['koc','krzeslo','piec']
druga_lista=[1,2,4,5,6]
del pierwsza_lista[2]
print(pierwsza_lista)
print(pierwsza_lista*100)
print(pierwsza_lista + druga_lista)
pierwsza_lista.sort()
koc,krzeslo,lampa = pierwsza_lista

nazwiska =[kowalski,adamiak,pusia]
nazwiska.sort()
posortwane = sorted(nazwiska)