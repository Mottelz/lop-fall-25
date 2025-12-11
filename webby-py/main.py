from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
	name = request.args.get("name", "Flask")
	return f"Hello {escape(name)}"