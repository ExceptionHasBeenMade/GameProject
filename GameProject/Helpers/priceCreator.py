import json

pathOfPrices = "./GameProject/data/prices.json"
pathOfResources = "./GameProject/data/resources.json"

connector = open(pathOfResources)
importedResources = json.load(connector)
connector.close()

connector = open(pathOfPrices)
importedPrices = json.load(connector)
connector.close()

importedPrices = {"price" : {}}

for category in importedResources["resources"]:
    for item in importedResources["resources"][category]:
        price = input(f"Pass prices of {item}\n")
        unit = input(f"Pass unit of {item}\n")
        importedPrices["price"].update({item : [price, unit]})

connector = open(pathOfPrices, "w", encoding="utf-8")
json.dump(importedPrices, connector)
connector.close()