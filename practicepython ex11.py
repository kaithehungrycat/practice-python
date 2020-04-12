def x(help_text="Give me a number and I will check it: "):
    return int(input(help_text))


y = x()  # dodajac wartosc w nawias, input wyswietli wartosc dodana
a = list(range(1, y + 1))
b_list = []

for element in a:
    if y % element == 0:
        b_list.append(element)

print(b_list)

######################################################################

# x = int(input("Enter number: "))
# print([a for a in range(1, x + 1) if x % a == 0])
