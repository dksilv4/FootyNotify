import requests
import json

userTeam = "Deportivo Capiata" ##type in team that are playing live

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/"+userTeam

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "c50156e257msh58be36df0d85bfep10de4cjsn14479e1c8f49"
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)

fatList = data['api']['teams']

teamName = fatList[0]["name"]
teamID = fatList[0]["team_id"]

print(teamID)
print(teamName)

url2 = "https://api-football-v1.p.rapidapi.com/v2/fixtures/live/"

##Uses london timezone
querystring = {"timezone":"Europe/London"}

##requests Live fixtures
response2 = requests.request("GET", url2, headers=headers, params=querystring)

##Saves response in JSON format
liveGameData = json.loads(response2.text)
liveGameList = liveGameData['api']['fixtures']
print(liveGameList) ##prints list of current live games around the world (amazing how many games of professional football there is)

##length of list to run for loop counter
listLength =len(liveGameList)
for x in range(listLength-1): ##takes list element, uses dict in a dict to grab team ID comparison
    y = liveGameList[x]
    if ((y['homeTeam']['team_id'] == teamID) or (y['awayTeam']['team_id'] == teamID)):
        ##formats score
        print((y['homeTeam']['team_name'])+" "+str(y['goalsHomeTeam'])+"-"+str(y['goalsAwayTeam'])+" "+(y['awayTeam']['team_name']))








