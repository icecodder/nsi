from pprint import pprint

tab1 = []

for table in range(11):
    resultats = []

    for i in range(11):
        resultats.append(table * i)

    tab1.append(resultats)

pprint(tab1)
