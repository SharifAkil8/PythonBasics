print("Hello, World!")

# DECLARING VARIABLES

name = "Alice" # String
age = 30 # Integer
is_student = True # Boolean Data Type

city = "Cordoba"
print(f"My favorite city is {city}")

# LISTS
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Add an item to the end of the list
fruits.append("orange")
print(fruits)

# Remove an item from the list
fruits.remove("banana")
print(fruits)

# CONDITIONAL STATEMENTS

x = 20
if x < 10:
    print("Less than 10")
elif x == 10:
    print("Exactly 10")
else:
    print("Greater than 10")

# LOOPS

for fruit in fruits:
    print(fruit)

count = 5
while count > 0:
    print(count)
    count -= 1

# FUNCTIONS

def greet(name):
    return "Hello " + name + "!"

print(greet("Alice"))

def multiply(x,y):
    return x*y
print(multiply(2,3))