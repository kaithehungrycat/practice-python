x = int(input("Gimme x: "))
a = list(range(1, x+1))
blist = []

for element in a:
    if x % element == 0:
        blist.append(element)

print(blist)

######################################################################

x = int(input("Enter number: "))
print([a for a in range(1, x + 1) if x % a == 0])