# napojnica i porez su dati u procentima

def solve(cena, napojnica, porez):
    totalCost = cena + (cena * napojnica / 100) + (cena * porez / 100)
    return "Ukupna cena usluge je %s RSD." % round(totalCost)

print(solve(1250.00, 8, 20))
