word = input("please provide word")
word = word.upper()
rev = word[::-1]

if word == rev:
    print("It is a palindrome ")
else:
    print("It's not a palindrome ")

print(word)

word = input("please provide word")

if word == word[::-1]:
    print("It is a palindrome ")
else:
    print("It's not a palindrome ")

print(word)