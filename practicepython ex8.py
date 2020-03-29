user1 = input("Rock, Scissors or Paper. What do you choose?")
user2 = input("Rock, Scissors or Paper. What do you choose?")


def compare(u1, u2):
    if u1 == u2:
        print("It's a Tie!")
    elif u1 == "rock":
        if u2 == "scissors":
            return "User 1 won!"
        elif u2 == "paper":
            return "User 2 won"

    elif u1 == "paper":
        if u2 == "rock":
            return "User 1 won"
        elif u2 == "scissors":
            return "User 2 won"

    elif u1 == "scissors":
        if u2 == "paper":
            return "User 1 won"
        elif u2 == "rock":
            return "User 2 won"
    else:
        return "Invalid input!"


print(compare(user1, user2))
