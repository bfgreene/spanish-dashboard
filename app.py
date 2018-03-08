from flask import Flask, jsonify, render_template
from scraping import scrape
import json

app = Flask(__name__)


@app.route('/')
def index():
	#return jsonify(scrape())
	return render_template("index.html", articles=scrape())


if __name__ == "__main_":
	app.run(debug=True, host='0.0.0.0', port=5000)
