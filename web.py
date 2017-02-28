from flask import Flask, render_template, request
app = Flask(__name__)
import os
import weather
from randombar import search_food

@app.route("/")
def index():
	address = request.values.get('address')
	term = request.values.get('term')
	bar = None
	forecast = None
	if address:
		bar = search_food(address)
	return render_template('index.html', bar=bar)
	# return render_template('index.html', forecast=forecast)
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/layout')
def layout():
	return render_template('layout.html')


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
