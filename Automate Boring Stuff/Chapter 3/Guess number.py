import random
import sys

b = 2
secretNumber = random.randint(1, 20)
print("Let's play the game. Try to guess my secret number (from 1 to 20) in 2 tries")


def guess_number(x):
    try:
        if int(x) < 20:
            if int(x) > secretNumber:
                print("To high")
            elif int(x) < secretNumber:
                print("To low")
            else:
                print("Congrats, You won!")
        else:
            print("till 20!")
    except:
        sys.exit("Invali input")


while b >= 1:
    a = input("Your choice is: ")
    print(guess_number(a))
    b -= 1
    print("Lives left :" + str(b))
    if b > 0:
        v = input("Wanna play again? (Y or N)")
        if v == "Y":
            continue
    else:
        sys.exit("Game Over")
