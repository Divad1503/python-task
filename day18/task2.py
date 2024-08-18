a = [3,8,9,5,1,3,6,7,4]
b = []
print(a)
number = int(input("Which number do you want to delete "))
for i in range(len(a)):
    if number == a[i]:
        continue
    else:
        b = b + [a[i]]
print(b)