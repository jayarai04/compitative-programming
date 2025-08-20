a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number: "))

if a>b and b>c:
  print(a,"is maximum")
elif b>a:
  print(b, "is maximum")
else: 
  print(c, "is maximum")