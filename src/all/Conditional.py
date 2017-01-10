import random
import sys
import os

# Python uses the industry standard conditional keywords except for minor changes
age = 21
if age > 16:
	print("You are old enough to drive")
else:
	print("You are not old enough to drive")

if age >= 21:
	print('You are old enough to drive a tractor trailer')
elif age >= 16:
	print('You are old enough to drive a car')
else:
	print('You are not old enough to drive')

# Use the "and" keyword instead of && to join conditions
# Use the "or" keyword instead of || to compare conditions
# Use the "not" keyword instead of ! to negate condition
if ((age >= 1) and (age <= 18)):
	print("You get a birthday")
elif (age == 21) or (age >= 65):
	print("You get a birthday")
elif not(age == 30):
	print("You don't get a birthday")
else:
	print("You get a birthday party yeah")
# test the waka.