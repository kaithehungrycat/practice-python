catNames = ()

while True:
    print('Podaj imie kota numer' + str(len(catNames) + 1) + '(Ewentualnie nie wpiusuj nic, aby zakonczyc.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('Oto imiona kotow:')
for name in catNames:
    print(' ' + name)