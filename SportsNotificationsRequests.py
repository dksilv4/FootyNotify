from datetime import datetime
import requests
import json

userTeam = "Nottingham Forest" ##type in team that are playing live

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/"+userTeam

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "82f50635a5msh6505487684c7ecfp16c7bbjsn5008a39862cb"
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

##vars, loop to append values into list, compare recent dates
n=0
fixtureList = []
fixturesLength = len(fixtures)

for n in range(fixturesLength):
    ##if list size == 5 break
    if len(fixtureList) > 4:
        break

    ##compares date to pull previous match scores
    elif ((fixtures[fixturesLength-1-n]['event_date'])[0:10] < datetime.today().strftime('%Y-%m-%d')):
        lastFixture = fixtures[fixturesLength - 1 - n]['homeTeam']['team_name'] + " " + str(
            fixtures[fixturesLength - 1 - n]['goalsHomeTeam']) + "-" + str(
            fixtures[fixturesLength - 1 - n]['goalsAwayTeam']) + " " + fixtures[fixturesLength - 1 - n]['awayTeam'][
                          'team_name']
        fixtureList.append(lastFixture)
    else:
        continue

##Last 5 match results

print(fixtureList)

##Next fixture

for n in range(fixturesLength):

    ##checks for game with ext game greater than current date and previous game less than current date, prints fixture
    if ((fixtures[fixturesLength - 1 - n]['event_date'])[0:10] > datetime.today().strftime('%Y-%m-%d')) and ((fixtures[fixturesLength - 2 - n]['event_date'])[0:10] < datetime.today().strftime('%Y-%m-%d')):
        nextFixture = fixtures[fixturesLength - 1 - n]['homeTeam']['team_name'] + " VS " \
                      + fixtures[fixturesLength - 1 - n]['awayTeam'][
                          'team_name']
        break

print(nextFixture)

##Standings function

url4 = "https://api-football-v1.p.rapidapi.com/v2/leagues/team/"+str(teamID) ##arg is teamID

response4 = requests.request("GET", url4, headers=headers, params=querystring) ##request

##Grabs leagueID based off teamID
leaguesData = json.loads(response4.text)
leaguesList = leaguesData['api']['leagues']
leagueID = leaguesList[0]['league_id']

print(leagueID)

##Request for standings based off leagueID
url5 = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/"+str(leagueID)

response5 = requests.request("GET", url5, headers=headers, params=querystring) ##request

standingsData = json.loads(response5.text)
standingsList = standingsData['api']['standings'][0]
standingsLength = len(standingsList)

leagueTable = [] ##Define league table and append rank, name and points to an entry
for y in range(standingsLength):
    tableEntry = str(standingsList[y]['rank']) + ". " + standingsList[y]['teamName'] + ", Pts: " + str(standingsList[y]['points'])
    leagueTable.append(tableEntry)
print(leagueTable)

##pog
































