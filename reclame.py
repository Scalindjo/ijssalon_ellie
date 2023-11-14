def aanbieding_1(smaak, prijs, korting):
    actie_prijs = prijs-korting*prijs 
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {actie_prijs} euro."
    return uitvoer
print(aanbieding_1(smaak = "aardbei",prijs = 4, korting = 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    return totaal

week_omzet = [220, 430, 125, 160, 205, 90, 345]

print(f"Het totaal van alle inkomsten van de week is {inkomsten_totaal(week_omzet)} euro, waarover {} euro btw betaald dient te worden.")