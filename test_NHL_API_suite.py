import config, api_ops, pytest

class Test_NHL_API_suite():
    @pytest.fixture()
    def test_setup(self):

        global roster_season2
        global players_inboth
        global player_points_season1
        global player_points_season2

        roster_season1 = api_ops.findRoster(config.season1)
        roster_season2 = api_ops.findRoster(config.season2)
        players_inboth = api_ops.compare_two_rosters(roster_season1, roster_season2)
        url_stats_season1 = api_ops.get_stats_url(config.season1, players_inboth)
        url_stats_season2 = api_ops.get_stats_url(config.season2, players_inboth)
        player_points_season1 = (api_ops.get_player_points(url_stats_season1))
        player_points_season2 = (api_ops.get_player_points(url_stats_season2))

    def test_stableTeam(self,test_setup):
        numberPlayersInBoth = len(players_inboth)
        assert numberPlayersInBoth > 0 , "None of the players continue the next season"

    def test_playerImprovement(self,test_setup):
        improve_players = api_ops.get_player_improve(player_points_season1, player_points_season2)
        assert len(player_points_season1) == improve_players, "Only " + str(improve_players) + " players out of " + str(len(player_points_season1)) + " improved"

    def test_teamImprovement(self,test_setup):
        total_points_season1 = api_ops.get_roster_total(player_points_season1)
        total_points_season2 = api_ops.get_roster_total(player_points_season2)
        assert total_points_season2 > total_points_season1, "There is no improvement in the team between the two seasons"

    def test_same_team(self,test_setup):
        teams_roster_season2_people = api_ops.get_player_team(roster_season2)
        team_differences = api_ops.compare_teams(config.team, teams_roster_season2_people)
        assert team_differences == 0, "There is a mismatch between both API's"

    def test_same_position(self,test_setup):
        position_people = api_ops.get_player_position_people(roster_season2)
        positions_team = api_ops.get_player_position_team(config.season2)
        different_positions = api_ops.compare_two_positions(position_people, positions_team)
        assert different_positions == 0, "There is a mismatch between both API's"
