a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55, 89, 55]
f = [0, 34]
c = []
d = []

e = [element for element in a if element in b]
g = [element for element in a if element in f]

print(e)
print(g)
