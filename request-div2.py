from random import betavariate
from urllib import request, response
import json
import requests

header = {'TRN-Api-Key': '', 
          'Accept': 'application/json',
          'Accept-Encoding': 'gzip'}
r = requests.get('https://public-api.tracker.gg/v2/division-2/standard/profile/psn/PunKxj', params=header)

if (r.status_code) == 200:
    data = json.loads(r.content)
    print(data['data']['platformInfo']['platformUserHandle'] + ' matou '+ data['data']['segments'][0]['stats']['roguesKilled']['displayValue'] + ' Rogues')
