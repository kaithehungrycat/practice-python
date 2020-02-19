num = int(input("Gimme num: "))
check = int(input("Gimme check: "))

if num / check >= 1:
    if num % check == 0:
        print("You have even")
    else:
        print("You have odd")

else:
    print("nope")