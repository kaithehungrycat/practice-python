#sap = {'color': 'red', 'age': '42'}
# for v in sap.values():
#     print(v)
# for k in sap.keys():
#     print(k)
# for i in sap.items():
#     print(i)
####
# print(list(sap.items()))

# for v,k in sap.items():
#    print('key: ' + v + ', value: ' + str(k))

# print('name' in sap.items())
# 'color' in sap.values()
# print('color' in sap.keys())

# print('I will bring ' + str(sap.get('colour', 0)) + ' carpet.') #give 0 if key doesn't exist in dict

#if 'weight' not in sap:
#   sap['weight'] = '95 kg'


###   !!!! sap.setdefault('height', '190 cm') #same function will not change already existing key to '185 cm' for example
#print(sap)
msg = 'Jaki byl ten dzien, co darowal co wzial'
count = {}

for character in msg:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)