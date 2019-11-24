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

def get_flat_list_int(mylist):
    flat_list = []
    for sublist in mylist:
        if len(sublist)== 0:
            sublist.append(0)
        for item in sublist:
            flat_list.append(item)
    return flat_list

def get_flat_list_str(mylist):
    flat_list = []
    for sublist in mylist:
        if len(sublist) == 0:
            sublist.append('N/A')
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
        player_points = get_flat_list_int(player_points_list)
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

def get_player_team(player_list):
    player_team = []
    player_team_list = []
    expression = jmespath.compile(config.jp_get_team)
    for player in player_list:
        player_info = get_response(config.people_url + str(player))
        team = expression.search(player_info)
        player_team_list.append(team)
        player_team = get_flat_list_str(player_team_list)
    return player_team

def compare_teams(team_name, team_list):
    differences = 0
    for team in team_list:
        if team != team_name:
            differences +=1
    return differences

def get_player_position_people(player_list):
    player_position = []
    player_position_list = []
    expression = jmespath.compile((config.jp_get_position_people))
    for player in player_list:
        player_info = get_response(config.people_url + str(player))
        position = expression.search(player_info)
        player_position_list.append((position))
        player_position = get_flat_list_str(player_position_list)
    return player_position

def get_player_position_team(season):
    expression = jmespath.compile(config.jp_get_position_team)
    url = config.teams_url + config.mtl_roster_ep + season
    roster_info = get_response(url)
    player_position = expression.search(roster_info)
    return player_position

def compare_two_positions(positions1, positions2):
    different_position = 0
    for position in positions1:
        if position not in positions2:
            different_position +=1
    return different_position

