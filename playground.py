from flask import Flask

app = Flask(__name__)
# Bootstrap(app)


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def homeGet():
    return "Hello world"


if __name__ == "__main__":
    app.run()
