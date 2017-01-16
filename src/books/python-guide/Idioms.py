# Unpacking
some_list = ['Python', 'PyCharm']
for index, item in enumerate(some_list):
    # Do something with index and item
    print(index, item)

# You can use this to swap variables as well
a = 1
b = 2
a, b = b, a
# Nested unpacking works too:
a, (b, c) = 1, (2, 3)
# In Python 3, a new method of extended unpacking was introduced by PEP 3132:
rest = [5, 6, 8, 15, 65]
a, *rest [1, 2, 3]
# a = 1, rest = [2, 3]
a, *middle, c = [1, 2, 3, 4]
# a = 1, middle = [2, 3], c = 4

# Create an ignored variable

filename = 'foobar.txt'
basename, __, ext = filename.rpartition('.')

# Create a length-N list of the same thing
four_nones = [None] * 4

# Create a length-N list of lists
four_lists = [[] for __ in range(4)]
