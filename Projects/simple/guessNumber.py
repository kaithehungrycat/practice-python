import random
import sys

a = random.randint(0, 9)
count = 5
user_input = input("Guess my number (from 0 to 9)")
print(a)

while user_input == "exit":
    break

while user_input != "exit" and count != 0:
    if int(user_input) in range(0, 10):
        if int(user_input) == a:
            print("U win")
            print("you have only " + str(count) + " lives left")
            break
        elif int(user_input) >= a:
            count -= 1
            print("Go lower mate")
            print("you have only " + str(count) + " lives left")
            user_input = (input("Guess my number (from 0 to 9)"))
        elif int(user_input) <= a:
            count -= 1
            print("Go higher mate")
            print("you have only " + str(count) + " lives left")
            user_input = (input("Guess my number (from 0 to 9)"))

    else:
        sys.exit("Invalid input")
