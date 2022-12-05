menu = {
    "taco": 7.00,
    "burrito": 7.50,
    "poke bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "super taco": 8.00,
    "tortilla salade": 8.00
}
keuze_lijst = []
totaal = []
while True:
    keuze = input("wat wilt u hebben?")
    keuze = keuze.lower()
    if keuze in menu:
        keuze_lijst.append(keuze)
        print(keuze_lijst)
    else:
        print("dat hebben we niet")

    if keuze == "":
        break

for eten in keuze_lijst:
    totaal.append(menu[eten])
totaal_bedrag = sum(totaal)
print(f"Dat word dan {totaal_bedrag} euro A.U.B.")