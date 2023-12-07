

array1 = ["tom", "joe", "frank"]

print(array1)
print("Index 0 is " + array1[0])
array1[1] = "sam"
print(array1)

for name in array1:
    print(name)

# Array completion
ten = [*range(10)]  # have to do the * so can decompose the range object into a list
print(ten)

ten_2 = [element for element in range(10)]
print(ten_2)

# Get 0 for as many times in the range
zeros = [0 for i in range(5)]
print(zeros)

# Get just even numbers by going through the range but adding a conditional check that the modulus is 0
even = [i for i in range(10) if i % 2 == 0]
print(even)
