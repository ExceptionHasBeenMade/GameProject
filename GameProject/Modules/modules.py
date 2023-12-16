import json, os, time, keyboard

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

def menu(mode, title, level, optionsList, descriptionList=[], descriptionOperator=[], gap=[], cls=True, sleep=0):
    if(cls):
        os.system("cls")
    if(sleep > 0):
        time.sleep(int(sleep))
    if(mode == "M"):
        print(" " + ("="*level) + " " + title + " " + ("="*level) + " ")
        print("")
        for i in range(len(optionsList)):
            if(gap != []):
                try:
                    if(gap[i] == 1):
                        print("")
                except:
                    print(IndexError)
                else:
                    print(optionsList[i])
            else:
                print(optionsList[i])
        print("")
        print("Esc. Exit")
    elif(mode == "ForItem"):
        print(" " + ("="*level) + " " + title + " " + ("="*level) + " ")
        print("")
        for i in range(len(optionsList)):
            if(gap != []):
                try:
                    if(gap[i] == 1):
                        print("")
                except:
                    print(IndexError)
                else:
                    print(optionsList[i])
            else:
                print(optionsList[i])
                for i in range(len(descriptionList)):
                    if(descriptionList[i].find("\n") > -1):
                        print(descriptionList[i][:-1] + descriptionOperator[i][i])
                        print(descriptionList[i+1] + descriptionOperator[i][i+1], end="")
                        print(descriptionList[i+2] + descriptionOperator[i][i+2])
                    else:
                        print(descriptionList[i] + descriptionOperator[i][i], end="")
        input()

def check(mList):
    while True:
        if(keyboard.is_pressed(mList[0])):
            return 0
        elif(keyboard.is_pressed(mList[1])):
            return 1
        elif(keyboard.is_pressed(mList[2])):
            return 2
        elif(keyboard.is_pressed(mList[3])):
            return 3
        elif(keyboard.is_pressed(mList[4])):
            return 4
        elif(keyboard.is_pressed(mList[5])):
            return 5
        elif(keyboard.is_pressed("esc")):
            return 6

def jsonClosing(variable, path):
    connector = open(path, "w", encoding="utf-8")
    json.dump(variable, connector)
    connector.close()

# for res in importedCargo["cargo"][conveyance][item]:
#     for item in importedCargo["cargo"]:#[conveyance]:
#         space = space + item[1]
# print(freeSpaceCounter("ship_NO_1"))