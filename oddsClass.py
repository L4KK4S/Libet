"""
OOP class for odds processing
"""


class Odds:

    def __init__(self, data: list):
        self.data = data
        self.date, self.hour = self.get_date()
        self.home_team = data["home_team"]
        self.away_team = data["away_team"]
        self.home_odds = data["bookmakers"][0]["markets"][0]["outcomes"][0]["price"]
        self.away_odds = data["bookmakers"][0]["markets"][0]["outcomes"][1]["price"]
        self.draw_odds = data["bookmakers"][0]["markets"][0]["outcomes"][2]["price"]

    def __str__(self):
        string = f"{self.home_team}({self.home_odds}) | {self.draw_odds} | ({self.away_odds}){self.away_team}    {self.hour} | {self.date}\n"
        return string

    def get_date(self):
        day = self.data["commence_time"][8:10]
        month = self.data["commence_time"][5:7]
        year = self.data["commence_time"][:4]
        hour = self.data["commence_time"][11:-4]
        return f"{day}/{month}/{year}", hour