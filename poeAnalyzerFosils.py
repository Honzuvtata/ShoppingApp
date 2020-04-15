from urllib.request import urlopen
import requests
import json

# pprint for printing of python dict with indent => pprint.pprint
import pprint
import pdb


delveEnvironments = {
    "Mines": [
        "Metallic Fossil",
        "Serrated Fossil",
        "Pristine Fossil",
        "Aetheric Fossil",
    ],
    "Fungal Caverns": [
        "Dense Fossil",
        "Aberrant Fossil",
        "Perfect Fossil",
        "Corroded Fossil",
        "Gilded Fossil",
    ],
    "Petrified Forest": [
        "Bound Fossil",
        "Jagged Fossil",
        "Corroded Fossil",
        "Sanctified Fossil",
    ],
    "Abyssal Depths": [
        "Aberrant Fossil",
        "Bound Fossil",
        "Gilded Fossil",
        "Lucent Fossil",
    ],
    "Frozen Hollow": [
        "Frigid Fossil",
        "Serrated Fossil",
        "Prismatic Fossil",
        "Sanctified Fossil",
    ],
    "Magma Fissure": [
        "Scorched Fossil",
        "Prismatic Fossil",
        "Pristine Fossil",
        "Enchanted Fossil",
        "Encrusted Fossil",
        "Faceted Fossil",
    ],
    "Sulfur Vents": [
        "Metallic Fossil",
        "Perfect Fossil",
        "Aetheric Fossil",
        "Encrusted Fossil",
    ],
}


def requestData():
    # send request to get complete data from poe (all stash tabs from all players)
    stringRequest = requests.get(
        "https://poe.ninja/api/data/itemoverview?league=Delirium&type=Fossil&language=en"
    )
    print("Response from POE server: ", stringRequest)
    print("Type of data from server: ", type(stringRequest.text))
    pythonObject = json.loads(stringRequest.text)
    print(type(pythonObject))
    return pythonObject


def getValueOfFossil(fossilName,):
    for fossil in fossilData["lines"]:
        if fossilName == fossil["name"]:
            chaosValue = fossil["chaosValue"]
            return chaosValue


def matchEnviromentsNamesValues():
    results = {}
    for environmentName, environmentValues in delveEnvironments.items():
        fossilsNamesValues = []
        # print(environmentName, environmentValues)
        for fossil in environmentValues:
            fossilValue = getValueOfFossil(fossil)
            fossilsNamesValues.append({"name": fossil, "chaosValue": fossilValue})
        results[environmentName] = fossilsNamesValues
        fossilsNamesValues = []
    return results


def findAverageProfitPerEnvironment(fossilsEnvironmentNamesAndValues):
    # Takes dict with arrays and fossils. Return environment: average chaos profit
    x = type(fossilsEnvironmentNamesAndValues)
    results = []
    for environment, fossilsInEnvironment in fossilsEnvironmentNamesAndValues.items():
        totalProfit = 0
        averageProfitPerFossil = 0
        for fossil in fossilsInEnvironment:
            totalProfit += fossil["chaosValue"]
        averageProfitPerFossil = totalProfit / len(fossilsInEnvironment)
        averageProfitInEnvironment = {
            "name": environment,
            "averageChaosProfit": averageProfitPerFossil,
        }
        results.append(averageProfitInEnvironment)
    return results


fossilData = requestData()
fossilsNamesAndValues = matchEnviromentsNamesValues()
pprint.pprint(fossilsNamesAndValues)
x = findAverageProfitPerEnvironment(fossilsNamesAndValues)
print(x)
