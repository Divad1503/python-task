Wahl = input("Was willst du berechnen? 1.Fläche 2.Seitenlänge ")
if Wahl == "1":
    Seitea = input("Wie lang ist die erste Seite? ")
    Seiteb = input("Wie lang ist die zweite Seite? ")
    Einheit = input("Welche Einheit willst du? ")
    a = int(Seitea)
    b = int(Seiteb)
    Fläche = a * b
    print(f"Die Fläche ist {Fläche}{Einheit}")
elif Wahl == "2":
    Fläche = input("Wie groß ist der Flächeninhalt? ")
    Seitea = input("Wie groß ist eine Seite? ")
    Einheit = input("Welche Einheit willst du? ")
    a = int(Seitea)
    b = int(Fläche)
    Seiteb = b / a
    print(f"Die Fläche ist {Seiteb}{Einheit}")
else:
    print("Es gibt nur 1 oder 2!")