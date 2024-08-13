day = [12,14,10,7,11,13,12,15,15,18,16,13,10,12]
a = int(input("On which day do you want to know the tempeture? "))
for i in range(a,13):
    if a == 13:
        print("On day 13 it was 12°C warm and the next days a re unknown")
    else:
        b = i + 1
        c = day[i]
        d = day[i + 1]
        print(f"Day {i} was {c}°C warm and day {b} was {d}°C warm")
