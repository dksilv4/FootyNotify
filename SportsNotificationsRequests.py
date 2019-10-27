import requests
import json

userTeam = "Deportivo Capiata" ##type in team that are playing live

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/"+userTeam

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "3e912ca4e7msh3e11bf13a48a111p1e25fdjsnf736c67d588a"
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)

fatList = data['api']['teams']

teamName = fatList[0]["name"]
teamID = fatList[0]["team_id"]

url2 = "https://api-football-v1.p.rapidapi.com/v2/fixtures/live/"

##Uses london timezone
querystring = {"timezone":"Europe/London"}

##requests Live fixtures
response2 = requests.request("GET", url2, headers=headers, params=querystring)

##Saves response in JSON format
liveGameData = json.loads(response2.text)
liveGameList = liveGameData['api']['fixtures']

##length of list to run for loop counter
listLength =len(liveGameList)
for x in range(listLength-1): ##takes list element, uses dict in a dict to grab team ID comparison
    y = liveGameList[x]
    if ((y['homeTeam']['team_id'] == teamID) or (y['awayTeam']['team_id'] == teamID)):
        ##formats score
        print((y['homeTeam']['team_name'])+" "+str(y['goalsHomeTeam'])+"-"+str(y['goalsAwayTeam'])+" "+(y['awayTeam']['team_name']))

###############getting the 5 most recent results##############

##url for fixtures, arg is teamID
url3 = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/"+str(teamID)

##request
response3 = requests.request("GET", url3, headers=headers, params=querystring)

##loads to json format
fixtureData = json.loads(response3.text)
fixtures = fixtureData['api']['fixtures']

##vars, loop to append values into list
n=0
fixtureList = []
for n in range(5):
    lastFixture = fixtures[n]['homeTeam']['team_name']+" "+str(fixtures[n]['goalsHomeTeam'])+"-"+str(fixtures[n]['goalsAwayTeam'])+" "+fixtures[n]['awayTeam']['team_name']
    fixtureList.append(lastFixture)

print(fixtureList)















