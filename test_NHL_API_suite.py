import config, api_ops, pytest

class Test_NHL_API_suite():
    roster_season1 = api_ops.findRoster(config.season1)
    global roster_season2
    roster_season2 = api_ops.findRoster(config.season2)
    global players_inboth
    players_inboth = api_ops.compare_two_rosters(roster_season1, roster_season2)

    def test_stableTeam(self):
        numberPlayersInBoth = len(players_inboth)
        assert numberPlayersInBoth > 0

        if numberPlayersInBoth > 0:
            print("There are " + str(numberPlayersInBoth) + " players in both seasons")
        else:
            print("None of the players continue the next season")


    def test_teamImprovement(self):
        url_stats_season1 = api_ops.get_stats_url(config.season1, players_inboth)
        url_stats_season2 = api_ops.get_stats_url(config.season2, players_inboth)

        player_points_season1 = (api_ops.get_player_points(url_stats_season1))
        player_points_season2 = (api_ops.get_player_points(url_stats_season2))

        improve_players = api_ops.get_player_improve(player_points_season1, player_points_season2)

        if len(player_points_season1) == improve_players:
            print("All the players improved")
        else:
            print("Only " + str(improve_players) + " out of " + str(len(player_points_season1)) + " improved")

        total_points_season1 = api_ops.get_roster_total(player_points_season1)

        total_points_season2 = api_ops.get_roster_total(player_points_season2)

        if total_points_season2 > total_points_season1:
            print("There is an improvement in the team")
        else:
            print("There is no improvement")

    def test_team_people(self):
        # roster_season2_teamsapi = api_ops.findRoster(config.season2)

        teams_roster_season2_people = api_ops.get_player_team(roster_season2)
        team_differences = api_ops.compare_teams("Montréal Canadiens", teams_roster_season2_people)

        if team_differences == 0:
            print("The team in both API's match")
        else:
            print("There is a mismatch between both API's")

        position_people = api_ops.get_player_position_people(roster_season2)
        positions_team = api_ops.get_player_position_team(config.season2)
        different_positions = api_ops.compare_two_positions(position_people, positions_team)

        if different_positions == 0:
            print("The positions in both API's match")
        else:
            print("There is a mismatch between both API's")
