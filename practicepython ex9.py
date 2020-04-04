import random

a = random.randint(0, 9)

b = int(input("Guess my number (from 0 to 9"))

print(a)


def guess(u1, u2):
    if u1 == u2:
        print("U win")
    elif u1 >= u2:
        print("Go higher mate")
    elif u1 <= u2:
        print("Go lower mate")


print(guess(a, b))

one_more_time = "y"

while one_more_time == "y":
    u1 = input("GUESS MY NUMBER?")
    print(a)
    print(guess(a, u1))
    if u1 == "exit":
        break


