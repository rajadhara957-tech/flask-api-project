from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load data from JSON file
with open("data.json") as f:
    internships = json.load(f)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask API!"})

@app.route('/internships', methods=['GET'])
def get_internships():
    return jsonify(internships)

@app.route('/internships/<string:location>', methods=['GET'])
def get_internships_by_location(location):
    result = [i for i in internships if i["location"].lower() == location.lower()]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
