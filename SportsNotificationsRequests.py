import requests
import json
'''Requests that use the API to search for various things including the Team details/name/id/ fixtures'''

def search_for_name(team_name):
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "c50156e257msh58be36df0d85bfep10de4cjsn14479e1c8f49"
    }  # must hide

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text) #the data from all matching football teams

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

    data = json.loads(response.text) #the data from all matching football teams

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

    data = json.loads(response.text) #the data from all matching football teams

    fatList = data['api']['teams']
    return fatList[0]


def search_to_file(team_name):
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "c50156e257msh58be36df0d85bfep10de4cjsn14479e1c8f49"
    }  # must hide

    response = requests.request("GET", url, headers=headers) #the data from all matching football teams

    data = json.loads(response.text)

    fatList = data['api']['teams']
    filewrite = open('testAPI.txt', 'a+').write(str(fatList[0]))

