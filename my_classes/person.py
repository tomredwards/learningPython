
"""
Class to test member variable and getters and setters
"""


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        print("\t\tI am in the age setter!")
        if isinstance(new_age, int) and 0 <= new_age < 120:
            self._age = new_age
        else:
            raise Exception("Incorrect age value")

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Person[{self.name}] is {self.age}"
