# Explain lexical scope with an example function.
def outer():
    x = "Python"
    def inner():
        print(x)
    inner()

outer()


# Create a function that uses a global variable and modifies it.
count = 0

def increment():
    global count
    count += 1

increment()
print(count)

# Write a function with a nested inner function and use nonlocal to modify its variable.
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()

# Pass a function as an argument to another function and call it.
def greet():
    return "Hello!"

def call_func(func):
    print(func())

call_func(greet)

# Write a lambda function to calculate the square of a number and use it in a loop.
square = lambda x: x ** 2
for i in range(5):
    print(square(i))

# Store a lambda function inside a dictionary and call it.
ops = {
    'square': lambda x: x * x
}

print(ops )

# What does it mean that Python treats functions as first-class citizens? Explain with example.
def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Harnoor"))

# Write a program that strips white space and converts a string to uppercase.\
s = "  hello world  "
print(s.strip().upper())


# Take a string input and split it by commas and join them using semicolons.
s = "apple,banana,grape"
parts = s.split(",")
result = ";".join(parts)
print(result)

# Check if a string ends with '.com' and starts with 'www'.
url = "www.example.com"
print(url.startswith("www") and url.endswith(".com"))


# Create a list and demonstrate append, pop, and indexing operations.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
fruits.pop()
print(fruits)
print(fruits[0])


# Write a program that counts the number of vowels in a given string using a loop.
s = "Beautiful Day"
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Vowel count:", count)

# Write a function with default and keyword arguments to print a greeting message.

def greet(name="User", message="Welcome!"):
    print(f"Hello, {name}. {message}")

greet()
greet("Harnoor", message="Have a great day!")

# Create a function that accepts any number of arguments and returns their average.
def average(*args):
    return sum(args) / len(args)

print(average(5, 10, 15))

