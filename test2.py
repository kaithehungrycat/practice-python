print("Hey! to play use: \n 0 - kamien \n 1 - papier \n 2 - nozyce")

u1 = int(input("Rock, Scissors or Paper. What do you choose?"))
u2 = int(input("Rock, Scissors or Paper. What do you choose?"))


def compare(a, b):
    range(0, 2)
    if a == b:
        print("Tie")
    elif a - b == 1 or a - b == -2:
        print("Win A")
    elif a - b == -1 or a - b == 2:
        print("Win B")
    else:
        print("Invalid input")


print(compare(u1, u2))

one_more_time = str(input("Once more? [y/n]"))

while one_more_time == "y":
    u1 = int(input("Rock, Scissors or Paper. What do you choose?"))
    u2 = int(input("Rock, Scissors or Paper. What do you choose?"))
    print(compare(u1, u2))
    one_more_time = str(input("Once more? [y/n]"))
