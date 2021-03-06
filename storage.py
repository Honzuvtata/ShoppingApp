import json
import random
import string

"""
items = [
    {"itemId": "id-WAPWXFSXVO", "name": "apple", "count": 1},
    {"itemId": "id-RLS2HWA52E", "name": "banana", "count": 2},
    ]

print(items[0]["itemId])
"""


def generateId(size=10, chars=string.ascii_uppercase + string.digits):
    # stack overflow link: https://stackoverflow.com/a/2257449/13186181
    randomId = "".join(random.choice(chars) for _ in range(size))
    return "itemId-" + randomId


def addItem(itemName, itemCount):
    duplicitId = checkDuplicity(itemName)
    if duplicitId:
        increaseCountBy1(duplicitId, itemCount)
    else:
        writeItemToList(itemName, itemCount)


def writeItemToList(itemName, itemCount):
    itemId = generateId()
    items = loadItems()
    items.append({"itemId": itemId, "name": itemName, "count": int(itemCount)})
    writeItems(items)


def increaseCountBy1(itemId, count=1):
    items = loadItems()
    for item in items:
        print(type(item))
        print(item["itemId"], "LOG!!!!!!!!!!!!")
        if item["itemId"] == itemId:
            #item["count"] += 1
            item["count"] = item["count"] + count
    writeItems(items)


def decreaseCountBy1(itemId):
    # TODO: instead of name use ID
    items = loadItems()
    for item in items:
        if item["itemId"] == itemId:
            item["count"] -= 1
    writeItems(items)


def deleteItem(itemId):
    # TODO: instead of name use ID
    items = loadItems()
    for item in items:
        if item["itemId"] == itemId:
            items.remove(item)
    writeItems(items)


def writeItems(items):
    with open("data\persistantData.json", "w") as persistantItems:
        json.dump(items, persistantItems, indent=4)
        print(items)


def loadItems(databasePath="data\persistantData.json"):
    with open(databasePath, "r") as persistantItems:
        data = json.load(persistantItems)
        return data


def checkDuplicity(itemName):
    items = loadItems()
    for item in items:
        if item["name"] == itemName:
            itemId = item["itemId"]
            return itemId
    return None
