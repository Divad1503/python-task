n = int(input("What is the number? ")) + 1
s = 0
for k in range(1,n):
    s = s + (1 / (k * k))
print(s)