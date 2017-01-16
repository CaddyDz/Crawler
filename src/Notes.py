# the double slashes // does a simple division and then round down the result
# which means // = / + floor(result)
# Example below
print(18/4)  # print out 4.5
print(18//4)  # print out 4
x = 18 / 4
print(round(x))  # print out 4
# strings are character chains and can be treated as arrays
string = "Lorem Ipsum"
print(string[0])  # print out L
print(string[7])  # print out p
# Ranges are defined just like MS Excel using the : operator
print(string[0:6])  # print out Lorem (and space) even the I is 6 but not included
# Len = string length
print(len(string))  # print out 11
# Lists are declared using brackets, and value can be changed in place
languages = ['C#', 'SQL', 'PHP', 'JS', 'HTML5', 'CSS3', 'Python']
print(
    languages[6]  # print out Python
)
# Items can be added to lists using += operator or append function
languages += ['Perl', 'Ruby', 'Java']
languages.append('Objective C')
print(languages)
# Testing wakatime.