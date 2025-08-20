A = int(input("Enter a positive integer: "))

total = 0

for i in range(1, A + 1, 2): 
    total += i

print("Sum of odd numbers =", total)