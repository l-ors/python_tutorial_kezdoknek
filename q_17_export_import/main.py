import bankszamla
import segito_fuggvenyek

feri_bankszamlaja = bankszamla.Bankszamla("Feri", 25000, [200000, -15000, -2000, 25000, -5000])


feri_bankszamlaja.szamlaadatok_kiirasa()

segito_fuggvenyek.tranzakciok_megjelenitese(feri_bankszamlaja.tranzakciok)

segito_fuggvenyek.teljes_kiadas(feri_bankszamlaja.tranzakciok)

segito_fuggvenyek.teljes_bevetel(feri_bankszamlaja.tranzakciok)


