""" Oefening 5 (  / 4)
Het JSON-bestand kerst_oefening5.json bevat een agenda.
Het zou echter handiger zijn als deze agenda in een CSV-bestand stond.

Lees kerst_oefening5.json in, in een Python variabele.
Schrijf deze vervolgens weg naar een bestand kerst_oefening5.csv.
kerst_voorbeeld5.csv toont hoe dit CSV-bestand er uit moet zien.

ALLES wat je naar dit CSV-bestand schrijft, moet uit het JSON-bestand komen. Manueel zaken ingeven mag dus niet.
Dit zodat het converteren blijft werken, ook wanneer je een andere JSON-agenda zou gebruiken.
Je mag ervanuit gaan dat iedere dag HETZELFDE aantal activiteiten heeft.
"""
import json # importeer json
import csv  # importeer de csv library

fp = open("kerstexamen_deel2 1/kerstexamen_deel2/kerst_oefening5/kerst_oefening5.json", "r")    # open de json file
info = json.load(fp)    # laad json file in variabele
fp.close()  # sluit het bestand

lijst1 = [] # maak lijst aan
lijst2 = [] # maaklijst aan 
for key,value in info.items():  # voor alle keys in de dictionary, geef de waarde
    lijst1.append(key)  # zet de key in de lijst
    lijst2.append(value)    # zet de waarde in een andere lijst

fp = open( "kerstexamen_deel2 1/kerstexamen_deel2/kerst_oefening5/kerst_oefening5.csv", "r" ) # open het csv bestand en lees dit
csv_reader = csv.reader( fp , delimiter=",")    # lees het bestand in met de "," om te weten dat het naar de volgende regel moet 
fp.close()  # sluit het bestand

fp = open( "kerstexamen_deel2 1/kerstexamen_deel2/kerst_oefening5.csv", "w" ) # open het csv bestand en lees dit
csv_writer = csv.writer( fp , delimiter=",")    # schrijf de lijst in het bestand
csv_writer.writerow(lijst1)  # zet de lijst in het csv bestand
csv_writer.writerow(lijst2)  # zet de lijst in het csv bestand
fp.close()  # sluit het bestand
