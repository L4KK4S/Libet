"""
OOP class for team processing
"""


class Team:

    def __init__(self, rank: str, name: str, game: str, win: str, draw: str, lost: str, goal_average: str, points: str):
        self.rank = rank
        self.name = name
        self.game = game
        self.win = win
        self.draw = draw
        self.lost = lost
        self.goal_average = goal_average
        self.points = points

    def __str__(self):
        string = f" {self.rank} | {self.name} | G: {self.game} | W: {self.win} | D: {self.draw} | L: {self.lost} | GA: {self.goal_average}| P: {self.points}"
        return string
