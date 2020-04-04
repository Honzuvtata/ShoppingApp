import json


'''
items = [
    {"name": "apple", "count": 1},
    {"name": "banana", "count": 2},
    ]

'''

def addItem(itemName, itemCount):
    items = loadItems()
    items.append({"name": itemName, "count": int(itemCount)})
    writeItems(items)

def increaseCountBy1(itemName):
    items = loadItems()
    for item in items:
        if item["name"] == itemName:
            item["count"] += 1
    writeItems(items)

def decreaseCountBy1(itemName):
    items = loadItems()
    for item in items:
        if item["name"] == itemName:
            item["count"] -= 1
    writeItems(items)


def deleteItem(itemName):
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


'''
addItem("apple", 3)
increaseCountBy1("apple")
decreaseCountBy1("apple")
deleteItem("apple")
'''