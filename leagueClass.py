"""
OOP class for league processing
"""


class League:

    def __init__(self, name: str, teams: list):
        self.name = name
        self.teams = teams

    def __str__(self):
        string = f"__________________{self.name}__________________\n"
        for team in self.teams:
            string += f"\n{team}"
        return string

    def add_team(self, team: list):
        self.teams.append(team)
