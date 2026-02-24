#Exercise 4a
#Get number
num = int(input("Enter a number: "))

#Classify number
if num < 10:    #If number less than 10
    print("Small")
elif num <= 50:  #If number between 10 and 50
    print("Medium")
else:  #All other number
    print("Large")

#Exercise 4b
#Get number
num = int(input("Enter a number: "))

#five categories
if num < 10:
    print("SVery mall")
elif num <= 20:
    print("Small")
elif num <= 50:
    print("Medium")
elif num <= 100:
    print("Large")
else:
    print("Very large")


#Exercise 4c
#Get number
num = int(input("Enter a number: "))

#Nested conditions
if num >= 0:
    if num <= 10:
        print("0-10")
    elif num <= 50:
        print("11-50")
    else:
        print("Above 50")
else:
    print("Negative number")