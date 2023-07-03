import json

pathOfJson = "C:/python_workspace/journeyers/data/harbors.json"

connector = open(pathOfJson, encoding="utf-8")
Json = json.load(connector)
connector.close()

for harbor in Json["alls"]:
    for destination in Json["alls"]:
        if(harbor == destination):
            lenght = 0
            harbor1 = [destination, lenght]
            Json["alls"][harbor].append(harbor1)
            connector = open(pathOfJson, "w", encoding="utf-8")
            json.dump(Json, connector)
            connector.close()
        else:
            lenght = input("Podaj długość trasy z punktu " + harbor + " do " + destination + ": ")
            harbor1 = [destination, lenght]
            Json["alls"][harbor].append(harbor1)
            connector = open(pathOfJson, "w", encoding="utf-8")
            json.dump(Json, connector)
            connector.close()