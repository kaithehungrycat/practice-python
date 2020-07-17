import sys
try:
    num = int(input("Gimme number: "))
except:
    sys.exit("Value error")


def collatz(x):
        while x != 1:
            if x % 2 == 0:
                x = x // 2
                print(x)
            else:
                x = 3 * x + 1
                print(x)



print(collatz(num))