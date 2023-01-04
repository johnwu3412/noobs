import requests
import json

class RiotClient():
    def __init__(self, base_url, key):
        self.base_url = base_url
        self.key = key

    def get_summoner_by_name(self, name):
        response = requests.get(self.base_url + 'lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + self.key)
        if (response.status_code > 299 and response.status_code < 200):
            raise Exception("Oops: " + response)
        print(response.text)
        summoner = json.loads(response.text)
        return summoner['id']

