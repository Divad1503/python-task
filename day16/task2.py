def treetop(high):
    top = "#"
    space = " " * (high+1)
    print(space,top)
    for i in range(high-1):
        space = " " * (high-i)
        top = f"#{top}#"
        print(space,top)
    for i in range(round(high/3)):
        b = high / 3
        if high % 3 == 0:
           space = " " * (high + 2 - round(b))
        a = round(len(top)/3)
        if a % 2 == 0:
            a = round(len(top)/3) - 1
        print(space,"#" * a)
    
high = int(input("How should the tree be\n"))
print(treetop(high))

