a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #lista a
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55, 89, 55] #lista b
c = [] #porownanie a do b
d = [] #porowbanie b do a

for element in a:
    if element in b:
        c.append(element)

for element in b:
    if element in a:
        d.append(element)


c=set(c)

print(c) #wynik z usunietymi duplikatami
print(list(dict.fromkeys(c))) #wynik z usunietymi duplikatami