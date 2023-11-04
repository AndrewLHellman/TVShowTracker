# Flask help from https://www.makeuseof.com/tag/python-javascript-communicate-json/

from flask import Flask, request, jsonify
from flask_cors import CORS
from random import randint

app = Flask(__name__)
cors = CORS(app)

@app.route("/reciever", methods=["POST"])
def postME():
    data = request.get_json()
    data = jsonify(data[randint(0, (len(data)) - 1)])
    return data

if __name__ == "__main__":
    app.run(debug=True)