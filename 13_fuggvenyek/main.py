ide_ev = 2022

felhasznalo1 = "Virág"
felhasznalo1_kor = 18
felhasznalo2 = "Emese"
felhasznalo2_kor = 20


def mikor_szuletett(nev, kor):
    return f"{nev} {ide_ev - kor}-ban/-ben született"



print(mikor_szuletett("Péter", 42))
print(mikor_szuletett(felhasznalo1, felhasznalo1_kor))
print(mikor_szuletett(felhasznalo2, felhasznalo2_kor))
print(mikor_szuletett(felhasznalo1, 19))



def udvozles(nev):
    print(f"Üdvözöllek {nev}!")

# udvozles(felhasznalo1)
# udvozles("Miki")
# udvozles(felhasznalo2)

