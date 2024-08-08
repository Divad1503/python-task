number1 = input("What is the number? ")
number2 = input("What is the potenz? ")
a = int(number1)
b = int(number2)
c = 1
if b == 0:
    print("1")
else:
    for i in range(b):
        c = c * a
    print(c)
