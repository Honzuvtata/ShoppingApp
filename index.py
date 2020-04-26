from flask import Flask, render_template, redirect, url_for, render_template, request
import sys
from storage import addItem, deleteItem, increaseCountBy1, decreaseCountBy1, loadItems
from poeAnalyzerFosils import analyzeFossils


app = Flask(__name__)
# Bootstrap(app)


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def homeGet():
    return render_template("home.html")


@app.route("/", methods=["POST"])
@app.route("/home", methods=["POST"])
def homePost():
    x = request.form["itemName"]
    return render_template("home.html")


@app.route("/test", methods=["GET"])
def testGet():
    return render_template("test.html")


@app.route("/test", methods=["POST"])
def testPost():
    userName = request.form["userName"]
    finalUrl = "/test/" + userName
    return redirect(url_for("/test/<userName>"))


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/shoppingList", methods=["GET"])
def shoppingListGet():
    items = loadItems()
    return render_template("shoppingList.html", len=len(items), items=items)


@app.route("/shoppingList", methods=["POST"])
def shoppingListPost():
    # TODO: Fix: submit button sended without values crashes
    try:
        itemName = request.form["item"]
        itemCount = int(request.form["count"])
        addItem(itemName, itemCount)
    except:
        print("ERROR: User submitted empty field")
    len = 0
    items = loadItems()
    for item in items:
        len += 1
    return render_template("shoppingList.html", items=items, len=len)


@app.route("/shoppingList/edit/<itemId>", methods=["GET"])
def edit(itemId):
    # show item with sended itemId
    items = loadItems()
    for item in items:
        if item["itemId"] == itemId:
            itemName = item["name"]
            itemCount = item["count"]
    return render_template("edit.html", itemName=itemName, itemCount=itemCount)


@app.route("/shoppingList/edit/<itemId>", methods=["POST"])
def editPut(itemId):  # TODO rename
    # Find what button user used
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
    # Shou item with sended itemId
    for item in items:
        if item["itemId"] == itemId:
            itemName = item["name"]
            itemCount = item["count"]
    return render_template("edit.html", itemName=itemName, itemCount=itemCount)


@app.route("/fossils", methods=["GET"])
def fossilsGetList():  # TODO rename
    # Shou item with sended itemId
    fossilsPrice = analyzeFossils()
    return render_template(
        "fossils.html", fossilsPrice=fossilsPrice, len=len(fossilsPrice)
    )
    pass


@app.route("/cv", methods=["GET"])
def CV():
    return render_template("cv.html")


@app.route("/test", methods=["GET"])
def test():
    return render_template("test.html")


@app.route("/playground", methods=["GET"])
def playground():
    users = [
        {"name": "Honza", "email": "honza@email.com"},
        {"name": "Kuba", "email": "kuba@email.com"},
        {"name": "Luke", "email": "luke@email.com"},
    ]
    player1 = {"name": "Honza", "level": 1, "HP": 10, "weapon": "trainingSword"}
    x = [1, 2, 3, 4, 5]
    y = 1
    z = 2
    return render_template(
        "playground.html",
        x=x,
        y=y,
        z=z,
        users=users,
        lenOfUsers=len(users),
        player1=player1,
    )


# Stes debug to 1. In debug mode server will update data after every change

# this line starts server with parameter debug=True.
if __name__ == "__main__":
    app.run(debug=True)  # (debug=True)
    app.run(host="0.0.0.0")  # (debug=True)
