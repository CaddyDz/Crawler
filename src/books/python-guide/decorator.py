# A decorator is a simple yet powerful syntax provided by Python
# A decorator is simply a function or a class that wraps (or decorates) a function or a method.
# The 'decorated' function or method will replace the original one 'undecorated'
# because functions are first class objects in Python.
# Example


def foo():
    5 + 5


def decorator(func):
    # Manipulate func
    return func

foo = decorator(foo)  # Manually decorate


@decorator
def bar():
    5 + 5
    # Do something
    # bar() is decorated
