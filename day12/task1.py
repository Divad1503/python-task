#Bubble sort
numbers = [2,5623,5,52,345,546,325,6,514,641,4,624,12,54574,144,24357,235,7643,667,89,36,7,345]
for i in range(len(numbers)):
    for h in range(len(numbers)-1):
        if numbers[h] > numbers[h+1]:
            numbers[h], numbers[h+1] = numbers[h+1], numbers[h]
print(numbers)
