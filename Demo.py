import requests
import json
#url = "https://www.albion-online-data.com/"

print(json.loads(requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T4_BAG,T5_BAG.json?locations=Caerleon,Bridgewatch&qualities=2%22").text))