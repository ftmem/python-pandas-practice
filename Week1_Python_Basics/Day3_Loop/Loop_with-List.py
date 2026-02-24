#List of numbers
numbers = [2, 5, 8, 11, 14, 17,20]

for number in numbers:
    if number > 10:
        print(number)

#Count numbers greater than 10
numbers = [2, 5, 8, 11, 14, 17,20]
count = 0
for number in numbers:
    if number > 10:
        count += 1
print("Count:",count)

#Sum only numbers greater than 10
numbers = [2, 5, 8, 11, 14, 17,20]
total = 0

for number in numbers:
    if number > 10:
        total += number  #add to total
print("Total:",total)