s = "Scissors"
p = "Paper"
r = "Rock"

user1 = str(input("Rock, Scissors or Paper. What do you choose?"))
user2 = str(input("Rock, Scissors or Paper. What do you choose?"))


def compare(u1, u2):
    if u1 == u2:
        print("It's a Tie!")
    elif u1 == "rock":
        if u2 == "scissors":
            return "User 1 won!"
        elif u2 == "paper":
            return "User 2 won"
        else:
            return "Invalid input!"

    elif u1 == "paper":
        if u2 == "rock":
            return "User 1 won"
        elif u2 == "scissors":
            return "User 2 won"
        else:
            return "Invalid input!"

    elif u1 == "scissors":
        if u2 == "paper":
            return "User 1 won"
        elif u2 == "rock":
            return "User 2 won"
        else:
            return "Invalid input!"
    else:
        return "Invalid input!"

print(compare(user1, user2))


one_more_time = input("One more time?(Y/N)")

while one_more_time == "Y":
    user1 = str(input("Rock, Scissors or Paper. What do you choose?"))
    user2 = str(input("Rock, Scissors or Paper. What do you choose?"))
    print(compare(user1, user2))
