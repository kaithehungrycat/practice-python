birthdays = {'mama':'17.04', 'tata':'03.02', 'Dusia':'27.04', 'Agata':'02.07'}

while True:
    name = input('Insert name (Leave blank to quit):')
    if name == '':
        break
    elif name in birthdays:
        print(name + 'have birthday in' + birthdays[name])
    else:
        print('Nie znaleziono daty urodzin osoby o imieniu ' + name)
        print('Kiedy ma urodziny?')
        bday = input()
        birthdays[name] = bday
        print('Baza wirusow zostala zaktualizowana')
