num = int(input("Please give me a number"))
check = int(input("Gimme check: "))

if num % 4 == 0:
    print("Multiple 4!")

elif num % 2 == 0:
    print("Number you have provided is even")

else:
    print("Number you have provided is odd")

if num / check >= 1:
    if num % check == 0:
        print(num, "divides evenly by", check)
    else:
        print(num, "does not divides evenly by", check)

else:
    print("nope")
