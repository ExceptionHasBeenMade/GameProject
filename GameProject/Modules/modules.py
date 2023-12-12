import json, os, time#, keyboard, math

pathOfConveyance = "./GameProject/data/conveyance.json"
pathOfHarbors = "./GameProject/data/harbors.json"
pathOfResources = "./GameProject/data/resources.json"
pathOfSettings = "./GameProject/data/settings.json"
pathOfOwns = "./GameProject/data/owns.json"
pathOfCargo = "./GameProject/data/cargo.json"

connector = open(pathOfResources)
importedResources = json.load(connector)
connector.close()

connector = open(pathOfHarbors)
importedHarbors = json.load(connector)
connector.close()

connector = open(pathOfConveyance)
importedConveyance = json.load(connector)
connector.close()

connector = open(pathOfSettings)
importedSettings = json.load(connector)
connector.close()

connector = open(pathOfOwns)
importedOwns = json.load(connector)
connector.close()

connector = open(pathOfCargo)
importedCargo = json.load(connector)
connector.close()

def jsonClosing(variable, path):
    connector = open(path, "w", encoding="utf-8")
    json.dump(variable, connector)
    connector.close()

def freeSpaceCounter(conveyance, space = 0):
    connector = open(pathOfCargo)
    importedCargo = json.load(connector)
    connector.close()
    for item in importedCargo["cargo"][conveyance]:
        space = space + importedCargo["cargo"][conveyance][item][1]
    return space

def nextTurn(res = False, con = False):
# Resources
    if(res):
        for resourceChoice in importedResources["resources"]:
            for resource in importedResources["resources"][resourceChoice]:
                extractionPoints = importedResources["resources"][resourceChoice][resource][3]
                extraction = importedResources["resources"][resourceChoice][resource][2]
                amount = importedResources["resources"][resourceChoice][resource][1]

                extracted = extractionPoints*extraction
                amount = extracted + amount

                importedResources["resources"][resourceChoice][resource][1] = amount
                jsonClosing(importedResources, pathOfResources)
# Conveyance
    if(con):
        for conveyance in importedConveyance["conveyance"]:
            if(importedConveyance["conveyance"][conveyance][2] == "None"):
                pass
            else:
                if(int(importedConveyance["conveyance"][conveyance][1]) - 1 == 0):
                    importedConveyance["conveyance"][conveyance][1] = importedConveyance["conveyance"][conveyance][2]
                    importedConveyance["conveyance"][conveyance][2] = "None"
                else:
                    importedConveyance["conveyance"][conveyance][1] = int(importedConveyance["conveyance"][conveyance][1]) - 1
            jsonClosing(importedConveyance, pathOfConveyance)

def menu(mode, title, level, optionsList, gap=[], cls=False, sleep=0):
    if(cls):
        os.system("cls")
    if(sleep > 0):
        time.sleep(int(sleep))
    if(mode == "M"):
        print(" " + ("="*level) + " " + title + " " + ("="*level) + " ")
        print("")
        for i in range(len(optionsList)):
            try:
                if(gap[i] == 1):
                    print("")
            except:
                print(IndexError)
            else:
                print(optionsList[i])
        print("")
        print("Esc. Exit")

# for res in importedCargo["cargo"][conveyance][item]:
#     for item in importedCargo["cargo"]:#[conveyance]:
#         space = space + item[1]
# print(freeSpaceCounter("ship_NO_1"))