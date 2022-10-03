""" Niveau 1"""

dict_1={1: 10, 2: 20}
dict_2={3: 30, 4: 40}
dict_3={5: 50, 6: 60}
# Resultaat: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict_1.update(dict_2)
dict_1.update(dict_3)
# print(dict_1)

""" Niveau 2 """
dict = {'a': 'Red', 'b': 'Green', 'c': None}
# Resultaat: {'a': 'Red', 'b': 'Green'}

dict_1 = {}
for keys,value in dict.items():
    if dict[keys] != None:
        dict_1[keys] = value
# print(dict_1)

""" Niveau 3 """
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
# Resultaat: {'a': 400, 'b': 400, 'd': 400, 'c': 300})

dict_tot = {}
for keys1,value1 in dict_1.items():
    dict_tot[keys1] = value1
for keys2,value2 in dict_2.items():
    if keys2 in dict_tot:
        value_tot = dict_tot[keys2] + value2
        dict_tot[keys2] = value_tot
    else:
        dict_tot[keys2] = value2
print(dict_tot)