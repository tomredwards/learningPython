import numpy as np  # Can access everything in numpy using the alias np

from datetime import *  # Everything within datetime is imported and can be accessed without the "datetime." prefix

#import datetime

print("hello world")

a = np.arange(6)

print(a)

print(datetime.now())  # This is a bit confusing, because the datetime module has a class named 'datetime' in it

# If just do: "import datetime", you have to call stuff via datetime.datetime
#print(datetime.datetime.now())

# Prints out the function or variable names in a module
print(dir(np))

# Prints the functions and variables in the current namespace
print(dir())
