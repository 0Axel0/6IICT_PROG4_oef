""" Opdracht:
Bekijk machten.csv. In dit bestand zijn drie kolommen gegeven:
    - basis: Getallen van 1 tot en met 10.
    - kwadraat: Het kwadraat van de linksgelegen basisgetallen.
    - derdemacht: De derdemacht van de linksgelegen basisgetallen.
    OPGELET: dit bestand gebruikt komma als scheidingsteken, geen punt-komma.

Momenteel zijn enkel de kolommen basis en kwadraat ingevuld.
De opdracht is als volgt:
    1) Open machten.csv in Python. Print iedere rij van de bekomen tabel. 
    2) Vul de kolom derdemacht aan in deze tabel. 
    3) Schrijf de verwerkte tabel weg naar een nieuw bestand. BVB. machten_verwerkt.csv.
OPGELET: Het verwerkte CSV-bestand moet komma's gebruiken als scheidingsteken. 

Puntenverdeling: (  / 5)
    1) Open en print machten.csv in Python (  / 1).
    2) Vul de kolom derdemacht aan in Python (  / 1).
    3) Schrijf de verwerkte tabel weg naar een nieuw bestand (  / 1).
    4) Schrijf bij iedere regel code commentaar die uitlegt wat je doet ( / 1).
    5) De ingeleverde code bevat geen foutmeldingen (  / 1).
      OPGELET: Voor onderdelen 1, 2 en 3 kijk ik enkel naar code die NIET in commentaar staat.
"""
import csv  # importeer de csv library

fp = open( "machten.csv", "r" ) # open het csv bestand en lees dit
csv_reader = csv.reader( fp , delimiter=",")    # lees het bestand in met de "," om te weten dat het naar de volgende regel moet 


machten_ll = [] # ll = lijst van lijsten
for rij in csv_reader:  # voor alle rijen in het bestand, geef de rij
    machten_ll.append(rij)  # zet alle rijen in een lijst
print(machten_ll)   # print de csv


machten_verwerkt = []   # maak een nieuwe lijst aan

for index, rij in enumerate(machten_ll):    # voor elke rij in de lijst, geef de index en de rij
    derde_macht = index ** 3    # de derde macht is de index tot de derde
    if index == 0:  # als de index 0 is dan:
        machten_verwerkt.append([rij[0],rij[1],rij[2]]) # schrijf de waardes van de eerste rij over
    else:   # anders:
        machten_verwerkt.append([rij[0],rij[1],str(derde_macht)])   # zet de derde macht achter de andere waardes



fp = open( "machten_verwerkt.csv", "w", newline="" )    # maak een nieuw bestand aan
csv_writer = csv.writer( fp , delimiter=",")    # schrijf de lijst in het bestand

for rij in machten_verwerkt:
    csv_writer.writerow(rij)  # zet de lijst in het csv bestand

fp.close()  # close het bestnd
    
    