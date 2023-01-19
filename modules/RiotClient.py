import requests
import json

class RiotClient():
    def __init__(self, base_url, key):
        self.base_url = base_url
        self.key = key
        self.champ = {}
        
        with open("champions.txt", "r", encoding = "utf-8") as f:
            for line in f:
                key,value = line.strip().split(":")
                self.champ[key]= value.strip()


    def get_summoner_by_name(self, name):
        response = requests.get(self.base_url + 'lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + self.key)
        if (response.status_code > 299 and response.status_code < 200):
            raise Exception("Oops: " + response)
        summoner = json.loads(response.text)
        return summoner['id']

    def get_masteries_by_summoner(self, summonerid):
        get_champion_mastery_endpoint = 'lol/champion-mastery/v4/champion-masteries/by-summoner/'
        get_mastery = self.base_url + get_champion_mastery_endpoint + summonerid + '?api_key=' + self.key

        #sending request and reformatting request -> todo: need to add error cases
        mastery = json.loads(requests.get(get_mastery).text)

        return(mastery)
    
    def champ_id_to_name(self, champ_id):
        return(self.champ[champ_id])        
        