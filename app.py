from flask import Flask, jsonify
from scraping import scrape

app = Flask(__name__)


@app.route('/')
def index():
	return jsonify(Articles=scrape())


if __name__ == "__main_":
	app.run(debug=True, host='0.0.0.0', port=5000)
