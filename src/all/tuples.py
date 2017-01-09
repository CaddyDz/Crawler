import string
# Tuples are like lists but the items can't be changed in place
# Use Paranthesis instead of Brackets
pi_tuple = (3, 1, 4, 1, 5,9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print (len(new_list))  # Output 6
print (min(new_list))  # Output 1