""" Oefening 1 (  / 2)
Maak onderstaande opdrachten over dictionaries.
Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" Opdracht 1:
Print voor IEDER element in onderstaande dictionary volgende tekst:
    <key> heb ik <value> uren per week

Voorbeeld:
    wisk heb ik 4 uren per week
    ...
    sph heb ik 2 uren per week
"""
vakken = {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}    # dictionary met gegevens
for vak,value in vakken.items():    # geef alle keys en waardes terug in deze dictionary
    print(f"{vak} heb ik {value} per week") # print de key en de waarde

""" Opdracht 2:
Vraag de gebruiker naar een vak. Print het aantal uur dat dit vak voorkomt in de dictionary.
Als het ingegeven vak niet bestaat, print dan "vak bestaat niet".

VOORBEELD:
    Geef een vak op: wisk
    4

    Geef een vak op: huppel
    vak bestaat niet
"""
vakken = {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}    # dictionary met gegevens
keuze = input("welk vak? ") # vraag om een input
if keuze in vakken: # als de keuze in de dictionary staat dan:
    print(vakken[keuze])    # print de waarde van de keuze
else:   # anders:
    print("vak bestaat niet")   # print dat het vak niet bestaat

""" Opdracht 3:
Schrijf een programma dat onderstaande 2 lijsten combineert in een dictionary.
print deze dictionary. Opgelet! Dit programma moet ook blijven werken als de lijsten wijzigen.
                                De lijsten zullen wel altijd evenveel elementen bevatten.

RESULTAAT: {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}
"""
namen = ["wisk", "prog", "cosn", "sph"] # lijst van waardes
uren = [4,4,2,2]    # lijst van waardes
dict = {}   # maak een dictionary aan
teller = 0  # teller aanmaken
for naam in namen:  # geef alle waardes in de lijst namen terug
    dict[naam] = uren[teller]   # voeg de naam met de bijbehoredende waarde toe aan de dictionary
    teller+=1   # teller +=1
print(dict) # print de dictionary

""" Opdracht 4:
Verander in onderstaande dictionary de key "error" naar "cosn". 
De volgorde van de dictionary hoeft niet hetzelfde te blijven. Print de dictionary. 

RESULTAAT: {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}
"""
vakken = {"wisk": 4, "prog": 4, "error": 2, "sph": 2}    # dictionary met gegevens
for key, value in vakken.items():   # geef alle keys en waardes terug
    if key == "error":  # als de key "error" is dan:
        del(key)    # verwijder dan de key
        vakken["cosn"] = 2    # voeg toe aan dictionary
print(vakken)   # print de dictionary