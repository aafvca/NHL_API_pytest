import config, api_ops

roster_season1 = api_ops.findRoster(config.season1)
roster_season2 = api_ops.findRoster(config.season2)

playersInBoth = api_ops.compare_two_rosters(roster_season1,roster_season2)
numberPlayersInBoth = len(playersInBoth)

if numberPlayersInBoth > 0:
    print("There are " + str(numberPlayersInBoth) + " players in both seasons")
else:
    print("None of the players continue the next season")
