#pip install flask
from flask import Flask, redirect, url_for
import sys
import os


sys.path.insert(0, os.getcwd()+"\..")
from modules.RiotClient import RiotClient

app = Flask(__name__)

rc = RiotClient("https://na1.api.riotgames.com/",os.getenv("RiotGamesKey"))
summonerID = rc.get_summoner_by_name("ShabobNiqqua")
@app.route("/")
def home():
    return rc.get_masteries_by_summoner(summonerID)

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run()
