# Flask help from https://www.makeuseof.com/tag/python-javascript-communicate-json/

from flask import Flask, request, jsonify
from flask_cors import CORS
from random import randint

app = Flask(__name__)
cors = CORS(app)

arrestedDevelopment = {
  "image": "images/ArrestedDevelopment.jpg",
  "description": "Arrested Development is an American television sitcom created by Mitchell Hurwitz. It aired on Fox for three seasons from November 2, 2003, to February 10, 2006, followed by two seasons on Netflix, season four being released in 2013 and season five being released in 2018 and 2019.",
  "genre": "Comedy",
  "recommenders": ["Tessa", "Andrew", "LeeAnn", "Jenaya", "Jeffrey"]
}

kimsConvenience = {
    "image": "images/KimsConvenience.jpg",
    "description": "Kim's Convenience (Korean: 김씨네 편의점; Hanja: 金氏네 便宜店; RR: Gimssine Pyeonuijeon) is a Canadian television sitcom that aired on CBC Television from October 2016 to April 2021. It depicts the Korean Canadian Kim family that runs a convenience store in the Moss Park neighbourhood of Toronto: parents \"Appa\" (Paul Sun-Hyung Lee) and \"Umma\" (Jean Yoon) – Korean for dad and mom, respectively – along with their daughter Janet (Andrea Bang) and estranged son Jung (Simu Liu). Other characters include Jung's friend and coworker Kimchee (Andrew Phung), his manager Shannon (Nicole Power) and Janet's friend Gerald Tremblay (Ben Beauchemin). The series is based on Ins Choi's 2011 play of the same name.",
    "genre": "Comedy",
    "recommenders": ["Andrew"]
}

showlist = [arrestedDevelopment, kimsConvenience];

@app.route("/reciever", methods=["POST"])
def postME():
    #data = request.get_json()
    data = jsonify(showlist[randint(0, (len(showlist)) - 1)])
    return data

if __name__ == "__main__":
    app.run(debug=True)