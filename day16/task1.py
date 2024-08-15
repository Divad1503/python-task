test = input("Which word do you test for palidrom?\n")
print("Write it with small letters")

def testen(test):
    start = 0
    end = len(test) - 1
    while start < end:
        teststart = test[start]
        testend = test[end]
        if not testend == teststart:
            exit(0)
        start += 1
        end -= 1
    return True
if testen(test):
    print(f"{test} is a Palindrome")
else:
    print(f"{test} is not a Palindrome")

