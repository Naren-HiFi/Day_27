def calculate(n, **kw):
    print(kw)
    n += kw["add"]
    n *= kw["multiply"]
    print(n)

calculate(3,add=4, multiply=5)

class Car:
    def __init__(self, **keywordargs):
        self.make = keywordargs.get("make")
        self.model = keywordargs.get("model")
        self.colour = keywordargs.get("color")
        self.seats = keywordargs.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(toast='nah', spam=4, eggs=2)


def test(*args):
    print(args)
    print(type(args))


test(1, 2, 3, 5)
"""
 def add(**kwargs):
 sum = 0
     for n in kwargs:
         sum += kwargs[n]
     return sum
 
 
 print(add(n1=5, n2=0, n3=20))
 
 
"""
