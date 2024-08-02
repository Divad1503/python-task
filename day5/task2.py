Grad = 273.15
Kelvin = input("Wie viel Kelvin ist der Stoff warm?  ")
Kelvinint = float(Kelvin)
Gradnew = Kelvinint - Grad
if Gradnew >= 0:
    print(f"Der Stoff ist {Gradnew}°C warm")
else:
    print("Es kannn nicht weniger als -273.15°C Grad werden")