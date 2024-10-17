from flask import Flask, jsonify
import random
import requests

app = Flask(__name__)

# URL для Google Sheets или Pastebin
SHEET_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT2X9puaSsG7NvDdRd16CdNL3YPjbsVPr8qO1LJximNbRNnGeVc1G_SIDmnBcQXkfN2nmpsNBqhh2rj/pub?output=csv'
PASTEBIN_URL = 'https://pastebin.com/raw/xxxxxxxx'  # замените на ваш URL

def get_quotes():
    # Извлечение цитат из Google Sheets
    response = requests.get(SHEET_URL)
    quotes = response.text.splitlines()
    return [quote.strip() for quote in quotes]

@app.route('/quote', methods=['GET'])
def quote():
    quotes = get_quotes()
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
