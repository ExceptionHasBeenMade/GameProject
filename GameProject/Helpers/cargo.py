import json
from Modules.modules import jsonClosing

pathOfCargo = "./data/cargo.json"
pathOfResources = "./data/resources.json"
pathOfConveyance = "./data/conveyance.json"

connector = open(pathOfConveyance)
importedConveyance = json.load(connector)
connector.close()

connector = open(pathOfCargo)
importedCargo = json.load(connector)
connector.close()

connector = open(pathOfResources)
importedResources = json.load(connector)
connector.close()

for conveyance in importedConveyance["conveyance"]:# Ship_NO_1
    for item in importedResources["resources"]:# Energy Resources
        for cargo in importedResources["resources"][item]:# Coal
            toAppend = {cargo: [cargo, 0]}
            importedCargo["cargo"][conveyance].append(toAppend)
jsonClosing(importedCargo, pathOfCargo)