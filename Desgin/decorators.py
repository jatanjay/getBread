"""
Concept 1: First class functions

A function is a first class function if:

1. It can be assigned to a variable
>
def square(x):
    return x * x

f = square
print(square)
print(f(2))

2. It can be passed as an argument to another function
>
def f(opr, var1, var2):
    return opr(var1, var2)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


x = f(add, 2, 3)
y = f(sub, 2, 3)

print(x, y)

3. It can be returned from another function
AKA CLOSURE!

>
def multiplier(factor):
    def number(x):
        return factor * x

    return number


to_number = multiplier(10)
print(to_number(10))
"""

"""
Concept 2: Higher order functions

A higher order function is a function that:

1. Takes one or more functions as arguments

Examples:
a) map function
def sq(x):
    return x * x
print(list(map(sq, [2, 2, 3]))) # [4, 4, 9]


b) filter function
def fil(x):
    return x >= 18
print(list(filter(fil, [25, 30, 18, 2, 3]))) # [25, 30, 18]

c) setTimeout in JavaScript


2. Returns a function as a result
def sub(x, y):
    return x - y


def div(x, y):
    return x / y


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def classify(func, test1, test2):
    if func(test1, test2) >= (test2 + test1):
        return func
    return False


all_funcs = [sub, div, add, mul]

for fx in all_funcs:
    print(classify(fx, 5, 10))
"""


"""
Concept 3:
decorators:
A.

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    return "Display Function ran"


@decorator_function
def display_info(name, age):
    return f"{name} & {age}"


print(display())
print(display_info("John", "22"))

Note:
Why @X syntax?
@decorator_function syntax is same as
f = decorator_function(display)
f()


B. Class decorators:
class Decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(
            "call method executed this before {}".format(
                self.original_function.__name__
            )
        )
        return self.original_function(*args, **kwargs)


@Decorator_class
def display():
    return "Display Function ran"


@Decorator_class
def display_info(name, age):
    return f"{name} & {age}"


print(display())
print(display_info("John", "22"))


B. Using stacked decorators

from functools import wraps


def my_logger(ogfunc):
    import logging

    logging.basicConfig(filename="{}.log".format(ogfunc.__name__), level=logging.INFO)

    @wraps(ogfunc)
    def wrapper(*args, **kwargs):
        logging.info("ran with args {}, and kwargs {}".format(args, kwargs))
        return ogfunc(*args, **kwargs)

    return wrapper


def my_timer(ogfunc):
    import time

    @wraps(ogfunc)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = ogfunc(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {} sec".format(ogfunc.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    x = [f for f in range(1000)]
    print(f"display_info ran with args {name}, {age}")


display_info("Jatan", [23, 25])





"""
