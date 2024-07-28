nummer1 = input("What is the first nummer ")
nummer2 = input("What is the second nummer ")
x = int(nummer1)
y = int(nummer2)
odd = (x % 2)

if odd == 0:
    sum1 = x + y
    difference = x - y

    print(f"The sum is {sum1} and the difference is {difference}")
else:
    product = x * y
    division = x / y
    print(f"The product is {product} and the division is {division}")
