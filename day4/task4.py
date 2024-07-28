xint = input("Enter first number ")
yint = input("Enter second number ")
x = int(xint)
y = int(yint)
if x >= y:
    print("error")
else:
    for i in range(x, y + 1):
        print(i)