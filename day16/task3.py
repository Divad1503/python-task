def tree(high):
    tree = "#"
    space = " " * high 
    for i in range(high):
        print(space,tree)
        tree = f"#{tree}#"
        space = " " * (high - i - 1)
    c = len(tree)
    wood = 0
    for h in range(round(high/3)):
        space = " "
        stamm = '#' * round(c/3)
        if round(c/3) % 2 == 0:
            stamm = stamm + "#"
        space = space * int(abs(c/3))
        print(space,stamm)


a = int(input("How high should the tree be "))
b = tree(a)
print(b)
