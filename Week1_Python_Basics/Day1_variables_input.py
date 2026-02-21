# Day 1 — Variables & Input
#Assign variables and print
name = "Ali"
age = 25
height = 1.75
#print variables
print("Name is " + name)
#print("Name:", name)
print("Age is " + str(age))
#print("Age:", age)
print("Height is " + str(height))
#print("Height:", height)



#Input from user information
user_name = input("Enter your name: ")
user_age =int(input("Enter your age: "))

#print inputs
print("Hello", user_name)
print("Your age", user_age, "years old")


#Simple arithmetic
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

sum_total = number1 + number2
difference = number1 - number2
product = number1 * number2

print("sum:", sum_total)
print("difference:", difference)
print("product:", product)


# Get a number from the user and print if it is Big or Small
number = int(input("Enter a number: "))
if number > 10:
    print("Big")
else:
    print("Small")

# Compare two numbers
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
if first > second:
    print("First is bigger")
elif first < second:
    print("Second is bigger")
else:
    print("Both are equal")



