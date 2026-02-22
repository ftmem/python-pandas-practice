#Input multiple values

#get multiple user inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

#print all info using f-string
print(f"Hello {name}! You are {age} years old and live in {city}")

################################
# Ask for 3 numbers
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

#calculate total and average
total = n1 + n2 + n3
average = total / 3

#print results
print("Total:", total)
print("Average:", average)


################
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
print("Max:", max(n1, n2, n3))
print("Min:", min(n1, n2, n3))
######################
