arr = []
while True:
    number_arr = True
    a = input("Choose a number ")
    if a == "":
        break
    s = int(a)
    for i in range(len(arr)):
        if s == arr[i]:
            print("The number was found. The number is already in the list")
            number_arr = False
            break
        
    if number_arr:
        arr.append(s)
        print("The number was not found. The Number has been added to the list. ")
                
print(arr)
