print("Program to find largest no")
print("Array is preinitialized")
array = [10, 5, 11, -9, 15]
largest = array[0]
for i in array:
    if i > largest:
        largest = i

print("largest is:", largest)