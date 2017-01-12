# A context manager is a Python object that provides extra contextual information to an action.
# This extra information takes the form of running a callable upon initiating the context using the 'with' statement,
# as well as running a callable upon completing all the code inside the 'with' block.
# The most well known example of using a context manager is shown here, opening on a file:
with open('file.txt') as f:
    contents = f.read()

print(contents)

# An easy way to implement this functionality is as follows
class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)
    def __enter__(self):
        return self.file
    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file.txt') as f:
    contents = f.read()