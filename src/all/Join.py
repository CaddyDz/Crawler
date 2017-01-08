# Two or more strings can be joined simply by adding them
string1 = "Remember you are unique"
# Use triple single quotes to make a multiline string
string2 = '''
Just Like everyone else
'''
string3 = string1 + string2
print(string3)
print("%s %s %s " % ('I like the quote', string1, string2))
# To print without new lines use end="" after the printing
# Example here
print("I don't like ", end="")
print("new lines")
# Printing can be executed multiple times simply by multiplying
# Example here
print("\n" * 5)  # Prints a new line 5 times
print("lorem ipsum dolor amet")
