""" Oefening 2 (  / 4)
Bekijk kerst_oefening2.csv. Het bevat de scores die juryleden (rij 1) hebben gegeven in een wedstrijd.
Er waren in totaal 5 deelnemers die beoordeeld zijn (rij 2-6).

In de volgende stappen zal je dit bestand inlezen, verwerken en wegschrijven.
Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" STAP 1:
Lees kerst_oefening2.csv in, in een variabele van Python. 
"""
import csv  # importeer de csv library
fp = open( "kerstexamen_deel1\kerstexamen_deel1\/kerst_oefening2/kerst_oefening2.csv", "r" ) # open het csv bestand en lees dit
csv_reader = csv.reader( fp , delimiter=",")    # de limiter van het bestand is een ","

""" STAP 2:
print voor IEDERE deelnemer zijn scores af. 

VOORBEELD (jou print hoeft niet exact hetzelfde te zijn):
    Deelnemer 1 kreeg volgende scores: 9, 8, 9, 10
    ...
    Deelnemer 5 kreeg volgende scores: 7, 4, 6, 7
"""
deelnemers = [] # lijst van lijsten
teller = 0  # maak een teller aan
for rij in csv_reader:  # voor alle rijen in het bestand, geef de rij
    for deelnemer in enumerate(rij): # voor alle waardes in de lijst geef de waardes en de index terug
        deelnemers.append(deelnemers[0])  #
        teller += 1
print(deelnemers)

""" STAP 3: 
Bereken voor iedere deelnemer de gemiddelde score. 
    Tip: Ieder element in een CSV-bestand is een string. Zet deze eerst om, vooraleer iets te berekenen.

Lukt dit niet?
    Je zult de gemiddelde score nodig hebben voor stap 4. 
    Bereken de gemiddelde score van iedere persoon manueel en voeg deze zelf toe aan de code (bvb. in een lijst).
    Doe je dit, dan krijg je geen punten op STAP 3.
"""


""" STAP 4:
Maak een nieuw bestand kerst_oefening2_verwerkt.csv aan. Dit bestand bevat alle kolommen van kerst_oefening2.csv.
Voeg er nog een nieuwe kolom aan toe. Deze bevat de gemiddelde score van iedere deelnemer (bepaald in STAP 3).

Een voorbeeld van het resultaat is te vinden in kerst_voorbeeld2.csv
"""
fp = open( "kerstexamen_deel1\kerstexamen_deel1\/kerst_oefening2/kerst_voorbeeld2.csv", "w" ) # open het csv bestand en schrijf
csv_reader = csv.reader( fp , delimiter=",")