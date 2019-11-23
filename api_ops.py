import requests
import config
import jmespath

def get_response(url):
    url_request = requests.get(url)
    status_code = url_request.status_code
    response = url_request.json()
    assert status_code == 200
    return response

def findRoster(season):
    roster_url = config.mtl_roster_ep + season
    team_info = get_response(config.teams_url + roster_url)
    expression = jmespath.compile(config.jp_get_names)
    team_roster = expression.search(team_info)
    assert len(team_roster) != 0
    return team_roster
