jahr = int(input("Which year is it? "))
schaltjahr = jahr % 4
a = jahr % 400
b = jahr % 100
if b == 0:
    if a == 0:
        print(f"The year {jahr} is a leap year")
    else:
        print(f"Year {jahr} is not a leap year")
else:
    if schaltjahr == 0:
        print(f"Year {jahr} is a leap year")
    else:
        print(f"Year {jahr} is not a leap year")