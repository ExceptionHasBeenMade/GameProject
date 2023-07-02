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
        # if True:
        #     if(i == 1):
        #         a1 = port
        #     elif(i == 2):
        #         a2 = port
        #     elif(i == 3):
        #         a3 = port
        #     elif(i == 4):
        #         a4 = port
        #     elif(i == 5):
        #         a5 = port
        #     elif(i == 6):
        #         a6 = port
        #     elif(i == 7):
        #         a7 = port
        #     elif(i == 8):
        #         a8 = port
        #     elif(i == 9):
        #         a9 = port
        #     elif(i == 10):
        #         a10 = port
        #     elif(i == 11):
        #         a11 = port
        #     elif(i == 12):
        #         a12 = port
        #     elif(i == 13):
        #         a13 = port
        #     elif(i == 14):
        #         a14 = port
        #     elif(i == 15):
        #         a15 = port
        #     elif(i == 16):
        #         a16 = port
        #     elif(i == 17):
        #         a17 = port
        #     elif(i == 18):
        #         a18 = port
        #     elif(i == 19):
        #         a19 = port
        #     elif(i == 20):
        #         a20 = port
        #     elif(i == 21):
        #         a21 = port
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