#Data Structures
#In Python, data structures are ways to store and organize data so they can be used efficiently.
#Python provides built-in data structures(available without importing any library) and allows you to create custom/advanced data structures.

# Example: List(Ordered, mutable (can change), allows duplicates.)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add element
print(fruits[1])         # Access element
print(fruits)
# Example: Tuple(Ordered, immutable (cannot change), allows duplicates.)
coordinates = (10, 20)
print(coordinates[0])
# Example: Set(Unordered, mutable, no duplicates.)
unique_numbers = {1, 2, 3, 3}
unique_numbers.add(4)
print(unique_numbers)  # {1, 2, 3, 4}
# Example: Dictionary
person = {"name": "Alice", "age": 25}
person["city"] = "New York"
print(person["name"])

#Create an algorithm to find the lowest value in a list:
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i
print('Lowest value:', minVal) 
#createMaxmumV
my_array = [7, 12, 9, 4, 11, 8]
maxVal = my_array[0]

for i in my_array:
    if i > maxVal:
        maxVal = i

print("Highest value:", maxVal)
#BUILDinCODES
#print(max(my_array))
#print(min(my_array))


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
