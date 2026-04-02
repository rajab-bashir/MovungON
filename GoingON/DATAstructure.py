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

stack = []
# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)
# Peek
topElement = stack[-1]
print("Peek: ", topElement)
# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)
# Stack after Pop
print("Stack after Pop: ", stack)
# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)
# Size
print("Size: ",len(stack))

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# Dequeue
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))

#F STRING
price = 59
txt = f"The price is {price} dollars"
print(txt)

#DictionaryCHANGE
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#NestedDICTIONARY
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

username = input("who are you")

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

  score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

    temperature = int(input('how is it? '))
is_sunny = input("Is it sunny? (yes/no): ")

is_sunny = is_sunny.lower() == "yes"

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")
  else:
    print('bad day')