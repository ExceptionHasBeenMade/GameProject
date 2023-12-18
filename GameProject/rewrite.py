import json, time, os, keyboard, math#, multiprocessing
from Modules.modules import nextTurn, jsonClosing, freeSpaceCounter, menu, check

pathOfConveyance = "./GameProject/data/conveyance.json"
pathOfHarbors = "./GameProject/data/harbors.json"
pathOfResources = "./GameProject/data/resources.json"
pathOfSettings = "./GameProject/data/settings.json"
pathOfOwns = "./GameProject/data/owns.json"
pathOfCargo = "./GameProject/data/cargo.json"
pathOfMagazine = "./GameProject/data/magazine.json"

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

connector = open(pathOfMagazine)
importedMagazine = json.load(connector)
connector.close()

m1 = importedSettings["playerSettings"]["m1"]
m2 = importedSettings["playerSettings"]["m2"]
m3 = importedSettings["playerSettings"]["m3"]
m4 = importedSettings["playerSettings"]["m4"]
m5 = importedSettings["playerSettings"]["m5"]
m6 = importedSettings["playerSettings"]["m6"]

mList = [m1, m2, m3, m4, m5, m6]

multiplier = importedSettings["playerSettings"]["multiplier"]
harborsList = importedHarbors["alls"]
# airportsList = importedAirports["alls"]

money = importedOwns["player"]["money"][0]
broken = False
broken1 = False
definitiveBroken = False

def reload():
    global shipName, shipPlace, shipDestination, shipIsLoading, shipMaxCapacity

    if(importedConveyance["conveyance"]["ship_NO_1"][2] == "None"):
        shipNo1Destination = "None"
    else:
        shipNo1Destination = importedConveyance["conveyance"]["ship_NO_1"][2]

    if(importedConveyance["conveyance"]["ship_NO_2"][2] == "None"):
        shipNo2Destination = "None"
    else:
        shipNo2Destination = importedConveyance["conveyance"]["ship_NO_2"][2]

    shipName = [importedConveyance["conveyance"]["ship_NO_1"][0], importedConveyance["conveyance"]["ship_NO_2"][0]]
    shipPlace = [str(importedConveyance["conveyance"]["ship_NO_1"][1]), str(importedConveyance["conveyance"]["ship_NO_2"][1])]
    shipDestination = [shipNo1Destination, shipNo2Destination]
    shipIsLoading = [importedConveyance["conveyance"]["ship_NO_1"][3], importedConveyance["conveyance"]["ship_NO_2"][3]]
    shipMaxCapacity = [importedConveyance["conveyance"]["ship_NO_1"][5], importedConveyance["conveyance"]["ship_NO_2"][5]]

reload()

optionList1 = ["M1. Resources informations", "M2. Transport details", "M3. Shop", "M5. Pass time", "M6. Settings"]
gap1 = [0, 0, 0, 0, 1]

optionList2 = ["M1.> Energy resources", "M2.> Industrial resources", "M3.> Mineable resources", "M4.> Natural resources", "M5.> Military resources"]

optionList3 = ["M1.> Coal", "M2.> Firewood", "M3.> Natural Gas", "M4.> Crude Oil", "M5.> Uran"]
descriptionList3 = ["Amount: ", "Extraction: ", "Extractors: "]
descriptionOperator3 = []

optionList4 = ["M1.> Ever Alot's status", "", "M2.> HMM Copenhagen's status", ""]

emptyList = []

while True:
    time.sleep(0.2)
    menu("M", "Information panel", 3, optionList1, gap=gap1)
    selection = check(mList)
    if(selection == 0):
        while True:
            time.sleep(0.2)
            menu("M", "Your resources", 2, optionList2)
            selection = check(mList)
            if(selection == 0):
                resourceChoice = "Energy resources"
                for resource in importedResources["resources"][resourceChoice]:
                    amount = importedResources["resources"][resourceChoice][resource][1]
                    extraction = importedResources["resources"][resourceChoice][resource][2]
                    extractionPoints = importedResources["resources"][resourceChoice][resource][3]
                    descriptionOperator3.append([str(amount), str(extraction), str(extractionPoints)])
                menu("ForItem", "Details of your energy resources", 1, optionList3, descriptionList=descriptionList3, descriptionOperator=descriptionOperator3)
                print("")
                print("Which energy resource do you want to extend")
                selection = check(mList)
                if(selection == 0):
                    extraction = importedResources["resources"][resourceChoice]["Coal"][2]
                    extractionPoints = importedResources["resources"][resourceChoice]["Coal"][3]
                    os.system("cls")
                    print("You actually have " + str(extractionPoints) + " coal extractors")
                    costOfNewExtractor = math.pow(extractionPoints, 2)*math.pow(extraction, 2)*10
                    if(money >= costOfNewExtractor):
                        print("It's possible to build up another extractor point for " + str(costOfNewExtractor) + "\n\nPress Enter for cofirm or Escape for exit")
                        while True:
                            time.sleep(0.2)
                            if(keyboard.is_pressed("Enter")):
                                money = money - costOfNewExtractor
                                extractionPoints = extractionPoints + 1
                                extraction = extractionPoints * 10
                                importedResources["resources"][resourceChoice]["Coal"][2] = extraction
                                importedResources["resources"][resourceChoice]["Coal"][3] = extractionPoints
                                importedOwns["player"]["money"][0] = money
                                jsonClosing(importedOwns, pathOfOwns)
                                jsonClosing(importedResources, pathOfResources)
                                broken = True
                                break
                            elif(keyboard.is_pressed("Escape")):
                                break
                    else:
                        print("You haven't enought money to build this extractor")
                        time.sleep(1.5)
                        break
                if(selection == 6):
                    selection = -1
                    break
            if(selection == 1):
                pass
            if(selection == 6):
                selection = -1
                break
    if(selection == 1):
        while True:
            time.sleep(0.2)
            menu("M", "Transport", 2, emptyList, esc=False)
            for i in range(2):
                if(shipDestination[i] == "None"):
                    optionList4[int(2*i+1)] = "This ship is in the " + shipPlace[i]
                else:
                    optionList4[int(2*i+1)] = "This ship is " + str(shipPlace[i]) + (" turns" if int(shipPlace[i])>1 else " turn") + " far from " + shipDestination[i]
            menu("M", "Ships", 1, optionList4, cls=False)
            selection = check(mList)
            if(selection == 6):
                selection = -1
                break

    if(selection == 6):
        break
