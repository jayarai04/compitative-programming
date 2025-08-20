A = int(input("Enter an integer: "))

original = A

rev = 0
while A > 0:
    digit = A % 10
    rev = rev * 10 + digit
    A //= 10

if original == rev:
    print("Yes")
else:
    print("No")   
