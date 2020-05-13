pierwszy_zbior = {'warszawa', 'krakow','katowice','lodz'}
drugi_zbior = {'warszawa'}
pierwszy_zbior.add('kielce')
print(pierwszy_zbior);
drugi_zbior.add('lodz')
print(drugi_zbior)
#zbiory nie maja sortowania
print(pierwszy_zbior - drugi_zbior)#roznica
print(pierwszy_zbior | drugi_zbior)#suma
print(pierwszy_zbior & drugi_zbior)#czesc wspolna
print(pierwszy_zbior ^ drugi_zbior)#ROZNICa SYMETRYCZNA
