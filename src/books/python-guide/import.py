# It is considered a bad practice to import all modules from a library
from math import *
x = sqrt(4)
# This is a better approach since it explicitly declares which function to import
from math import sqrt
x = sqrt(4)
# This is the best practice since the function is already within the module scope
import math
x = sqrt(4)