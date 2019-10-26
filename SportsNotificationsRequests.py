import requests
import json


def search_for_name(team_name):
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "c50156e257msh58be36df0d85bfep10de4cjsn14479e1c8f49"
    }  # must hide

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    fatList = data['api']['teams']
    result = (fatList[0]["name"])
    print(fatList[0])
    return result


def search_for_team_id(team_name):
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "c50156e257msh58be36df0d85bfep10de4cjsn14479e1c8f49"
    }  # must hide

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    fatList = data['api']['teams']
    result = (fatList[0]["team_id"])
    return result


def search_for_team_details(team_name):
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "c50156e257msh58be36df0d85bfep10de4cjsn14479e1c8f49"
    }  # must hide

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    fatList = data['api']['teams']
    return fatList[0]


def search_to_file(team_name):
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "c50156e257msh58be36df0d85bfep10de4cjsn14479e1c8f49"
    }  # must hide

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    fatList = data['api']['teams']
    filewrite = open('testAPI.txt', 'a+').write(str(fatList[0]))


def get_live_game(teamID):
    querystring = {"timezone": "Europe/London"}
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "c50156e257msh58be36df0d85bfep10de4cjsn14479e1c8f49"
    }  # must hide
    ##requests Live fixtures
    response2 = requests.request("GET", "https://api-football-v1.p.rapidapi.com/v2/fixtures/live/", headers=headers,
                                 params=querystring)

    ##Saves response in JSON format
    liveGameData = json.loads(response2.text)
    liveGameList = liveGameData['api']['fixtures']
    print(
        liveGameList)  # prints list of current live games around the world (amazing how many games of professional football there is)

    ##length of list to run for loop counter
    listLength = len(liveGameList)
    for x in range(listLength - 1):  ##takes list element, uses dict in a dict to grab team ID comparison
        y = liveGameList[x]
        if ((y['homeTeam']['team_id'] == teamID) or (y['awayTeam']['team_id'] == teamID)):
            ##formats score
            home_team_name = y['homeTeam']['team_name']
            home_team_score = y['goalsHomeTeam']
            away_team_name = y['goalsAwayTeam']
            away_team_score = y['awayTeam']['team_name']
            return '{} {} - {} {}'.format(home_team_name, home_team_score, away_team_score, away_team_name)
