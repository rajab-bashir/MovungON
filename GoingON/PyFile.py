#conditions
age = int(input("Enter your age: "))
name = input("Enter your name: ")

if age >= 18:
    if name.lower() == "bashir":
        print("You are eligible!")
    else:
        print("Name not allowed.")
else:
    print("You are underage.")

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "Pass"
elif marks >= 40:
    grade = "D"
elif marks >= 30:
    grade = "E"
else:
    grade = "F"

print(f"Grade: {grade}")
status = "Pass" if marks >= 50 else "Fail"

print(f"Grade: {grade}")
print(f"Status: {status}")

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

    age = int(input("Enter your age: "))

s = "Adult" if age >= 18 else "Minor"

print(s)

#LOOPS
#Loops in Python are used to repeat actions efficiently
# For loops (counting through items) 
#While loops (based on conditions)

#For Loop
for n in range(10):
    print(n)

numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    total += num

print("Total:", total) 
li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x),   

#WHILEloop
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")

    # Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
        
    print(a[i])
    i += 1

#OR
a = "geeksforgeeks"

for ch in a:
    if ch == 'e' or ch == 's':
        continue
    print(ch)

i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break") 

 #Almost any value is evaluated to True if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0., false,non
