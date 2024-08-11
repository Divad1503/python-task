a = input("Which word to warp? ")
b = list(a)
k = ""
q = "."
g = 0
w = ":"
for i in range(len(b) * 4):
    c = i % 4
    if c == 0:
        k = k + q
    elif c == 1:
        k = k + w
    elif c == 2:
        k = k + b[g]
        g = g + 1
    elif c == 3:
        k = k + w
k = k + "."
print(k)