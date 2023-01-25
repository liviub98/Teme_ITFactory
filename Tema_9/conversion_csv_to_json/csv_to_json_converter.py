import csv
import json

# Sa se scrie o functie care citeste date dintr-un fisier csv
# si le scrie intr-un fisier json. Functia primeste numele fisierelor ca parametri.

with open('login_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open('login_data.json', 'w') as f:
    json.dump(data, f, indent=4)

