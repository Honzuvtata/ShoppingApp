import json
import random
import string

"""
items = [
    {"id": "id-WAPWXFSXVO", "name": "apple", "count": 1},
    {"id": "id-RLS2HWA52E", "name": "banana", "count": 2},
    ]

"""


def generateId(size=10, chars=string.ascii_uppercase + string.digits):
    # stack overflow link: https://stackoverflow.com/a/2257449/13186181
    randomId = "".join(random.choice(chars) for _ in range(size))
    return "id-" + randomId


def addItem(itemName, itemCount):
    itemId = generateId()
    items = loadItems()
    items.append({"id": itemId, "name": itemName, "count": int(itemCount)})
    writeItems(items)


def increaseCountBy1(itemName):
    # TODO: instead of name use ID
    items = loadItems()
    for item in items:
        if item["name"] == itemName:
            item["count"] += 1
    writeItems(items)


def decreaseCountBy1(itemName):
    # TODO: instead of name use ID
    items = loadItems()
    for item in items:
        if item["name"] == itemName:
            item["count"] -= 1
    writeItems(items)


def deleteItem(itemName):
    # TODO: instead of name use ID
    items = loadItems()
    for item in items:
        if item["name"] == itemName:
            items.remove(item)
    writeItems(items)


def writeItems(items):
    with open("persistantData.json", "w") as persistantItems:
        json.dump(items, persistantItems, indent=4)
        print(items)


def loadItems():
    with open("persistantData.json", "r") as persistantItems:
        data = json.load(persistantItems)
        return data
