import requests
import json

base_url = 'https://na1.api.riotgames.com/'
api_endpoint = 'lol/summoner/v4/summoners/by-name/'
key = 'RGAPI-16399abc-5203-46b0-a907-ec20409bba6b'

summoner_name =  input("Enter your summoner name: ")

get_summoner = base_url + api_endpoint + summoner_name + '?api_key=' + key
print(requests.get(get_summoner).text)
 