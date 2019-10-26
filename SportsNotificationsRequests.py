import requests
import json


def search_for_name(team_name):

    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "af10c3e836mshb4fb54db83a539fp154ebajsn4fdd167bfc6c"
    }  # must hide

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)


    fatList = data['api']['teams']
    result = (fatList[0]["name"])

    ##print data['teams']
    print result
    return result


def search_for_team_id(team_name):

    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "af10c3e836mshb4fb54db83a539fp154ebajsn4fdd167bfc6c"
    }  # must hide

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    fatList = data['api']['teams']
    result = (fatList[0]["team_id"])

    ##print data['teams']
    print result
    return result

def search_for_team_details(team_name):

    url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/" + team_name

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "af10c3e836mshb4fb54db83a539fp154ebajsn4fdd167bfc6c"
    }  # must hide

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    fatList = data['api']['teams']
    print fatList[0]
    return fatList[0]
