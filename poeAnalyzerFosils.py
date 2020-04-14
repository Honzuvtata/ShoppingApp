from urllib.request import urlopen
import requests
import json

# pprint for printing of python dict with indent => pprint.pprint
import pprint
import pdb


delveEnviroments = {
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
    print(type(stringRequest.text))
    return stringRequest


fosilData = requestData()
# print(fosilData.text)

for fosil in fosils["lines"]:
    pass
