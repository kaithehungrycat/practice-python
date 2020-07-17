spam = ['apples', 'bananas', 'tofu', 'dog', 'cats']

def listThing(a):
    for i in range(len(a) - 1):
        print(a[i], end=', ')
    print('and ' + str(a[len(a) - 1]))


listThing(spam)
