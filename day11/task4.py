n = int(input("What is the number? ")) + 1
s = 0
f = 1
for k in range(n):
    if k == 0:
        k = 1
    f = f * k 
    s = s + (1 / f)
print(s)