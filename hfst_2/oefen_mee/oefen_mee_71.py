import csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader:
    eruptions_ld.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar


film_header = ["Year","Name"]


eruptions_ld_verwerkt = []
for index, rij in enumerate(eruptions_ld):
    dictionary = {}
    dictionary["Year"] = abs(int(rij["Year"]))
    dictionary["Name"] = rij["Name"]
    eruptions_ld_verwerkt.append(dictionary)


fp = open( "eruptions_ld_verwerkt.csv", "w", newline="" )    # maak een nieuw bestand aan
csv_writer = csv.DictWriter( fp , delimiter=";", fieldnames=film_header)    # schrijf de lijst in het bestand
csv_writer.writeheader()

for rij in eruptions_ld_verwerkt:
    csv_writer.writerow(rij)

fp.close()
print(eruptions_ld_verwerkt)