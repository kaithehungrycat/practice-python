from datetime import *

a = input("Hey Mate! Please tell me your name: ")
b = int(input("And how old are you? "))
c = int(input("How many copies would you like to see?"))
d = datetime.now()

while c > 0:
    print("Hey {}! \nDid you know that you will turn 100 in year {}?".format(a, (d.year - b) + 100))
    c -= 1
