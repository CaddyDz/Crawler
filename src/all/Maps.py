import random
import sys
import os
# Dictionaries or maps are like lists but they are key value pair
# Note that dictionaries can't be joined with addition sign
super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}
print(super_villains['Captain Cold'])				  
# del keyword is used to delete an entry
del super_villains['Fiddler']
print(super_villains)
# Values of keys can be updated in place 
super_villains['Pied Piper'] = 'Hartley Rathaway'
# Get the length of the dictionary
print(len(super_villains))
# Note that both keys and values can be extracted
print(super_villains.get("Pied Piper"))
# Get the list of keys in the dictionary
print(super_villains.keys())
# Get the list of values in the dictionary
print(super_villains.values())
