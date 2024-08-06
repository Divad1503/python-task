a = int(input("Enter a number "))
b = int(input("Enter number 2 "))
for i in range(1,11):
    if i >= a and i < b:
        continue
    else:
        print(i)