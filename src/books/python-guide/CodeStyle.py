# General concepts
# Explicit code
# Bad
def make_complex(*args):
    x, y = args
    return dict(**locals())
# Good
def make_complex(x, y):
    return {'x': x, 'y': y}
# One statement per line
# Bad
print('one'); print('two')
x = 1
if x == 1: print('one')
'''
if <complex comparison> and <other complex comparison>:
    # Do something
'''
# Good
print('One')
print('two')
if x == 1:
    print('one')
'''
cond1 = <complex comparison>
cond2 = <other complex comparison>
if cond1 and cond2:
    # Do something
'''