from my_classes.my_class import MyClass

clss1 = MyClass("Test1")

# This calls the __str__ overriden method that returns the string representation of the object
print(clss1)

# Calling Static Methods
print(clss1.staticmethod())
print(MyClass.staticmethod())

# Calling class methods
print(clss1.class_method())
print("Purpose=" + clss1.class_purpose())

clss2 = MyClass("Test2")
print(clss2)

# Now set the purpose to something different.
MyClass.redefine_purpose("Testing")
print(clss1, clss2)

# This will redefine / overwrite the purpose for all instances of the MyClass class
clss1.redefine_purpose("More Testing")
print(clss1, clss2)

# Calling instance methods
print(clss1.method())

# Calling getter:
print("clss1 name is: " + clss1.name)
