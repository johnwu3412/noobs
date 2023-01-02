import requests
import json

url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Jack%20J'
key = 'RGAPI-16399abc-5203-46b0-a907-ec20409bba6b'

get_summoner = url + '?api_key=' + key
print(get_summoner)
print(requests.get(get_summoner).text)
