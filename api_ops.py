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

def compare_two_rosters(roster1, roster2):
    playersInBoth = []
    for player in roster1:
        if player in roster2:
            playersInBoth.append(player)
    return playersInBoth

def get_stats_url(season, player_id_list):
    stats_url = []
    for player in player_id_list:
        player_stats_url = config.people_url + str(player) + config.stats_single_season_url + season
        stats_url.append(player_stats_url)
    return stats_url

def get_flat_list(mylist):
    flat_list = []
    for sublist in mylist:
        if len(sublist)== 0:
            sublist.append(0)
        for item in sublist:
            flat_list.append(item)
    return flat_list

def get_player_points(player_urls):
    player_points_list = []
    for player in player_urls:
        player_stats = get_response(player)
        expression = jmespath.compile(config.jp_get_points)
        points = expression.search(player_stats)
        player_points_list.append(points)
        player_points = get_flat_list(player_points_list)
    return player_points

def get_player_improve(stat_list1, stat_list2):
    assert len(stat_list1) == len(stat_list2)
    improve_players = 0
    number_players = len(stat_list1)
    index = 0
    while index <= number_players - 1:
        # print(index)
        if stat_list1[index] < stat_list2[index]:
            improve_players += 1
        index += 1
    return improve_players

def get_roster_total(stat_list1):
    total_stat = 0
    for stat in stat_list1:
        total_stat += stat
    return total_stat
