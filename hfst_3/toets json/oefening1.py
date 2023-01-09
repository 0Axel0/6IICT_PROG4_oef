""" Algemeen (gaat over oefening 1 en 2): (  / 2)
Schrijf bij iedere regel code commentaar (  / 1)
Zorg dat de code geen geeft foutmeldingen (  / 1)
    Opgelet! Code in commentaar wordt niet bekeken.
"""

""" OEFENING 1: (  / 5)
oefening1.json bevat info over Warren Buffett.
Dit is een zeer bekende investeerder.
"""

""" STAP 1: (  / 1)
laad oefening1.json in Python. Zet deze dictionary in een variabele.
Gebruik voor beide delen de JSON-module van Python.

Lukt dit niet? Dan mag je de dictionary rechtstreeks in de variabele plakken.
               Je krijgt dan wel geen punten voor dit onderdeel.
"""
import json # importeer json

fp = open("oefening1.json", "r")    # open de json file
info = json.load(fp)    # laad json file in variabele
fp.close()  # sluit het bestand

""" STAP 2: (  / 1)
print volgende zaken van Warren Buffett in een grote f-string:
    - voornaam
    - geboortedatum
    - bedrijf
    - 1 hobby (bvb. deze op index 3)

Je moet deze info uit de dictionary halen (dus niet manueel invullen).

De print kan er als volgt uit zien:
Warren is geboren op 03-08-1930. Hij is de eigenaar van Berkshire Hathaway. Hiernaast speelt hij ook ukelele.
"""
# ga voor alle ingegeven keys de values printen
voornaam = (info["voornaam"])   
geboortedatum = (info["geboortedatum"])
bedrijf = (info["bedrijf"])
hobby = (info["hobbys"][1])
print(f"{voornaam}, {geboortedatum}, {bedrijf}, {hobby}")

""" STAP 3: (  / 2)
Gebruik code om het minimale en maximale vermogen in de laatste 5 jaar (2017-2021) te bepalen.
Ook als de cijfers van het vermogen zouden wijzigen, moet de code blijven werken.
    Tip: je kan de functies min() en max() toepassen op lijsten. Dit geeft de kleinste/grootste waarde terug.

Lukt dit niet? Dan mag je het minimale en maximale vermogen zelf bepalen.
               Je krijgt dan wel slechts een deel van de punten voor dit onderdeel

Voeg dit minimale en maximale vermogen toe als value aan de hoofddictionary. 
Gebruik hiervoor de keys verm_min en verm_max.
"""

lijst = []  # maak niuewe lijst
vermogen_in_miljard = info["vermogen_in_miljard"]   # ga in de dictionary vermogen_in_miljard
for key, value in vermogen_in_miljard.items():  # voor alle keys in deze dictionary, geef de value terug
    lijst.append(value) # zet de values in een lijst
min_vermogen = min(lijst)   # bepaal min vermogen
max_vermogen = max(lijst)   # bepaal maximum vermogen
print(f"min = {min_vermogen}, max = {max_vermogen}")    # print de vermogens

info["verm_min"] = min_vermogen # zet vermogens in de dictionary
info["verm_max"] = max_vermogen # zet vermogens in de dictionary


""" STAP 4: (  / 1)
Schrijf de gewijzigde dictionary weg naar een NIEUW JSON-bestand.
Bijvoorbeeld oefening1_resultaat.json .
"""

fp = open("toets json.json", "w")   # open het bestand en schrijf
json.dump(info, fp) # schrijf de waardes in het bestand
fp.close()  # sluit het bestand