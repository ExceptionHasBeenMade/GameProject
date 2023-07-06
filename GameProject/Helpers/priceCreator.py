import json

pathOfPrices = "./GameProject/data/prices.json"
pathOfResources = "./GameProject/data/resources.json"

connector = open(pathOfResources)
importedResources = json.load(connector)
connector.close()

connector = open(pathOfPrices)
importedPrices = json.load(connector)
connector.close()

# importedPrices = {"price" : {}}
i = 0 

for category in importedResources["resources"]:
    for item in importedResources["resources"][category]:
        if(i == 0):
            price = input(f"Pass prices of {item}\n")
            unit = input(f"Pass unit of {item}\n")
            energyValue = input(f"Pass energy value of {item}\n") # In kWh/kg
            importedPrices["price"].update({item : [float(price), unit, float(energyValue)]})
        elif(i == 1):
            price = input(f"Pass price of {item}\n")
            unit = input(f"Pass unit of {item}\n") # pc - one piece
            inaccessible = input(f"Pass chances (in %) of being inaccessible of {item}\n")
            importedPrices["price"].update({item : [float(price), unit, float(inaccessible)/100]})
        elif(i == 2):
            price = input(f"Pass price of {item}\n")
            unit = input(f"Pass unit of {item}\n")

            importedPrices["price"].update({item : [float(price), unit]})
        elif(i == 3):
            price = input(f"Pass price of {item}\n")
            unit = input(f"Pass unit of {item}\n")
            
            importedPrices["price"].update({item : [float(price), unit]})
        elif(i == 4):
            price = input(f"Pass price of {item}\n")
            unit = input(f"Pass unit of {item}\n")

            importedPrices["price"].update({item : [float(price), unit]})
        else:
            continue
    i+=1
    connector = open(pathOfPrices, "w", encoding="utf-8")
    json.dump(importedPrices, connector)
    connector.close()