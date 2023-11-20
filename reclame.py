from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    actie_prijs = prijs-korting*prijs 
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {actie_prijs} euro."
    return uitvoer

print(aanbieding_1(smaak = "aardbei",prijs = 4, korting = 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_percentage = totaal*btw
    output_string = f"Het totaal van alle inkomsten van de week is {totaal} euro, waarover {btw_percentage} euro btw betaald dient te worden."
    return output_string
week_omzet = [220, 430, 125, 160, 205, 90, 345]

print(inkomsten_totaal(week_omzet, 0.09))

def laag_en_hoog(mijn_lijst):
    low_and_high = [min(mijn_lijst), max(mijn_lijst)]
    return low_and_high
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    average = [sum(mijn_lijst)/len(mijn_lijst)]
    output = f"De gemiddelde inkomsten deze week zijn {average} euro."
    return output
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    output = laag_en_hoog(invoer_lijst)
    return output
print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    output = mijn_functie_2(a = invoer_lijst_2[0], b = invoer_lijst_2[1])
    return output
print(combinatie([10,5,3,2,1,2,9]))