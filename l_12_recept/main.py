oszetevok = []
uj_osszetevo = ""

print("Összetevők megadása - kilépéshez használd a 'kilépés' szót")

while uj_osszetevo != "kilépés":
    uj_osszetevo = input("Adj meg egy összetevőt: ")

    if uj_osszetevo != "" and uj_osszetevo != "kilépés":
        oszetevok.append(uj_osszetevo)
        print(oszetevok)

print()
print("A végső összetevők listája:")
print(oszetevok)