my_list = [1, 2, 3]
my_list[0] = 4
print(my_list)  # [4, 2, 3] <- The same list as changed

x = 6
x = x + 1  # The new x is another object
print(x)

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
foo += 'ooo'  # This is bad, instead you should do:
foo = ''.join([foo, 'ooo'])

foo = 'foo'
bar = 'bar'

foobar = '%s%s' % (foo, bar)  # It is OK
foobar = '{0}{1}'.format(foo, bar)  # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar)  # It is best
