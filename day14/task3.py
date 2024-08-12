mynumbers = [1,2,3,4,5]
for i in range(len(mynumbers)):
    for h in range(len(mynumbers)-1):
        if mynumbers[h] < mynumbers[h+1]:
            mynumbers[h], mynumbers[h+1] = mynumbers[h+1], mynumbers[h]
print(mynumbers)