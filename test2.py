print("Hey! to play use: \n 0 - kamien \n 1 - papier \n 2 - nozyce")

u1 = int(input("Rock, Scissors or Paper. What do you choose?"))
u2 = int(input("Rock, Scissors or Paper. What do you choose?"))


def compare(a, b):
    if a == b:
        print("Tie")
    elif a-b == 1 or a-b == -2:
        print("Win A")
    else:
        print("Win B")


print(compare(u1, u2))
