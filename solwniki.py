dziennik={1:'kowalski', 2:'dygas', 3:'straczek'}
print(dziennik.get(1))
print(dziennik[2])
dziennik[4] = "pankiewicz"
print(dziennik.get(4))
for key in dziennik.keys():
    print(key)
for value in dziennik.values():
    print(value)
del dziennik[1]
for value in dziennik.values():
    print(value)
dziennik[2] = 'nowy uczen'
print('nowy uczen to ' + dziennik[2])