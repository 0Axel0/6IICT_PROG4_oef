boodschappen_lijst = ["appel","doerian","banaan","doerian","appel","kers",
"kers","mango","appel","appel","kers","doerian","banaan",
"appel","appel","appel","appel","banaan","appel"]

"""
Oplossing:
boodschappen_dict = {'appel': 9, 'doerian': 3, 'banaan': 3, 'kers': 3, 'mango': 1}

"""
boodschappen_dict = {}
for fruit in boodschappen_lijst:
    if fruit in boodschappen_dict:
        boodschappen_dict[fruit] +=1
    else:
        boodschappen_dict[fruit] = 1
print(boodschappen_dict)