def add(*args):
    return sum(args)


print(add(2, 4, 5))
print(add(2, 4, 5, 8, 10, 13))
print(add(1, 4))


def foo(a, b=4, c=6):
    print(a, b, c)


foo(4, 9)


def calculate(n, **kwargs):
    print(kwargs)
    n *= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-2")
print(my_car.model)


def test(*args):
    print(args)
    print(type(args))


test(1, 2, 3, 5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
