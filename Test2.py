input_num = int(input("choose a number: "))
lista = list(range(1, input_num+1))
print([element for element in lista if input_num % element == 0])