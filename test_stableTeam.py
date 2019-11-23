import config, api_ops, jmespath
import pytest

# class TestStableTeam():

roster_season1 = api_ops.findRoster(config.season1)
roster_season2 = api_ops.findRoster(config.season2)
print(roster_season1)
print(roster_season2)

playersInBoth = api_ops.compare_two_rosters(roster_season1,roster_season2)
print(playersInBoth)
numberPlayersInBoth = len(playersInBoth)

if numberPlayersInBoth > 0:
    print("There are " + str(numberPlayersInBoth) + " players in both seasons")
else:
    print("None of the players continue the next season")
