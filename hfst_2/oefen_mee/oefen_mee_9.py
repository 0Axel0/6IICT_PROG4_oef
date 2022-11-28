import json

fp = open("hfst_2/oefen_mee/oefen_mee_9.json", "r")
quiz = json.load(fp)
fp.close()


for key, onderwerp in quiz["quiz"].items():
    print(key)
    for key2, vraag in onderwerp.items():
        print(vraag["vraag"])
        print(vraag["opties"])

        antwoord = input()
        if antwoord == vraag["antwoord"]:
            print("juist\n")
        else:
            print("fout\n")