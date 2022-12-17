"""
Allows to get the odds of the matches of the 5  main football championships.
"""

import requests
from oddsClass import Odds
from data import *



def get_odds_by_league(league: str):

    """
    gets the odds of the next day's games by league.

    :param league: the league we want to operate
    :return: the list of the odds of the league

    example:
        >>>odds.get_odds_by_league("Ligue 1")
        AC Ajaccio(1.97) | 3.35 | (4.1)Angers    14:00 | 28/12/2022
        Troyes(2.85) | 3.58 | (2.38)Nantes    14:00 | 28/12/2022
        Auxerre(1.8) | 3.83 | (4.3)AS Monaco    16:00 | 28/12/2022
        Clermont(4.42) | 3.75 | (1.8)Lille    18:00 | 28/12/2022
        Brest(3.85) | 3.75 | (1.91)Lyon    20:00 | 28/12/2022
        Paris Saint Germain(1.27) | 6.25 | (9.85)Strasbourg    20:00 | 28/12/2022
        Lorient(1.99) | 3.67 | (3.63)Montpellier    16:00 | 29/12/2022
        Stade de Reims(2.25) | 3.37 | (3.23)Rennes    18:00 | 29/12/2022
        Marseille(1.52) | 4.52 | (5.8)Toulouse    20:00 | 29/12/2022
        Nice(3.18) | 3.0 | (2.48)RC Lens    20:00 | 29/12/2022
        Toulouse(3.97) | 3.25 | (2.03)AC Ajaccio    14:00 | 01/01/2023
        AS Monaco(1.48) | 4.7 | (6.1)Brest    14:00 | 01/01/2023
        Angers(2.88) | 3.35 | (2.48)Lorient    14:00 | 01/01/2023
        Nantes(3.8) | 3.32 | (2.06)Auxerre    14:00 | 01/01/2023
        Lyon(6.95) | 4.93 | (1.42)Clermont    16:00 | 01/01/2023
        RC Lens(1.94) | 3.82 | (3.68)Paris Saint Germain    19:45 | 01/01/2023
        Strasbourg(1.83) | 3.77 | (4.2)Troyes    14:00 | 02/01/2023
        Lille(1.63) | 4.02 | (5.4)Stade de Reims    16:00 | 02/01/2023
        Montpellier(1.89) | 3.75 | (3.95)Marseille    18:00 | 02/01/2023
        Rennes(4.22) | 3.8 | (1.82)Nice    20:00 | 02/01/2023

    """

    # get the league api
    match league:
        case "Ligue 1":
            api = leagues_data["Ligue 1"]["api"]
        case "Premier League":
            api = leagues_data["Premier League"]["api"]
        case "La Liga":
            api = leagues_data["La Liga"]["api"]
        case "Bundesliga":
            api = leagues_data["Bundesliga"]["api"]
        case "Serie A":
            api = leagues_data["Serie A"]["api"]
        case _:
            return "Error: This league is not reconized"

    # initialize the variables
    api_key = "2c366662b6a06eeab2ac282248ffcf62"
    url = f"https://api.the-odds-api.com/v4/sports/{api}/odds?regions=eu&apiKey={api_key}&bookmakers=betclic"
    data = list()

    # call the api
    response = requests.get(url)
    content = response.json()

    # get the datas
    for row in content:
        if row["bookmakers"] != []:
            match = Odds(row)
            data.append(match)

    # display the odds
    for odds in data:
        print(odds)



    return data

def get_odds_all():
    """
       This function returns the odds on the next day's matches in the 5 major leagues.

       :return: a list of the list of all the leagues odds
       """

    data = list()

    # call the get_odds_by_league() function for eacch league and add the datas to a data list
    for league in ["Ligue 1", "Premier League", "La Liga", "Bundesliga", "Serie A"]:
        data.append(get_odds_by_league(league))

    return data
