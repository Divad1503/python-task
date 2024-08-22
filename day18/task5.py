a = [1,3,5,8,9,3,6]
for i in range(round(len(a)/2)):
    a[i],a[len(a)-1-i] = a[len(a)-1-i],a[i]
print(a)