from flask import Flask, render_template, redirect, url_for, render_template, request
import logging
import sys
from storage import addItem, deleteItem, increaseCountBy1, decreaseCountBy1, loadItems

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def homeGet():
    return render_template("home.html")


@app.route("/", methods=["POST"])
@app.route("/home", methods=["POST"])
def homePost():
    x = request.form["itemName"]
    app.logger.info(x)
    return render_template("home.html")


@app.route("/test", methods=["GET"])
def testGet():
    return render_template("test.html")


@app.route("/test", methods=["POST"])
def testPost():
    userName = request.form["userName"]
    finalUrl = "/test/" + userName
    return redirect(url_for("/test/<userName>"))


@app.route("/login", methods=["GET"])
def loginPass():
    return render_template("login.html")


@app.route("/")
@app.route("/login", methods=["POST"])
def login():
    user = request.form["nm"]
    with open("persistantData.txt", "w") as f:
        f.write(user)
    app.logger.info("PRINT1")
    return redirect(url_for("user", usr=user))


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/shoppingList", methods=["GET"])
def shoppingListGet():
    items = loadItems()
    return render_template("shoppingList.html", len=len(items), items=items)


@app.route("/shoppingList", methods=["POST"])
def shoppingListPost():

    item = request.form["item"]
    app.logger.info(item)
    count = request.form["count"]
    app.logger.info(count)
    addItem(item, count)
    items = loadItems()
    len = 0
    for item in items:
        len += 1
    return render_template("shoppingList.html", items=items, len=len)


@app.route("/shoppingList/edit/<itemId>", methods=["GET"])
def edit(itemId):
    items = loadItems()
    for item in items:
        if item["itemId"] == itemId:
            itemName = item["name"]
            itemCount = item["count"]
    return render_template("edit.html", itemName=itemName, itemCount=itemCount)


@app.route("/shoppingList/edit/<itemId>", methods=["POST"])
def editPut(itemId):  # TODO rename
    value = request.form["function"]
    items = loadItems()
    if value == "increase":
        increaseCountBy1(itemId)
    elif value == "decrease":
        decreaseCountBy1(itemId)
    elif value == "delete":
        deleteItem(itemId)
        return redirect("/shoppingList")
        # return shoppingListGet()

    items = loadItems()
    for item in items:
        if item["itemId"] == itemId:
            itemName = item["name"]
            itemCount = item["count"]
    return render_template("edit.html", itemName=itemName, itemCount=itemCount)


# Stes debug to 1. In debug mode server will update data after every change

# this line starts server with parameter debug=True.
if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
