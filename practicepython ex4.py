x = int(input("Gimme x: "))
a = list(range(1, x+1))
blist = []

for element in a:
    if x % element == 0:
        blist.append(element)

print(blist)

######################################################################

input_num = int(input("choose a number: "))
lista = list(range(1, a+1))
print([element for element in lista if input_num % element == 0])


