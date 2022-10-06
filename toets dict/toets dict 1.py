""" Opdracht 1: (  /3)
Onderstaande dictionary toont de gegevens gekoppeld aan de laptop 
van Rens Crijns. Onder de dictionary zijn de opgaves te vinden.
"""

laptop_crijns = {
    "name": "R90Y2ZH1",
    "asset_tag": "R90Y2ZH1",
    "serial": "R90Y2ZH1",
    "model": {"id": 8, "name": "L390 Touch"},
    "status_label": {
        "id": 8,
        "name": "KoopSignpost",
        "status_type": "deployable",
        "status_meta": "deployed",
    },
    "assigned_to": {
        "id": 1957,
        "username": "CRRE071105",
        "name": "Rens Crijns",
        "first_name": "Rens",
        "last_name": "Crijns",
        "employee_number": "CRRE071105",
        "type": "user",
        "created_at": {
            "date": "???",
            "time": "13:36:37"
        },
    },
    "category": {"id": 4, "status": "laptopMETtouch"},
    "manufacturer": {"id": 2, "name": "LENOVO"},
    "supplier": "???",
    "supplier_2": {"id": 1, "name": "SignPost"}
}


""" 1) Verander de waarde, gekoppeld aan de key date. (  /1)
       De waarde moet "2021-11-09" worden.
    Print laptop_crijns om te zien of de wijziging is doorgevoerd. 
"""
laptop_crijns["assigned_to"]["created_at"]["date"]="2021-11-09"


""" 2) Momenteel heeft de laptop van Rens twee leveranciers (suppliers). (  /1)
       Dit is een fout in het systeem. Overschrijf met de waarde van key supplier_2
       de waarde van key supplier. Verwijder vervolgens de key supplier_2. 
    Print laptop_crijns om te zien of de wijziging is doorgevoerd. 
"""
laptop_crijns["supplier"]=laptop_crijns["supplier_2"]
del laptop_crijns["supplier_2"]

""" 3) Er staan een hoop verschillende ID's in de dictionary. (  /1)
       Doorloop de dictionary en print alle waarden gekoppeld aan 
       een id key. Je moet een for-lus gebruiken!
"""
for key,value in laptop_crijns.items():
        print(value)