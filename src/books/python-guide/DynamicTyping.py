# Bad
a = 1
a = 'A string'


def a():
    pass  # Do something

# Good
count = 1
msg = 'A string'


def func():
    pass  # Do something
# Using the same name for different data types can cause problems such as this one
items = 'a b c d'  # This is a string
items = items.split(' ')  # Becomes a list
items = set(items)  # And then a set
