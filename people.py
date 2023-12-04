from my_classes.person import Person

fred = Person("Fred", 20)

joe = Person("Joe", 30)

print(fred, joe)

fred.age = 11

# Fred should now be 11
print(fred)
