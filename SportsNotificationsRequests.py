import requests
import json

userteam = "real_m"

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/"+userteam

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "af10c3e836mshb4fb54db83a539fp154ebajsn4fdd167bfc6c"
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)

fatList = data['api']['teams']
print(fatList)


##print data['teams']
