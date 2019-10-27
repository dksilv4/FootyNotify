import requests
import json

'''Requests that use the API to search for various things including the Team details/name/id/ fixtures'''
token = '3e912ca4e7msh3e11bf13a48a111p1e25fdjsnf736c67d588a'
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

def get_last_five(teamID):
    ##url for fixtures, arg is teamID
    querystring = {"timezone": "Europe/London"}
    ##request
    response = requests.request("GET", "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/" + str(teamID), headers=headers, params=querystring)

    ##loads to json format
    fixtureData = json.loads(response.text)
    fixtures = fixtureData['api']['fixtures']

    ##vars, loop to append values into list
    n = 0
    fixtureList = []
    for n in range(5):
        lastFixture = fixtures[n]['homeTeam']['team_name'] + " " + str(fixtures[n]['goalsHomeTeam']) + "-" + str(
            fixtures[n]['goalsAwayTeam']) + " " + fixtures[n]['awayTeam']['team_name']
        fixtureList.append(lastFixture)

    return fixtureList
