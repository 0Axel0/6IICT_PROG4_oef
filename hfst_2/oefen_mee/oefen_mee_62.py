import csv  # importeer de csv library

film_kritieken = [  # de lijst film_kritieken
    {"FILM": "Monty Python and the Holy Grail", "SCORE": 8},
    {"FILM": "Monty Python's Life of Brian", "SCORE": 8.5},
    {"FILM": "Monty Python's Meaning of Life", "SCORE": 7}
]
film_header = ["FILM", "SCORE"] # de lijst film_header

fp = open( "kritieken_to_csv.csv", "w", newline="" )    # maak een nieuw bestand aan
csv_writer = csv.DictWriter( fp , delimiter=";", fieldnames=film_header)    # schrijf de lijst in het bestand

csv_writer.writeheader()    # schrijf de header in het bestand
for rij in film_kritieken:  # voor elke rij in de lijst film_kritieken,
    csv_writer.writerow(rij)    # schrijf de rij in het bestand

fp.close()  # maak het bestand dicht

print(film_kritieken)