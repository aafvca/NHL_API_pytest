import config, api_ops

roster_season1 = api_ops.findRoster(config.season1)
roster_season2 = api_ops.findRoster(config.season2)

playersInBoth = api_ops.compare_two_rosters(roster_season1,roster_season2)

url_stats_season1 = api_ops.get_stats_url(config.season1, playersInBoth)
url_stats_season2 = api_ops.get_stats_url(config.season2, playersInBoth)

player_points_season1 =  (api_ops.get_player_points(url_stats_season1))
player_points_season2 =  (api_ops.get_player_points(url_stats_season2))


improve_players = api_ops.get_player_improve(player_points_season1,player_points_season2)

if len(player_points_season1) == improve_players:
    print("All the players improved")
else:
    print("Only " + str(improve_players) + " out of " + str(len(player_points_season1)) + " improved")

total_points_season1 = api_ops.get_roster_total(player_points_season1)

total_points_season2 = api_ops.get_roster_total(player_points_season2)

if total_points_season2 > total_points_season1:
    print ("There is an improvement in the team")
else:
    print("There is no improvement")
