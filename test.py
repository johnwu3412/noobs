import requests
import json
import os
# variables
base_url = 'https://na1.api.riotgames.com/'
get_summoner_api_endpoint = 'lol/summoner/v4/summoners/by-name/'
get_champion_mastery_endpoint = 'lol/champion-mastery/v4/champion-masteries/by-summoner/'

key = os.getenv('RiotGamesKey')
#input for summoner name
summoner_name =  input("Enter your summoner name: ")

#constructing API url to get account id of a summoner
get_summoner = base_url + get_summoner_api_endpoint + summoner_name + '?api_key=' + key

#sending request and reformatting request -> todo: need to add error cases
summoner = json.loads(requests.get(get_summoner).text)
print(summoner)

#constructing API url to get champion mastery of a summoner
get_mastery = base_url + get_champion_mastery_endpoint + summoner["id"] + '?api_key=' + key

#sending request and reformatting request -> todo: need to add error cases
mastery = json.loads(requests.get(get_mastery).text)

#convert champion.txt to a dictionary where key is id and value is name (Ivan)
champ = {}
x = ""

with open("champions.txt", "r", encoding = "utf-8") as f:
    for line in f:
        x = line
        key,value = line.strip().split(":")
        champ[key]= value.strip()

print(mastery)
