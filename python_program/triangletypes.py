
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

if a == 90 or b == 90 or c == 90:
    print("Right triangle")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse triangle")
else:
    print("Acute triangle")