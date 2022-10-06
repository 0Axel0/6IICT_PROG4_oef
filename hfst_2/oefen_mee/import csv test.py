import csv  # importeer de csv library

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )  # open het bestand dat je wil door het pad aan te geven om er te komen.
csv_reader = csv.reader( fp , delimiter=";")    # laat python weten dat de ; de manier is om naar de volgende kolom te gaan.

for rij in csv_reader:  # voor elke rij in het bestand,
    print(rij)  # print de rij

fp.close() # Na sluiten is CSV niet meer bruikbaar
