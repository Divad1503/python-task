Münzen = [("2 Euro",200),
          ("1 Euro",100), 
          ("50 Cent",50), 
          ("20 Cent",20), 
          ("10 Cent",10), 
          ("5 Cent",5), 
          ("2 Cent",2), 
          ("1 Cent",1)
          ]
betrag = 1553
ergebnis = []
for name,wert in Münzen:
    anzahl = betrag // wert
    if anzahl > 0:
        ergebnis.append(f"{anzahl}x {name}")
        betrag -= anzahl * wert
print(ergebnis)
