#Optional parameters

def func(word, add=5, frequency=1):
    print(word*(frequency+add))

call = func('yup',10,2)
print(call)

class car(object):
    def __init__(self, make, model, year, condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            print('This car is a %s %s from %s, it is %s and has %s kms.' %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("nope")




whip = car('Ford','Fusion', '2012', 'New', '0')
whip.display(True)