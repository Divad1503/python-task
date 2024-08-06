a = input("What is the first number? ")
b = input("What is the second number? ")
aint = int(a)
bint = int(b) +1
c = 0
for i in range(aint,bint):
    if i % 5 == 0:
        c = c+1
print(c)