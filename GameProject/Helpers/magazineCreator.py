import json

pathOfHarbors = "./GameProject/data/harbors.json"
pathOfResources = "./GameProject/data/resources.json"
pathOfMagazines = "./GameProject/data/magazine.json"

connector = open(pathOfMagazines)
importedMagazines = json.load(connector)
connector.close()

connector = open(pathOfResources)
importedResources = json.load(connector)
connector.close()

connector = open(pathOfHarbors)
importedHarbors = json.load(connector)
connector.close()

importedMagazines = {"magazine" : {}}

for harbor in importedHarbors["alls"]:
    importedMagazines["magazine"].update({harbor : {}})
    for category in importedResources["resources"]:
        # importedMagazines["magazine"][harbor].update({category : {}})
        for item in importedResources["resources"][category]:
            importedMagazines["magazine"][harbor].update({item : 0})
            # importedMagazines["magazine"][harbor][category].update({item : 0})

connector = open(pathOfMagazines, "w", encoding="utf-8")
json.dump(importedMagazines, connector)
connector.close()

            # lenght = input("Podaj długość trasy z punktu " + harbor + " do " + destination + ": ")
            # harbor1 = [destination, lenght]
            # Json["alls"][harbor].append(harbor1)
            # connector = open(pathOfJson, "w", encoding="utf-8")
            # json.dump(Json, connector)
            # connector.close()