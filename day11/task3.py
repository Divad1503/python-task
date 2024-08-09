a = int(input("What is the number? "))
c = 0
for i in range(a,0,-1):
    c = c + (1 / i)
print(c)