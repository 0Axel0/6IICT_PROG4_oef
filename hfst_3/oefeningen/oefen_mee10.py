import json

""" Volgende info ontbreekt in oefen_mee10.json:
 - De koningin.
 - Het aantal lopers.

"""
def schaak_info(info):
    teller = 0
    for stuk, stuk_info in info.items():
        teller += 1
        if teller == 6:
            raise KeyError
        if stuk_info["aantal"] == "/":
            raise TypeError
        zin = f"""Er zijn {stuk_info['aantal']} {stuk}. 
                De engelse naam is {stuk_info['engelse_naam']}. 
                Ze bewegen {stuk_info['beweging']}"""
        print(zin)
try:       
    fp = open("hfst_3/oefeningen/oefen_mee10.json", "r")
    info = json.load(fp)
    schaak_info(info)
except FileNotFoundError:
    print("bestand kon niet geladen worden.")
finally:
    try:
        fp.close()
    except:
        print("")