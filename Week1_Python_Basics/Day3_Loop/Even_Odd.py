#Print even numbers from 1 to 20
for i in range(1, 20):
    if i % 2 == 0:   #Check if number is divisible by 2
        print("Even numbers: ",i)

#Print odd numbers from 1 to 20
for i in range(1, 20):
    if i % 2 != 0:  #odd numbers have remainder
        print("Odd numbers: ", i)

#Count how many even numbers exist from 1 to 20
count = 0  #counter variable
for i in range(1, 20):
    if i % 2 != 0:
        count += 1  #increse counter
print("Even count: " ,count)