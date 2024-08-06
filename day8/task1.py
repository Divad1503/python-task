a = int(input("Enter number 1 "))
b = int(input("Enter number 2 "))
for i in range(1,11):
    if i == a or i == b:
        continue
    else:
        print(i)