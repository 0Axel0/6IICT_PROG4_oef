""" Oefening 4 (  / 2)
Maak onderstaande opdrachten over dictionaries.

Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" Opdracht 1:
Zoek in onderstaande dictionary de club die het MEESTE kaarten heeft ontvangen.
Print deze club. Opgelet! Dit programma moet ook blijven werken als de dictionary wijzigt.

RESULTAAT: Nederland
"""

aantal_kaarten_wk = {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}
lijst = []  # maak niuewe lijst

for key, value in aantal_kaarten_wk.items():  # voor alle keys in deze dictionary, geef de value terug
    lijst.append(value) # zet de values in een lijst
max = max(lijst)   # bepaal maximum vermogen
for land,kaarten in aantal_kaarten_wk.items(): # voor alle landen in de dictionary geef de kaarten terug
    if kaarten == max:  # als de kaarten overeen komen met het land dat de meeste kaarten heeft dan:
        print(land)    # print dat land

""" Opdracht 2:
Print de waarde bij de key "corners".
"""
wk = {"Duitsland": {"status": "uitgeschakeld", "matchen_gespeeld": 3, "statistieken": {"kaarten": 14, "corners": 9.8, "CS%": 10}}}
print(wk["Duitsland"]["statistieken"]["corners"])   # gaan de dictionary en print de gevraagde waarde die bij de key hoort

""" Opdracht 3:
Vraag de gebruiker om een letter. Verwijder vervolgens alle keys waarin deze letter staat.
    Tip: gebruik if ... in ... om te controleren of een bepaalde letter in de key voorkomt.

Print de gewijzigde dictionary. 
Opgelet! Het programma mag geen onderscheid maken tussen kleine en grote letters.

VOORBEELD:
    Geef een letter op: L
    {"Spanje": 7}

    Geef een letter op: N
    {}

    Geef een letter op: z
    {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}

"""
aantal_kaarten_wk = {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}

lijst = []  # maak lijst aan
aantal_kaarten_wk_aangepast = {}    # maak dictionary aan
letter = input("welke letter? ")    # vraag om een input
letter1 = letter.capitalize()   # zet de input om naar een hoofdletter
letter2 = letter.lower()    # zet de waarde om naar een kleine letter

for landen, kaarten in aantal_kaarten_wk.items():   # voor alle landen in de dictionary, geef alle kaarten terug
    lijst.append(landen)    # zet de landen in de lijst
for waarde in lijst:    # voor alle landen in de lijst:
    if letter or letter1 or letter2 in waarde:  # als de hoofdletter, de kleine letter in het land zit dan:
        lijst.remove(waarde)    # verwijder dat land
    else:   # anders:
        aantal_kaarten_wk_aangepast[waarde]   # zet de waarde in de dictionary
print(aantal_kaarten_wk_aangepast)    # print de dictionary