"""
Class that shows ways to create multiple construtors

To create multiple constructors you can have default arguments in the __init__ method,
or have a @classmethod decorated method that returns an object.

The __init__ method can also perform type checking (instanceof) on the arguments and
perform different initialization steps based on the type of the argument passed in
(convert types, handle different date formats, etc.)
"""

import math


class Circle:

    # Has a default value for radius
    def __init__(self, radius=1):
        self.radius = radius

    # Provides a way to "construct" a Circle object from a diameter
    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius=diameter / 2)

