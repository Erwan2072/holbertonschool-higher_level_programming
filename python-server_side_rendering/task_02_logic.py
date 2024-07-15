from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Read items from JSON file
def load_items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    return data.get("items", [])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    items_list = load_items()
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
