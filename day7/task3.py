str = input("Enter a number ")
int = int(str)
for i in range(1,int):
    if i % 2 == 1:
        print(f"Number is odd: {i}")
    else:
        print(f"Number is even: {i}")