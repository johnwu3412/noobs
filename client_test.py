from modules.RiotClient import RiotClient
import os
rc = RiotClient("https://na1.api.riotgames.com/",os.getenv("RiotGamesKey"))
print(rc.get_summoner_by_name("lemonjoint"))