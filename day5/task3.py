Wahl = input("Was willst du berechnen? 1.Fläche 2.Seitenlänge ")
if Wahl == "1":
    Seitea = input("How long is the first line? ")
    Seiteb = input("How long is the second line? ")
    Einheit = input("Which unit do you want? ")
    a = int(Seitea)
    b = int(Seiteb)
    Fläche = a * b
    print(f"The area is {Fläche}{Einheit}² big")
elif Wahl == "2":
    Fläche = input("How big is the area? ")
    Seitea = input("How long is the first line? ")
    Einheit = input("Which unit do you want? ")
    a = int(Seitea)
    b = int(Fläche)
    Seiteb = b / a
    print(f"The other line is {Seiteb}{Einheit} long")
else:
    print("Es gibt nur 1 oder 2!")