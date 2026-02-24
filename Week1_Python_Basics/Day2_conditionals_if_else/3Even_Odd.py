#Esercise 3a
#Get number from useer
num = int(input("Enter a number: "))

#Check if even or odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exercise 3b
#Get number
num = int(input("Enter a number: "))

#Combind conditions: even and > 10, odd and < 10
if num % 2 == 0 and num > 10:
    print("Even and bigger than 10")
elif num % 2 != 0 and num < 10:
    print("Odd and smaller than 10")
else:
    print("Other case")

#Exercise 3c
#Check divisibility by 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0:    #if divisibility by 3
    print("Divisible by 3")
if num % 5 == 0:     #if divisibility by 5
    print("Divisible by 5")
if num % 3 !=3 and num % 5 != 0:  #if divisibility by neither
    print("Not divisible by 3 or 5")