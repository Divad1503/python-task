a = int(input("How are tokens there? "))
k = ""
q = "."
w = ":"
j = "|"

for i in range(a):
    c = i % 4
    if c == 0:
        k = k + q
    elif c == 1:
        k = k + w
    elif c == 2:
        k = k + j
    elif c == 3:
        k = k + w
print(f"Amount of Tokens:{a}")
print(k)