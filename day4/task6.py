xstr = input("What is the first number ")
ystr = input("What is the second number ")
x = int(xstr)
y = int(ystr)
if x<=y:
    print("error")
else:
    for i in range(x,y,-2):
        print(i)