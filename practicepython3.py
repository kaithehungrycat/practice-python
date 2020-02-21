x = int(input("Please provide num from 1 to 88: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for element in a:
    if element > x:
        b.append(element)


print(b)


