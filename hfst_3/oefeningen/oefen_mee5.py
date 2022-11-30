""" Niveau 1 & 2
Wat gaat hier mis?
de lijst telt maar 5 waardes, aleen int waardes zijn mogenlijk
"""
try:
    fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )

    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)
except IndexError:
    print("het maximum is 5")
except ValueError:
    print("waarde moet een geheel getal zijn")
""" Niveau 3 (haal uit commentaar) """
while True:
    fruit = input("Element aan lijst toevoegen: ")
    
    if fruit == "":
        break # Loop stopt wanneer gebruiker een lege string ingeeft.
    else:
        fruit_lijst.append(fruit)

print(fruit_lijst)
