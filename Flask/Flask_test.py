#pip install flask

#           ***Imports***
from flask import Flask, redirect, url_for, request
from flask_restful import Api, Resource, reqparse
import json
# Api Class-> makes the flask app a Restful API

import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'modules'))
from RiotClient import RiotClient

#           ***Initializing***
app = Flask(__name__)
api = Api(app)

rc = RiotClient("https://na1.api.riotgames.com/",os.getenv("RiotGamesKey"))
#summonerID = rc.get_summoner_by_name("ShabobNiqqua")

requests = [""]
insults = {}

class InsultsList(Resource):
    def get(self):
        return json.dumps(insults), 200
    def post(self):
        data = request.get_json()
        insults[data["name"]]= data["value"]
        return 200


#           ***Processing***
@app.route("/")
def home():
    return rc.get_masteries_by_summoner(summonerID)

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

api.add_resource(InsultsList, '/insultme')

#
if __name__ == "__main__":
    app.run(debug=True)

