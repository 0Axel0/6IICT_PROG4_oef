""" Oefening 6 (  / 3)
Onderstaande code implementeert het spel woordzoeker.
Hier zal een gebruiker een willekeurig (Engels) woord proberen raden.
Maak het programma beter bestand tegen fouten door de 2 stappen te volgen.

Je moet enkel commentaar schrijven bij code die je zelf hebt geschreven.
"""

import requests

""" STAP 1:
In onderstaande functie moet de gebruiker een woord ingeven. Raise in deze functie volgende errors:
    - TypeError als het ingegeven woord karakters bevat die geen letters zijn.
                TIP: gebruik hiervoor de string methode isalpha.
    - IndexError als de LENGTE van het ingegeven woord niet gelijk is aan de moeilijkheid.
Schrijf duidelijk bij de error waarom deze geraised is.
"""
def geef_woord_in(moeilijkheid): # De waarde van moeilijkheid is een geheel getal.
    ingegeven_woord = input("Welk woord zoeken we: ")
    if ingegeven_woord.isalpha: # als het ingegeven woord bestaad uit letters dan:
        if len(ingegeven_woord) != moeilijkheid:    # als de lengte van het woord hetzelfde is als de ingegeven lengte dan: 
            return ingegeven_woord  # geef het woord terud
        else:   # anders:
            print("de lengte van het ingegeven woord klopt niet")   # print de foutcode
            raise IndexError    # raise bepaalde error
    else:   # anders:
        print("woord bevat karakters")  # print de foutcode
        raise TypeError # raise de error


""" STAP 2: 
Vang onderstaande specifieke errors op in de instellingen (beschrijf het probleem zo duidelijk mogelijk).
Enkel als er GEEN exception optreedt, mag alle code onder START SPEL uitgevoerd worden.
    - De gebruiker geeft geen geheel getal op in moeilijkheid (ValueError).
    - Geen verbinding met de API (requests.exceptions.ConnectionError)
    - Vang alle andere mogelijke problemen op met een algemene exception.
"""
# INSTELLINGEN
try:    # probeer:
    moeilijkheid = int(input("Hoeveel letters in te zoeken woord: "))
    if moeilijkheid == float:   # als het getal een komma getal is dan:
        raise ValueError    # raise de error
except ValueError:  # als het ingegeven getal een komma getal is dan:
    print("getal moet en geheel getal zijn")  # print de foutcode
try:    # probeer:
    url = f"https://random-word-api.herokuapp.com/word?length={moeilijkheid}"
except requests.exceptions.ConnectionError: # als er geen verbinding gemaakt kan worden dan:
    print("kan geen verbinding maken met de API")   # print de foutcode
except: # als het niet werkt dan:
    print("er is een probleem ondervinden") # print de foutcode
te_zoeken_woord =  requests.get(url).text[2:-2]
print(f"ENKEL voor ontwikkelaars. Het te_zoeken_woord is {te_zoeken_woord}\n")
# EINDE INSTELLINGEN

# START SPEL
for ronde in range(moeilijkheid):
    print(f"RONDE {ronde+1}/{moeilijkheid}")

    ingegeven_woord = geef_woord_in(moeilijkheid)


    # VERGELIJKEN WOORDEN
    for index, letter in enumerate(ingegeven_woord):
        if letter == te_zoeken_woord[index]:
            print(f"{letter} staat op de juiste positie.")
        elif letter in te_zoeken_woord:
            print(f"{letter} komt voor in woord, maar staat op verkeerde positie.")
        else:
            print(f"{letter} zit niet in woord.")
    if te_zoeken_woord == ingegeven_woord:
        print(f"Je hebt het woord '{te_zoeken_woord}' geraden!")
        break
    # EINDE VERGELIJKEN WOORDEN




    print("------------------")
else:
    print(f"Je hebt het woord niet gevonden. Het woord was '{te_zoeken_woord}'.")
