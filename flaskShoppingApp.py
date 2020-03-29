from flask import Flask
app = Flask(__name__)


@app.route("/home")
def hello():
	return "<h1> Tyršova 4 shoppin app </h1>"


# Stes debug to 1. In debug mode server will update data after every change
if __name__=='__main__':
	app.run(debug=True)