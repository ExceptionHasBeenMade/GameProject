import json, time, os, keyboard, math#, multiprocessing
from Modules.modules import nextTurn, jsonClosing, freeSpaceCounter, menu

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

multiplier = importedSettings["playerSettings"]["multiplier"]
harborsList = importedHarbors["alls"]
# airportsList = importedAirports["alls"]

money = importedOwns["player"]["money"][0]
broken = False
broken1 = False
definitiveBroken = False

x = 0
i = 0

def reload():
    global shipNo1Name, shipNo1Place, shipNo1Destination, shipNo1IsLoading, shipNo1MaxCapacity
    global shipNo2Name, shipNo2Place, shipNo2Destination, shipNo2IsLoading, shipNo2MaxCapacity

    shipNo1Name = importedConveyance["conveyance"]["ship_NO_1"][0]
    shipNo1Place = str(importedConveyance["conveyance"]["ship_NO_1"][1])
    if(importedConveyance["conveyance"]["ship_NO_1"][2] == "None"):
        shipNo1Destination = "None"
    else:
        shipNo1Destination = importedConveyance["conveyance"]["ship_NO_1"][2]
    shipNo1IsLoading = importedConveyance["conveyance"]["ship_NO_1"][3]
    shipNo1MaxCapacity = importedConveyance["conveyance"]["ship_NO_1"][5]

    shipNo2Name = importedConveyance["conveyance"]["ship_NO_2"][0]
    shipNo2Place = str(importedConveyance["conveyance"]["ship_NO_2"][1])
    if(importedConveyance["conveyance"]["ship_NO_2"][2] == "None"):
        shipNo2Destination = "None"
    else:
        shipNo2Destination = importedConveyance["conveyance"]["ship_NO_2"][2]
    shipNo2IsLoading = importedConveyance["conveyance"]["ship_NO_2"][3]
    shipNo2MaxCapacity = importedConveyance["conveyance"]["ship_NO_2"][5]

reload()

menu("M", "Title", 3)

input()