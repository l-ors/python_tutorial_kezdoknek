class Bankszamla:
    def __init__(self, tulajdonos, egyenleg, tranzakciok):
        self.tulajdonos = tulajdonos
        self.egyenleg = egyenleg
        self.tranzakciok = tranzakciok
    
    def szamlaadatok_kiirasa(self):
        print(f"A tuajdonos: {self.tulajdonos} Az egyenleg pedig: {self.egyenleg}ft")