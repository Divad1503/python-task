a = [1,3,5,8,9,3]
print(a)
b = int(input("Where do you want to separate "))
c = []
d = []
for i in range(b):
    c = c + [a[i]]
for h in range(len(a)-1,b-1,-1):
    d = d + [a[h]]
print(c,",",d)