import csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.reader( fp , delimiter=";")

eruptions_ll = [] # ld = lijst van dictionaries
for rij in csv_reader:
    eruptions_ll.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar


eruptions_ll_verwerkt = []
for index, rij in enumerate(eruptions_ll):
    if index == 0:
        eruptions_ll_verwerkt.append([rij[1],rij[4]])
    else:
        eruptions_ll_verwerkt.append([abs(int(rij[1])),rij[4].lower()])





fp = open( "eruptions_ll_verwerkt.csv", "w", newline="" )    # maak een nieuw bestand aan
csv_writer = csv.writer( fp , delimiter=";")    # schrijf de lijst in het bestand

for rij in eruptions_ll_verwerkt:
    csv_writer.writerow(rij)

fp.close()
print(eruptions_ll_verwerkt)
