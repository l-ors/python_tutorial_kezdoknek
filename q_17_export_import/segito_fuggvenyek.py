def tranzakciok_megjelenitese(tranzakciok):
    for tranzakcio in tranzakciok:
        print(f"{tranzakcio}ft értékű tranzakció")

def teljes_kiadas(tranzakciok):
    kiadasok_osszege = 0
    for tranzakcio in tranzakciok:
        if tranzakcio < 0:
            kiadasok_osszege += tranzakcio
    print(f"A teljes kiadások összege: {kiadasok_osszege}ft")

def teljes_bevetel(tranzakciok):
    bevetelek_osszege = 0
    for tranzakcio in tranzakciok:
        if tranzakcio > 0:
            bevetelek_osszege += tranzakcio
    print(f"A teljes bevételek összege: {bevetelek_osszege}ft")