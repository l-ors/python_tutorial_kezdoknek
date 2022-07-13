szam = 0

while True:
    print(f"A szám jelnlegi értéke: {szam}")
    bevetiel = input("Mennyivel változtassuk a számot? [k = kilépés] ")
    if bevetiel == "k":
        break
    else:
        szam += int(bevetiel)

print(f"A szám végső értéke: {szam}")