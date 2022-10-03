""" Niveau 1 """
dict = {
    "belgie": {
        "provincie": {
            "naam": "limburg",
            "weetjes": {
                "oppervlakte":  2.422,
                "inwoners": 885.951,
                "gouverneur": "Jos Lantmeeters"
            }
        }
    }
}
x = dict["belgie"]["provincie"].pop("weetjes")
dict["belgie"]["provincie"]["informatie"] = x
# print(dict)
# print(dict["belgie"]["provincie"]["informatie"]["gouverneur"])

""" Niveau 3 """
extra_info = [  ["mannen", 49.77], 
                ["vrouwen", 50.23], 
                ["hoofdstad", "hasselt"] ]

extra_informatie = {}
for waarde in extra_info:
    for index,cel in enumerate(waarde):
        extra_informatie[waarde[0]] = waarde[1]
dict["belgie"]["provincie"]["informatie"]["extra_info"] = extra_informatie
print(dict)