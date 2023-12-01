

# This will get replaced by the second "say_hi" method definition
def say_hi():
    print("Hello World!")


# Note: This method replaces the say_hi() one above!!!
# An optional parameter was created so that it could still be called with no arguments
def say_hi(name="World!"):  # Note, there cannot be any spaces for the default value of the argument
    print("Hello " + name)


def say_hi_name(name):
    print("Hello " + name)


def add_two_numbers(left, right):
    return left + right


say_hi()

say_hi_name("Tom")

added = add_two_numbers(1, 2)
print(added)
addedStrings = add_two_numbers("str1", "str2")
print(addedStrings)  # two strings were concatenated in this case!!!


def subtract_two_numbers(left, right):
    return left - right


subValue = subtract_two_numbers(100, 50)
print(subValue)

subValue = subtract_two_numbers(right=10, left=30)
print(subValue)


def lots_of_args(x, y, z):
    print(x, y, z)
    pass


# Note that the positional arguments have to be first
lots_of_args(1, z=3, y=2)


# Allows for any number of arguments - *args becomes a tuple (immutable)
def variable_args(a, b, *args):
    print(a, b, args)


variable_args(1, 2, 3, 4, 5, 6, 7, 8, 9)


def many_named_args(**kwargs):
    print(kwargs)


many_named_args(x = 1, y = 2, s = "hello world")


def mixed_many_args(*args, **kwargs):
    print("args=", args)
    print("kwargs=", kwargs)


print("Start of call to mixed_many_args.......")
mixed_many_args(1, 2, 3, a=1, b=2, c=3)


# Passing a list as the functions for an argument, but decompose into the position arguments
lots_of_args(*[10, 20, 30])


def four_arguments(a, b, c=True, d=False):
    print(a, b, c, d)


four_arguments(*[1, 2, True, "str_value"])
four_arguments(**{'b': 2, 'a': 1, 'd': "str_value", 'c': False})

four_arguments(*[11, 22], **{"c": "c_val", "d": "d_val"})

# What happens if I pass in an array then a dictionary - it becomes a single value for *args!!!
mixed_many_args([11, 22], {"c": "c_val", "d": "d_val"})

# Let's try that again, I want everything broken out!
mixed_many_args(*[11, 22], **{"c": "c_val", "d": "d_val"})

