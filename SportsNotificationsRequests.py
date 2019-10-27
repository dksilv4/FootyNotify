import requests
import json
from datetime import datetime
import os

# Requests that use the API to search for various things including the Team details/name/id/ fixtures
token = '82f50635a5msh6505487684c7ecfp16c7bbjsn5008a39862cb'
token2 = os.environ.get('AUTH_RAPIDAPI')
headers = {'x-rapidapi-host': "api-football-v1.p.rapidapi.com", 'x-rapidapi-key': token}


def search(team_name):
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)  # the data from all matching football teams

    fatList = data['api']['teams']
    result = (fatList[0]["name"])
    print(fatList[0])
    return fatList[0]['team_id'], fatList[0]['name']


def get_live_game(teamID):
    querystring = {"timezone": "Europe/London"}

    # requests Live fixtures
    response = requests.request("GET", "https://api-football-v1.p.rapidapi.com/v2/fixtures/live/", headers=headers,
                                params=querystring)
    # Saves response in JSON format
    live_game_data = json.loads(response.text)
    live_game_list = live_game_data['api']['fixtures']

    listLength = len(live_game_list)

    for x in range(listLength - 1):  ##takes list element, uses dict in a dict to grab team ID comparison
        y = live_game_list[x]
        if ((y['homeTeam']['team_id'] == teamID) | (y['awayTeam']['team_id'] == teamID)):
            ##formats score
            return (y['homeTeam']['team_name']) + " " + str(y['goalsHomeTeam']) + "-" + str(
                y['goalsAwayTeam']) + " " + (y['awayTeam']['team_name'])
    return None



def get_last_five(teamID):
    ##url for fixtures, arg is teamID
    querystring = {"timezone": "Europe/London"}
    ##request
    response = requests.request("GET", "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/" + str(teamID),
                                headers=headers, params=querystring)

    ##loads to json format
    fixtureData = json.loads(response.text)
    fixtures = fixtureData['api']['fixtures']

    # vars, loop to append values into list
    fixture_list = ["Here are the last five games:"]
    for n in range(0, 5):
        home_team_name = fixtures[n]['homeTeam']['team_name']
        home_team_score = fixtures[n]['goalsHomeTeam']
        away_team_score = fixtures[n]['goalsAwayTeam']
        away_team_name = fixtures[n]['awayTeam']['team_name']
        fixture = '{} {} - {} {}'.format(home_team_name, home_team_score, away_team_score, away_team_name)
        fixture_list.append(fixture)

    return fixture_list


'''-------------------------------------------------------'''


##Next fixture
def get_next_fixture(teamID):
    global nextFixture
    querystring = {"timezone": "Europe/London"}
    ##url for fixtures, arg is teamID
    url3 = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/" + str(teamID)

    ##request
    response3 = requests.request("GET", url3, headers=headers, params=querystring)

    ##loads to json format
    fixtureData = json.loads(response3.text)
    fixtures = fixtureData['api']['fixtures']
    fixtureList = []
    fixturesLength = len(fixtures)
    for n in range(fixturesLength):

        ##checks for game with ext game greater than current date and previous game less than current date, prints fixture
        if ((fixtures[fixturesLength - 1 - n]['event_date'])[0:10] > datetime.today().strftime('%Y-%m-%d')) and (
                (fixtures[fixturesLength - 2 - n]['event_date'])[0:10] < datetime.today().strftime('%Y-%m-%d')):
            nextFixture = fixtures[fixturesLength - 1 - n]['homeTeam']['team_name'] + " VS " \
                          + fixtures[fixturesLength - 1 - n]['awayTeam'][
                              'team_name']
            break

    return nextFixture


'''-------------------------------------------------------'''


##Standings function
def get_standings(teamID):
    url4 = "https://api-football-v1.p.rapidapi.com/v2/leagues/team/" + str(teamID)  ##arg is teamID
    querystring = {"timezone": "Europe/London"}
    response4 = requests.request("GET", url4, headers=headers, params=querystring)  ##request

    ##Grabs leagueID based off teamID
    leaguesData = json.loads(response4.text)
    leaguesList = leaguesData['api']['leagues']
    leagueID = leaguesList[0]['league_id']

    print(leagueID)

    ##Request for standings based off leagueID
    url5 = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/" + str(leagueID)
    querystring = {"timezone": "Europe/London"}
    response5 = requests.request("GET", url5, headers=headers, params=querystring)  ##request

    standingsData = json.loads(response5.text)
    standingsList = standingsData['api']['standings'][0]
    standingsLength = len(standingsList)

    leagueTable = []  ##Define league table and append rank, name and points to an entry
    for y in range(standingsLength):
        tableEntry = str(standingsList[y]['rank']) + ". " + standingsList[y]['teamName'] + " - Pts: " + str(
            standingsList[y]['points'])
        leagueTable.append(tableEntry)
        format1 = str(leagueTable).replace("[", "")  # this formats the standings so it can be texted to user
        format2 = format1.replace("]", "")
        format3 = format2.replace(",", "\n")
        finalformatting = format3.replace("'", "")
    return finalformatting


'''-------------------------------------------------------'''


def search_new(team_name):
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)  # the data from all matching football team

    fatList = data['api']['teams']
    result = (fatList[0]["name"])
    print(fatList[0])
    return fatList[0]['team_id'], fatList[0]['name']


'''-------------------------------------------------------'''


def get_live_game_new(teamID):
    querystring = {"timezone": "Europe/London"}

    # requests Live fixtures
    response = requests.request("GET", "https://api-football-v1.p.rapidapi.com/v2/fixtures/live/", headers=headers,
                                params=querystring)
    # Saves response in JSON format
    live_game_data = json.loads(response.text)
    live_game_list = live_game_data['api']['fixtures']

    for x in range(0, len(live_game_list)):  # takes list element, uses dict in a dict to grab team ID comparison
        y = live_game_list[x]
        home_team_id = y['homeTeam']['team_id']
        away_team_id = y['awayTeam']['team_id']
        if home_team_id == teamID or away_team_id == teamID:
            # formats score output
            home_team_name = y['homeTeam']['team_name']
            home_team_score = y['goalsHomeTeam']
            away_team_name = y['goalsAwayTeam']
            away_team_score = y['awayTeam']['team_name']
            return '{} {} - {} {}'.format(home_team_name, home_team_score, away_team_score, away_team_name)
        else:
            return None


'''-------------------------------------------------------'''


def get_last_five_new(teamID):
    querystring = {"timezone": "Europe/London"}
    ##url for fixtures, arg is teamID
    url3 = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/" + str(teamID)

    ##request
    response3 = requests.request("GET", url3, headers=headers, params=querystring)

    ##loads to json format
    fixtureData = json.loads(response3.text)
    fixtures = fixtureData['api']['fixtures']

    ##vars, loop to append values into list, compare recent dates
    n = 0
    fixtureList = []
    fixturesLength = len(fixtures)

    for n in range(fixturesLength):
        ##if list size == 5 break
        if len(fixtureList) > 4:
            break

        ##compares date to pull previous match scores
        elif ((fixtures[fixturesLength - 1 - n]['event_date'])[0:10] < datetime.today().strftime('%Y-%m-%d')):
            lastFixture = fixtures[fixturesLength - 1 - n]['homeTeam']['team_name'] + " " + str(
                fixtures[fixturesLength - 1 - n]['goalsHomeTeam']) + "-" + str(
                fixtures[fixturesLength - 1 - n]['goalsAwayTeam']) + " " + fixtures[fixturesLength - 1 - n]['awayTeam'][
                              'team_name']
            fixtureList.append(lastFixture)
        else:
            continue

    ##Last 5 match results
    print(fixtureList)
    return fixtureList
