import math
day = [12,14,10,7,11,13,12,15,15,18,16,13,10,12]
for i in range(len(day)):
    print(f"day{i} = {day[i]}°C")
a = 0

#exercise 3
for i in range(len(day)-1):
    
    tem = day[i] - day[i + 1]
    if a <= abs(tem):
        a = abs(tem)


for i in range(len(day)-1):
    tem = day[i] - day[i + 1]
    if a == abs(tem):
        print(f"Day {i} was {day[i]}°C warm and day {i+1} was {day[i+1]}°C warm and the temperature diffrenz is {abs(tem)}")
        