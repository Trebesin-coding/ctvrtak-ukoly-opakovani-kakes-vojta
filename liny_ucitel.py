import random
import sys
import json

znamka = random.randint(1, 5)
jmeno = input(f"Jak se jmenuješ {znamka}?: ")
with open("liny_ucitel.json", "r") as file:
    data = json.load(file)
bakalari = data

if jmeno not in bakalari:
    print(f"{jmeno} nejsi studentem, chceš být student?")
    pridani = input("ano/ne:")
    if pridani == "ano":
        if jmeno == "vojta":
            data[jmeno] = {"znamky": [], "prumer": []}
        else:
            data[jmeno] = znamka
            data[jmeno] = {"znamky": [], "prumer": []}
    else:
        sys.exit

if jmeno in bakalari:
    if jmeno == "vojta":
        nadrzovani = int(input(f"Můj hvězdnej student. Jakou chceš známku?"))
        data[jmeno]["znamky"].append(nadrzovani)
    else:
        data[jmeno]["znamky"].append(znamka)
    prumer = sum(data[jmeno]["znamky"]) / len(data[jmeno]["znamky"])
    data[jmeno]["prumer"] = round(prumer, 2)
if prumer >= 3:
    print(f"{jmeno} by se měl začít učit 😭😭😭")

print(bakalari)

with open("liny_ucitel.json", "w") as file:
    json.dump(bakalari, file, indent = 4)