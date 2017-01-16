# Mutable types allows in-place modification of content.
# Typical mutable types are lists and dictionaries (maps)

# Mutable functions for lists
list = [1, 2, 3]
list.append(4)
print(list)   # Output: [1, 2, 3, 4]
list.pop(2)
print(list)  # Output: [1, 2, 4]

my_list = [1, 2, 3]
my_list[0] = 4
print(my_list)  # [4, 2, 3] <- The same list as changed

x = 6
x = x + 1  # The new x is another object

# Bad
# Create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = ""
for n in range(20):
    nums += str(n)  # Slow and inefficient
print(nums)

# Good
# Create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = []
for n in range(20):
    nums.append(str(n))
print("".join(nums))  # Much more efficient

# Best
# Create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = [str(n) for n in range(20)]
print("".join(nums))

foo = 'foo'
bar = 'bar'

foobar = foo + bar  # This is good
foo += 'oooo'  # This is bad, instead you should do:
foo = ''.join([foo, 'oooo'])
# Note the % formatting can also be used to concatenate a pre-determined number of strings besides str.join() and +. However, PEP 3101, discourages the usage of the % operator in favor of the str.format() method.

foo = 'foo'
bar = 'bar'

foobar = '%s%s' % (foo, bar)  # It is OK
foobar = '{0}{1}'.format(foo, bar)  # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar)  # It is best
