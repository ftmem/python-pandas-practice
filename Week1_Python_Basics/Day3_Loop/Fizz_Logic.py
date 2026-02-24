#Print numbers, but print "fizz" if divisible by 3
for i in range(1, 16):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)

#Count how many numbers are divisible by 3
count = 0
for i in range(1, 16):
    if i % 3 == 0:
        count += 1
print("Fizz count",count)