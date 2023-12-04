# Understanding how exceptions work in Python

# This is for the custom exception
# This is a little confusing, becuase you have to import the module.file then the class in the file
# In this case, the file and custom exception class are both called 'MyException'
from my_exceptions.MyException import MyException

from my_exceptions.DetailedException import DetailedException

def function_that_can_have_exception(left, right):
    try:
        i_left = int(left)
        i_right = int(right)
    # except TypeError as error:  # The "as error" is optional, if you want to interact with the error
    except ValueError as error:  # The "as error" is optional, if you want to interact with the error
        print("An exception occurred: " + error.args[0])
        return -1
    else:
        return i_left + i_right


num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")

total = function_that_can_have_exception(num1, num2)
print(total)


def only_lowercase(str_message):
    """ Now a function that raises a custom Exception """
    if str_message.islower():
        print("Great")
    else:
        print("Input is not all lowercase!")
        raise MyException("String is not lowercase")
        # raise Exception("String is not lowercase")


str_message = input("Enter a lower case string: ")
only_lowercase(str_message)


def only_even(num_arg):
    """ Now a function that raises a custom Exception """
    try:
        num = int(num_arg)
    except:
        raise DetailedException("Could not convert input to integer", -10)

    if num % 2 == 0:
        print("Great")
    else:
        print("Input is not even!")
        raise DetailedException("Number is not even", -20)


even_num = input("Enter an even number: ")
only_even(even_num)
