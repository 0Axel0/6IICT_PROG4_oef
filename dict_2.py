""" Opdracht 2:
Je krijgt een lijst van lijsten genaamd landen_steden.
1) Vorm deze om naar een dictionary van lijsten.
   De eerste lijst bevat alle keys. Deze moeten gekoppeld worden aan de overige lijsten.
   
   Te bekomen dictionary:
   {
    "USA":  ["Boston", "Pittsburgh", "Washington"],
    "UK":   ["London", "Edinburgh", "Belfast"],
    "Frankrijk": ["Parijs", "Lyon", "Avignon"],
    "Duitsland: ["Keulen", "Berlijn"]
   }

2) Vraag de gebruiker om een stad. 
   Gebruik de opgestelde dictionary om het land te printen waarin deze stad zich bevindt.
   >>> input: Lyon
       Frankrijk
"""
landen_steden = [
    ["USA", "UK", "Frankrijk", "Duitsland"],    # Landen
    ["Boston", "Pittsburgh", "Washington"],     # Steden USA
    ["London", "Edinburgh", "Belfast"],         # Steden UK
    ["Parijs", "Lyon", "Avignon"],              # Steden Frankrijk
    ["Keulen", "Berlijn"]                       # Steden Duitsland
]



dict_land = {}                                        # maak een nieuwe dictionary aan.
for index, land in enumerate(landen_steden[0]):       # geef de index en het land terug van alle waardes in de eerste lijst van "landen_steden".
    dict_land[land] = landen_steden[index+1]          # zet het eerste land als de key in de dictionary met de tweede lijst als waarde.
                                                      # ga verder tot dat de alle landen van de eerste lijst zijn gebruikt met de als waardes de volgende lijst.

print(dict_land)                                      # print de nieuwe dictionary.

stad = input("Geef een stad: ")                       # variabele stad is een input
for land, steden in dict_land.items():                # geef de lande en de steden in de dictionary "dict_land".
    if stad in steden:                                # als de stad in het de key van dat land zit dan,
        print(land)                                   # print het land.
    else:                                             # anders,
        print("Stad niet in lijst.")                  # print "Stad niet in lijst.". 
