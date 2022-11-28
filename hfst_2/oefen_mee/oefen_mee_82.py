import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/oefen_mee_81.json", "r")
appel = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

print(appel[input("welke dag? ")])