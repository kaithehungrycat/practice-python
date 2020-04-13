a = [5, 10, 15, 20, 25]
b = []


def first_last():
    b.append(a[0])
    x = len(a) - 1
    b.append(a[x])
    return b


def f_l():
    return [a[0], a[len(a) - 1]]


#def zzz():
    #c = []
    #first, last = a
    #c = [first, last]
    #print(c)


print(f_l())
