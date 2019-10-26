import SportsNotificationsRequests.py


class Team:
    def __init__(self, teamName=None, leagueName=None, standing=None):
        self.teamName = teamName
        """self.leagueName = leagueName"""
        self.standing = standing


myTeam = Team("", "", "")


class LiveGame:

    def __init__(self, fixture_id, homeTeam, awayTeam, lineups, underWay, halfTimeScore, finalScore):
        self.fixture_id = fixture_id
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.lineups = lineups
        self.underWay = underWay
        self.halfTimeScore = halfTimeScore
        self.finalScore = finalScore


liveGame = LiveGame("", "", "", "", "", "", "", "", )
