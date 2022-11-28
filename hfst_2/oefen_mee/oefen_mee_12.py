import json

fp = open("hfst_2/oefen_mee/oefen_mee_12.json", "r")
planning = json.load(fp)
fp.close()

lijst = ["j","n"]

keuze = input("welke dag? ")
dag = planning[keuze]
print(dag)
x = input("wil je de planning veranderen?")
if x == lijst[0]:
    fp = open("hfst_2/oefen_mee/oefen_mee_12.json", "a")
    nieuwe_planning = input("wat is de niuewe planning?")
    planning[keuze] = nieuwe_planning
    json.dump(nieuwe_planning, fp)
    fp.close()
else:
    print("fijne dag!")