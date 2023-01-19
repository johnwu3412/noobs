#pip install flask

from flask import Flask, redirect, url_for

import sys

sys.path.insert(0, r'C:\Users\Kenny\Documents\Project 2022\noobs')

#from RiotClient import get_masteries_by_summoner, get_summoner_by_name

from modules.RiotClient import RiotClient

import os

app = Flask(__name__)



rc = RiotClient("https://na1.api.riotgames.com/",os.getenv("RiotGamesKey"))

@app.route("/")
def home():
    return test()

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run()
