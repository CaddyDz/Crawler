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

