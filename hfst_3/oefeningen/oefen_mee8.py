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
while True:
    keuze = input("wat wilt u hebben?")
    if keuze in menu:
        keuze_lijst.append(keuze)
        print(keuze_lijst)
    else:
        print("dat hebben we niet")

    if keuze == "":
        break
    
for eten in keuze_lijst:
    for key, value in menu[eten]:
        	print(value)