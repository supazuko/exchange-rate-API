import requests
import os
from flask import Flask, jsonify, request, abort
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


@app.route('/')
def index():
    return 'Welcome to Exchange Rate'


@app.route('/exchange-rate/', methods=['POST'])
def convert():
    data = request.get_json()
    currency_1 = data["currency1"]
    currency_2 = data["currency2"]

    # send the request to the external api to convert currencies using the variables as arguments
    r = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency_2}")
    if r.status_code == 200:
        rate = r.json()["conversion_rates"][currency_1]
    else:
        return abort(400, "Invalid Currency")

    # return response with rate in json

    return jsonify({
        "rate": rate
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
