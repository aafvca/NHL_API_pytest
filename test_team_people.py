import config, api_ops

roster_season2_teamsapi = api_ops.findRoster(config.season2)

teams_roster_season2_people = api_ops.get_player_team(roster_season2_teamsapi)
team_differences = api_ops.compare_teams("Montréal Canadiens", teams_roster_season2_people)

if team_differences == 0:
    print("The team in both API's match")
else:
    print("There is a mismatch between both API's")

position_people = api_ops.get_player_position_people(roster_season2_teamsapi)
positions_team = api_ops.get_player_position_team(config.season2)
different_positions = api_ops.compare_two_positions(position_people,positions_team)

if different_positions == 0:
    print("The players positions in both API's match")
else:
    print("There is a mismatch between both API's")
