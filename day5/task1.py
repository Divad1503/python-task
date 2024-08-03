kelvin = 273.15
Grad = input("How many degrees is the material? ")
Gradint = float(Grad)
kelvinnew = kelvin + Gradint
if kelvinnew >= 0:
    print(f"The material {kelvinnew} kelvin warm")
else:
    print("It can't go lower than 0 kelvin")
    print("0 degrees are 273.15 kelvin")