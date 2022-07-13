class Ember:
    def __init__(self, nev, kor, lakhely):
        self.nev = nev
        self.kor = kor
        self.lakhely = lakhely

    def bemutatkozas(self):
        print(f"Én vagyok {self.nev}, {self.kor} éves vagyok, {self.lakhely}-ről/-ról.")

felhasznalo1 = Ember("Ferenc", 20, "Budpaest")
felhasznalo2 = Ember("Péter", 23, "Miskolc")

felhasznalo1.bemutatkozas()
felhasznalo2.bemutatkozas()


