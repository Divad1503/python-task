kelvin = 273.15
Grad = input("Wie viel Grad ist der Stoff? ")
Gradint = float(Grad)
kelvinnew = kelvin + Gradint
if kelvinnew >= 0:
    print(f"Der Stoff ist {kelvinnew} kelvin warm")
else:
    print("Es kann nicht weniger als 0 Kelvin gehen")
    print("0 Grad sind 273.15°C")