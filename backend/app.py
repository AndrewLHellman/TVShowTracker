# Flask help from https://www.makeuseof.com/tag/python-javascript-communicate-json/

from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
from random import randint
from data.tmdbtest import create
import json

app = Flask(__name__)
cors = CORS(app)

#pasteShows

with open("data/pasteShowsToIds.json", "r") as show_id_file:
   show_ids = list(json.load(show_id_file).values())

@app.route("/reciever", methods=["POST"])
def postME():
    #data = request.get_json()
    data = jsonify(create(show_ids[randint(0, (len(show_ids) - 1))]))
    return data

# Creation of this was aided by Google Bard
@app.route("/images", methods=["GET"])
def image():
  image_file_name = request.args.get("image_file_name")
  with open(f"images/{image_file_name}", "rb") as image_file:
    image_data = image_file.read()

  return Response(image_data, content_type=f"image/{image_file_name.split('.')[-1]}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
