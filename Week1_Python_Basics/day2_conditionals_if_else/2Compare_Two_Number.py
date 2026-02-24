# Compare Two Numbers
#Exercise 2a
# Get two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Compare numbers
if a > b:                 # If first is bigger
    print("First is bigger")
elif a < b:               # If second is bigger
    print("Second is bigger")
else:                     # If equal
    print("Both are equal")

# Exercise 2b
# Get two numbers
a = int(input("A: "))
b = int(input("B: "))

# Check if A is bigger or equal
if a >= b:
    print("A is bigger or equal")
else:
    print("B is bigger")

# Exercise 2c
# Get three numbers
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

# Compare all three to find biggest
if a >= b and a >= c:      # If a is bigger or equal to b and c
    print("A is biggest")
elif b >= a and b >= c:    # If b is bigger or equal to a and c
    print("B is biggest")
else:                       # Otherwise c is biggest
    print("C is biggest")

#Exercise 2d
# Store three numbers in a list
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

# Print maximum and minimum using built-in functions
print("Maximum:", max(a, b , c))  # Print largest number
print("Minimum:", min(a, b, c))  # Print smallest number