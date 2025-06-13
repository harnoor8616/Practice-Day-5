# Create a list of 5 student names and print the list.
students = ["Aman", "Simran", "Rahul", "Neha", "Priya"]
print(students)

# Given a string, print each character on a new line.
string = "Python"
for char in string:
    print(char)



# What is the output of id(10) and id(10.0)? Explain the result
print(id(10))      # same
print(id(10.0))    # different

# Write a program that takes two numbers and prints their sum, difference, product, and quotient.
a = 20
b = 5
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)


# Given two numbers, print whether the first is greater than, less than, or equal to the second.
a = 8
b = 12
if a > b:
    print("First is greater")
elif a < b:
    print("First is less")
else:
    print("Both are equal")


# Check if the number 4 is both greater than 2 and less than 10 using logical operators.
num = 4
print(num > 2 and num < 10)


# Write a program to check if an element exists in a list using membership operator.
colors = ["red", "blue", "green"]
print("blue" in colors)


# Explain what a += 3 does. Show with a working example.
a = 5
a += 3
print(a)

# Write a program to check if a number is even or odd.
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Use a loop to print all numbers from 1 to 20, except multiples of 5 (use continue).
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)


# Write a program to calculate the factorial of a number using a while loop.
num = 5
fact = 1
while num > 0:
    fact *= num
    num -= 1
print(fact)



# Take an input age and print whether the person is a child, teenager, adult, or senior.
age = 45
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")



# Use a nested if condition to determine if a year is a leap year.
year = 2024
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Not a Leap Year")



# Define a function that returns the square of a number.
def square(n):
    return n * n

print(square(6))


# Write a function that takes a list of numbers and returns the maximum number.
def find_max(lst):
    return max(lst)

print(find_max([2, 45, 12, 99, 5]))


