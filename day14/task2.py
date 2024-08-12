a = int(input("How many items do you have? "))
c = 0
for i in range(a):
    b = int(input("How much did it cost? "))
    c = c + b
print(f"The items cost {c}$")