import json, time, os, keyboard, math#, threading
from Modules.modules import nextTurn, jsonClosing, freeSpaceCounter

os.system("cls")

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
maxCapacity = 100000

x = 0
i = 0
if True:
    shipNo1Name = importedConveyance["conveyance"]["ship_NO_1"][0]
    shipNo1Place = str(importedConveyance["conveyance"]["ship_NO_1"][1])
    if(importedConveyance["conveyance"]["ship_NO_1"][2] == "None"):
        shipNo1Destination = "None"
    else:
        shipNo1Destination = importedConveyance["conveyance"]["ship_NO_1"][2]
    shipNo1IsLoading = importedConveyance["conveyance"]["ship_NO_1"][3]
    shipNo1Cargo = importedConveyance["conveyance"]["ship_NO_1"][5]

    shipNo2Name = importedConveyance["conveyance"]["ship_NO_2"][0]
    shipNo2Place = str(importedConveyance["conveyance"]["ship_NO_2"][1])
    if(importedConveyance["conveyance"]["ship_NO_2"][2] == "None"):
        shipNo2Destination = "None"
    else:
        shipNo2Destination = importedConveyance["conveyance"]["ship_NO_2"][2]
    shipNo2IsLoading = importedConveyance["conveyance"]["ship_NO_2"][3]
    shipNo2Cargo = importedConveyance["conveyance"]["ship_NO_2"][5]

while True:
    os.system("cls")
    time.sleep(0.2)
    print(" === Information panel === ")
    print("")
    print("M1. == Resources informations == ")
    print("M2. == Transport details == ")
    print("M3. == Shop ==")
    print("M5. == Pass time == ")
    print("")
    print("M6. == Settings == ")
    print("")
    print("Esc. == Exit ==")
    print("")
    while True:
        if(keyboard.is_pressed(m1)):
            time.sleep(0.2)
            i = 2
            while True:
                if(broken):
                    broken = False
                    break
                os.system("cls")
                print(" = Your resources = \n")
                print("M1.> Energy resources")
                print("M2.> Industrial resources")
                print("M3.> Mineable resources")
                print("M4.> Natural resources")
                print("M5.> Military resources\n")
                print("Press nubmer of resources type you want to see details or press esc to exit")
                while True:
                    if(i == 0):
                        i = 1
                        break
                    elif(keyboard.is_pressed("esc")):
                        broken = True
                        break
                    elif(keyboard.is_pressed(m1)):
                        os.system("cls")
                        i = 1
                        resourceChoice = "Energy resources"
                        while True:
                            if(i == 0):
                                break
                            os.system("cls")
                            print(" = Details of your energy resources = ")
                            print("")
                            for resource in importedResources["resources"][resourceChoice]:
                                amount = importedResources["resources"][resourceChoice][resource][1]
                                extraction = importedResources["resources"][resourceChoice][resource][2]
                                extractionPoints = importedResources["resources"][resourceChoice][resource][3]
                                print("M" + str(i) + ".> " + resource + " ↓" )
                                print("Amount: " + str(amount))
                                print("Extraction: " + str(extraction) + ", from: " + str(extractionPoints) + (" extractors" if int(extractionPoints)>1 else " extractor"))
                                print("")
                                i+=1
                            i = 1
                            print("Which " + resourceChoice[:-1].lower() + " do you want to extend")
                            while True:
                                if(keyboard.is_pressed(m1)):
                                    extraction = importedResources["resources"][resourceChoice]["Coal"][2]
                                    extractionPoints = importedResources["resources"][resourceChoice]["Coal"][3]
                                    os.system("cls")
                                    print("You actually have " + str(extractionPoints) + " coal extractors")
                                    costOfNewExtractor = math.pow(extractionPoints, 2)*math.pow(extraction, 2)*10
                                    if(money >= costOfNewExtractor):
                                        print("It's possible to build up another extractor point for " + str(costOfNewExtractor) + "\n\nPress Enter for cofirm or Escape for exit")
                                        while True:
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
                                    while True:
                                        if(keyboard.is_pressed("Enter")):
                                            break
                                        elif(keyboard.is_pressed("Escape") or broken == True):
                                            x = 1
                                            break
                                elif(keyboard.is_pressed(m2)):
                                    pass
                                elif(keyboard.is_pressed(m3)):
                                    pass
                                elif(keyboard.is_pressed(m4)):
                                    pass
                                elif(keyboard.is_pressed(m5)):
                                    pass
                                elif(keyboard.is_pressed("esc") or broken == True):
                                    broken = False
                                    if(x == 1):
                                        i = 1
                                        x = 0
                                    else:
                                        i = 0
                                    break
                    elif(keyboard.is_pressed(m2)):
                        resourceChoice = "Industrial resources"
                        break
                    elif(keyboard.is_pressed(m3)):
                        resourceChoice = "Mineable resources"
                        break
                    elif(keyboard.is_pressed(m4)):
                        resourceChoice = "Natural resources"
                        break
                    elif(keyboard.is_pressed(m5)):
                        resourceChoice = "Military resources"
                        break
                if(i == 3):
                    i = 0
                    break
        elif(keyboard.is_pressed(m2)):
            broken = False
            time.sleep(0.2)
            while True:
                os.system("cls")
                print(" == Transport == ")
                print("")
                print(" = Ships = ")
                print("M1.> " + shipNo1Name + "'s status")
                if(shipNo1Destination == "None"):
                    print("This ship is in the " + shipNo1Place)
                else:
                    print("This ship is " + str(shipNo1Place) + (" turns" if int(shipNo1Place)>1 else " turn") + " far from " + shipNo1Destination)
                i = 0
                print("M2.> " + shipNo2Name + "'s status")
                if(shipNo2Destination == "None"):
                    print("This ship is in the " + shipNo2Place)
                else:
                    print("This ship is " + str(shipNo2Place) + (" turns" if int(shipNo2Place)>1 else " turn") + " far from " + shipNo2Destination)
                print(" = Airplanes = ")
                print("")
                print("Press number of conveyance you want to see details or press esc to exit")
                while True:
                    if(keyboard.is_pressed("esc")):
                        broken = True
                        break
                    elif(keyboard.is_pressed(m1)):
                        conveyanceChoice = "1"
                        break
                    elif(keyboard.is_pressed(m2)):
                        conveyanceChoice = "2"
                        break
                    elif(keyboard.is_pressed(m3)):
                        conveyanceChoice = "3"
                        break
                    elif(keyboard.is_pressed(m4)):
                        conveyanceChoice = "4"
                        time.sleep(0.2)
                        break
                if(broken == True):
                    break
                i = 0
                while True:
                    if(broken == True):
                        broken = False
                        break
                    os.system("cls")
                    if(conveyanceChoice == "1"):
                        print("Details of " + shipNo1Name)
                        if(shipNo1Destination != "None"):
                            print("This ship is " + str(shipNo1Place) + (" turns" if int(shipNo1Place)>1 else " turn") + " far from " + shipNo1Destination)
                            input()
                            break
                        elif(shipNo1Destination == "None" and shipNo1IsLoading == False):
                            while True:
                                os.system("cls")
                                print(" = Ship is ready to put out = \n")
                                print("M1.> Put it out to")
                                print("M2.> See shipping")
                                # print("M3.> See parts condition")
                                print("")
                                print("Press number of thing you want to do or exit by pressing esc")
                                while True:
                                    if(broken == True or broken1 == True):
                                        broken1 = False
                                        broken = False
                                        break
                                    if(keyboard.is_pressed("esc")):
                                        broken = True
                                        break
                                    elif(keyboard.is_pressed(m1)):
                                        while True:
                                            if(broken == True):
                                                broken = False
                                                break
                                            os.system("cls")
                                            print(" = Select destination of your carriage route = ")
                                            actualPlace1 = importedConveyance["conveyance"]["ship_NO_1"][1]
                                            i = 1
                                            for port in importedHarbors["alls"]:
                                                print(str(i) + ".> Send ship to " + port)
                                                if True:
                                                    if(i == 1):
                                                        a1 = port
                                                    elif(i == 2):
                                                        a2 = port
                                                    elif(i == 3):
                                                        a3 = port
                                                    elif(i == 4):
                                                        a4 = port
                                                    elif(i == 5):
                                                        a5 = port
                                                    elif(i == 6):
                                                        a6 = port
                                                    elif(i == 7):
                                                        a7 = port
                                                    elif(i == 8):
                                                        a8 = port
                                                    elif(i == 9):
                                                        a9 = port
                                                    elif(i == 10):
                                                        a10 = port
                                                    elif(i == 11):
                                                        a11 = port
                                                    elif(i == 12):
                                                        a12 = port
                                                    elif(i == 13):
                                                        a13 = port
                                                    elif(i == 14):
                                                        a14 = port
                                                    elif(i == 15):
                                                        a15 = port
                                                    elif(i == 16):
                                                        a16 = port
                                                    elif(i == 17):
                                                        a17 = port
                                                    elif(i == 18):
                                                        a18 = port
                                                    elif(i == 19):
                                                        a19 = port
                                                    elif(i == 20):
                                                        a20 = port
                                                    elif(i == 21):
                                                        a21 = port
                                                i+=1
                                                if(i == 22):
                                                    break
                                            print("")
                                            i = 0
                                            voyageDest = input()
                                            if(voyageDest == "exit"):
                                                break
                                            if(voyageDest == "esc" or voyageDest == "exit"):
                                                broken = True
                                                break
                                            elif(voyageDest.isdigit() != True):
                                                print("Wrong destination entered")
                                                time.sleep(1.5)
                                                continue
                                            if(int(voyageDest) >= 1 and int(voyageDest) <= 21):
                                                i = int(voyageDest)
                                                if True:
                                                    if(i == 1):
                                                        dest1 = ["Gdansk", 0]
                                                    elif(i == 2):
                                                        dest1 = ["Felixstowe", 1]
                                                    elif(i == 3):
                                                        dest1 = ["Rotterdam", 2]
                                                    elif(i == 4):
                                                        dest1 = ["Valencia", 3]
                                                    elif(i == 5):
                                                        dest1 = ["Pireus", 4]
                                                    elif(i == 6):
                                                        dest1 = ["Los Angeles", 5]
                                                    elif(i == 7):
                                                        dest1 = ["New York & New Jersey", 6]
                                                    elif(i == 8):
                                                        dest1 = ["Houston", 7]
                                                    elif(i == 9):
                                                        dest1 = ["Vancouver", 8]
                                                    elif(i == 10):
                                                        dest1 = ["Santos", 9]
                                                    elif(i == 11):
                                                        dest1 = ["Callao", 10]
                                                    elif(i == 12):
                                                        dest1 = ["Colon", 11]
                                                    elif(i == 13):
                                                        dest1 = ["Shanghai", 12]
                                                    elif(i == 14):
                                                        dest1 = ["Jebel Ali", 13]
                                                    elif(i == 15):
                                                        dest1 = ["Mumbai", 14]
                                                    elif(i == 16):
                                                        dest1 = ["Yokohama", 15]
                                                    elif(i == 17):
                                                        dest1 = ["Tanger-Med", 16]
                                                    elif(i == 18):
                                                        dest1 = ["Port Said", 17]
                                                    elif(i == 19):
                                                        dest1 = ["Durban Port", 18]
                                                    elif(i == 20):
                                                        dest1 = ["Neko", 19]
                                                    elif(i == 21):
                                                        dest1 = ["Sydney", 20]
                                                i = 0
                                                while True:
                                                    if(broken == True):
                                                        broken = False
                                                        break
                                                    os.system("cls")
                                                    precisely = importedHarbors["alls"][actualPlace1][dest1[1]]
                                                    for x in precisely:
                                                        eta = precisely[x]
                                                    costs = int(eta[1])*420
                                                    time.sleep(0.2)
                                                    if(costs <= money):
                                                        print(" = Details of sail from " + actualPlace1 + " to " + str(dest1[0]) + " = \n")
                                                        print("Costs: " + str(costs))
                                                        print("ETA: " + str(eta[1]) + " weeks\n")
                                                        print(" >>  PROCEED  <<  > Enter")
                                                        print(" >>  EXIT     <<  > Escape")
                                                        while True:
                                                            if(keyboard.is_pressed("esc")):
                                                                broken = True
                                                                break
                                                            if(keyboard.is_pressed("enter")):
                                                                importedConveyance["conveyance"]["ship_NO_1"][2] = str(dest1[0])
                                                                importedConveyance["conveyance"]["ship_NO_1"][1] = int(eta[1])
                                                                money = money - costs
                                                                importedOwns["player"]["money"][0] = money
                                                                jsonClosing(importedConveyance, pathOfConveyance)
                                                                jsonClosing(importedOwns, pathOfOwns)
                                                                os.system("cls")
                                                                print("This ship has been put out to " + dest1[0])
                                                                voyageDest = "exit"
                                                                time.sleep(1.5)
                                                                break
                                                    else:
                                                        print("You haven't enought money to proceed it")
                                                        time.sleep(1.5)
                                                        break
                                            else:
                                                break
                                    elif(keyboard.is_pressed(m2)):
                                        while True:
                                            os.system("cls")
                                            freeSpace = maxCapacity - freeSpaceCounter("ship_NO_1")
                                            shipNo1Cargo = freeSpace
                                            if(broken1 == True):
                                                break
                                            print("Free cargo space of Ship No. 1 is: " + str(shipNo1Cargo))
                                            if(shipNo1Cargo < 0):
                                                os.system("cls")
                                                print("Error 2.01a[Wrong cargo space]")
                                                input()
                                                os.system("exit")
                                            elif(shipNo1Cargo > maxCapacity):
                                                os.system("cls")
                                                print("Error 2.01b[Wrong cargo space]")
                                                input()
                                                os.system("exit")
                                            elif(shipNo1Cargo == maxCapacity):
                                                print("You can only load ship")
                                                input()
                                                flag = "embark"
                                            elif(shipNo1Cargo == 0):
                                                print("You can only unload ship")
                                                input()
                                                flag = "disembark"
                                            else:
                                                print("What do you want to do\n")
                                                print("M1. Embark")
                                                print("M2. Disembark")
                                                print("Esc. Exit")
                                                while True:
                                                    if(keyboard.is_pressed(m1)):
                                                        flag = "embark"
                                                        break
                                                    elif(keyboard.is_pressed(m2)):
                                                        flag = "disembark"
                                                        break
                                                    elif(keyboard.is_pressed("esc")):
                                                        broken1 = True
                                                        flag = None
                                                        break
                                            if(flag == "embark"):
                                                x = 0
                                                i = 0
                                                for resource in importedResources["resources"]:
                                                    x+=1
                                                    print(str(x) + ". " + resource)
                                                    for cargo in importedResources["resources"][resource]:
                                                        i+=1
                                                        print("   " + str(i) + ". " + cargo.capitalize())
                                                x = 0
                                                embarks = input("\nEnter number of what you want to embark: ")
                                                if(embarks.isnumeric()):
                                                    embarks = int(embarks)
                                                elif(embarks == "exit" or embarks == "esc"):
                                                    broken = True
                                                    break
                                                else:
                                                    print("\nEntered wrong number")
                                                    time.sleep(1.5)
                                                    os.system("cls")
                                                    continue
                                                i = 1
                                                broken = False
                                                if(embarks > 0 and embarks < 26):
                                                    for resource in importedResources["resources"]:
                                                        if(broken == True):
                                                                broken = False
                                                                break
                                                        for cargo in importedResources["resources"][resource]:
                                                            if(broken == True):
                                                                break
                                                            if(i == embarks):
                                                                i = 0
                                                                os.system("cls")
                                                                freeSpace = maxCapacity - freeSpaceCounter("ship_NO_1")
                                                                print("In " + shipNo1Name + " ship is " + str(freeSpace) + " free cargo space")
                                                                count = input("Pass count of " + str(cargo.lower()) + " you want to embark: ")
                                                                if(count == "esc" or count == "exit"):
                                                                    broken = True
                                                                    break
                                                                if(freeSpace - int(count) < 0):
                                                                    print("\nYou haven't enought space in this ship to embark that much.")
                                                                    time.sleep(1.5)
                                                                    os.system("cls")
                                                                    continue
                                                                else:
                                                                    importedCargo["cargo"]["ship_NO_1"][cargo][1] = importedCargo["cargo"]["ship_NO_1"][cargo][1] + int(count)
                                                                    jsonClosing(importedCargo, pathOfCargo)
                                                                    added = importedConveyance["conveyance"]["ship_NO_1"][5] - freeSpace
                                                                    importedConveyance["conveyance"]["ship_NO_1"][5] = importedConveyance["conveyance"]["ship_NO_1"][5] - added
                                                                    jsonClosing(importedConveyance, pathOfConveyance)
                                                                    broken = True
                                                                    if(importedConveyance["conveyance"]["ship_NO_1"][5] == 0):
                                                                        print("You can't load more")
                                                                        time.sleep(1.5)
                                                                        # needToExit = True
                                                                    break
                                                            i+=1
                                                else:
                                                    print("\nEntered wrong number")
                                                    time.sleep(1.5)
                                                    os.system("cls")
                                                    continue
                                            elif(flag == "disembark"):
                                                freeSpace = maxCapacity - freeSpaceCounter("ship_NO_1")
                                                shipNo1Cargo = freeSpace
                                                os.system("cls")
                                                i = 1
                                                print("List of thing you can disembark: ")
                                                for cargo in importedCargo["cargo"]["ship_NO_1"]:
                                                    if(importedCargo["cargo"]["ship_NO_1"][cargo][1] > 0):
                                                        print(str(i) + ". " + importedCargo["cargo"]["ship_NO_1"][cargo][0] + "  --  " + str(importedCargo["cargo"]["ship_NO_1"][cargo][1]) + " to disembark")
                                                        i+=1
                                                i = 0
                                                disembarks = input("Enter number of what you want to disembark: ")
                                                if(disembarks.isnumeric()):
                                                    disembarks = int(disembarks)
                                                elif(disembarks == "exit" or disembarks == "esc"):
                                                    broken = True
                                                    break
                                                else:
                                                    print("\nEntered wrong number")
                                                    time.sleep(1.5)
                                                    os.system("cls")
                                                    continue
                                                for i in range(disembarks):
                                                    if(disembarks == i+1):
                                                        print(importedCargo["cargo"]["ship_NO_1"][i][1])
                                                        input()
                                                    else:
                                                        i+=1
                                    elif(keyboard.is_pressed(m3)):
                                        break
                                if(broken == True):
                                    break
                        elif(shipNo1Destination == "None" and shipNo1IsLoading == True):
                            multiplier = importedConveyance["conveyance"]["ship_NO_1"][4]
                            rlt = multiplier * 120
                            for second in range(int(rlt)):
                                print("This ship is actually busy and will be ready in " + str(rlt) + " seconds")
                                time.sleep(1)
                                rlt = rlt - 1
                                os.system("cls")
                                shipNo1IsLoading = False
                                if(keyboard.is_pressed("esc")):
                                    shipNo1IsLoading = True
                                    broken = True
                                    break
                            importedConveyance["conveyance"]["ship_NO_1"][4] = rlt/120
                            if(importedConveyance["conveyance"]["ship_NO_1"][4] == 0.0):
                                importedConveyance["conveyance"]["ship_NO_1"][3] = False
                            jsonClosing(importedConveyance, pathOfConveyance)
                    if(broken == True):
                        broken = False
                        break
                    elif(conveyanceChoice == "2"):
                        pass
                    elif(conveyanceChoice == "3"):
                        pass
                    elif(conveyanceChoice == "4"):
                        pass
        elif(keyboard.is_pressed(m3)):
            broken = False
            time.sleep(0.2)
            while True:
                os.system("cls")
                print()
        elif(keyboard.is_pressed(m5)):
            time.sleep(0.2)
            while True:
                if(broken == True):
                    broken = False
                    break
                os.system("cls")
                print(" == Pass time == \n")
                print("M1. Pass one turn")
                print("Esc. Exit")
                while True:
                    if(keyboard.is_pressed(m1)):
                        nextTurn(res = True, con = True)
                        break
                    elif(keyboard.is_pressed("esc")):
                        broken = True
                        break
        elif(keyboard.is_pressed(m6)):
            time.sleep(0.1)
            while True:
                if(broken == True):
                    broken = False
                    break
                os.system("cls")
                print(" == Settings == ")
                print("")
                print("M1. Set multiplier for voyage costs")
                print("M2. Assign M- buttons")
                print("")
                print("Esc. Exit")
                while True:
                    if(broken == True):
                        broken = False
                        break
                    if(keyboard.is_pressed(m1)):
                        while True:
                            os.system("cls")
                            print("Actual multiplier is " + str(multiplier))
                            print("")
                            newMultiplier = input("Enter new multiplier or type exit to exit: ")
                            if(newMultiplier.isdigit()):
                                newMultiplier = int(newMultiplier)
                                if(newMultiplier == int(newMultiplier)):
                                    multiplier = newMultiplier
                                    importedSettings["playerSettings"]["multiplier"] = newMultiplier
                                    jsonClosing(importedSettings, pathOfSettings)
                                    print("New multiplier is " + str(newMultiplier))
                                    broken = True
                                    time.sleep(0.75)
                                    break
                                elif(newMultiplier == "exit"):
                                    broken = True
                                    break
                            elif(newMultiplier == "exit" or newMultiplier == "esc"):
                                broken = True
                                break
                            else:
                                print("Wrong multiplier entered")
                                time.sleep(0.5)
                                broken = True
                                break
                    if(keyboard.is_pressed(m2)):
                        os.system("cls")
                        time.sleep(0.2)
                        print("Press button which you want to re-assign")
                        while True:
                            if(keyboard.is_pressed(m1)):
                                new = input("Rewrite M1(" + m1 + ") as(write new key): ")
                                if(new == "exit" or new == "esc"):
                                    broken = True
                                    break
                                m1 = new
                                importedSettings["playerSettings"]["m1"] = new
                                del new
                                broken = True
                            elif(keyboard.is_pressed(m2)):
                                new = input("Rewrite M2(" + m2 + ") as(write new key): ")
                                if(new == "exit" or new == "esc"):
                                    broken = True
                                    break
                                m2 = new
                                importedSettings["playerSettings"]["m2"] = new
                                del new
                                broken = True
                            elif(keyboard.is_pressed(m3)):
                                new = input("Rewrite M3(" + m3 + ") as(write new key): ")
                                if(new == "exit" or new == "esc"):
                                    broken = True
                                    break
                                m3 = new
                                importedSettings["playerSettings"]["m3"] = new
                                del new
                                broken = True
                            elif(keyboard.is_pressed(m4)):
                                new = input("Rewrite M4(" + m4 + ") as(write new key): ")
                                if(new == "exit" or new == "esc"):
                                    broken = True
                                    break
                                m4 = new
                                importedSettings["playerSettings"]["m4"] = new
                                del new
                                broken = True
                            elif(keyboard.is_pressed(m5)):
                                new = input("Rewrite M5(" + m5 + ") as(write new key): ")
                                if(new == "exit" or new == "esc"):
                                    broken = True
                                    break
                                m5 = new
                                importedSettings["playerSettings"]["m5"] = new
                                del new
                                broken = True
                            elif(keyboard.is_pressed(m6)):
                                new = input("Rewrite M6(" + m6 + ") as(write new key): ")
                                if(new == "exit" or new == "esc"):
                                    broken = True
                                    break
                                m6 = new
                                importedSettings["playerSettings"]["m6"] = new
                                del new
                                broken = True
                            jsonClosing(importedSettings, pathOfSettings)
                            if(broken == True):
                                break
                    elif(keyboard.is_pressed("esc")):
                        broken = True
                        break
        elif(keyboard.is_pressed("Escape")):
            broken = False
            os.system("cls")
            time.sleep(0.2)
            print("Quit? \n(Enter/Escape)")
            while True:
                if(keyboard.is_pressed("enter")):
                    exit()
                elif(keyboard.is_pressed("escape")):
                    time.sleep(0.2)
                    broken = True
                    break
            if(broken == True):
                broken = False
                break
