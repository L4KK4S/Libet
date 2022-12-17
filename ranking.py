"""
Allows to know the rankings of the 5 main football championships in live.
"""

import lxml
import requests
from bs4 import BeautifulSoup
from leagueClass import League
from teamClass import Team
from data import *

def string2list(text: str):

    """
    Takes a string with spaces and returns a list of the different elements of this string.

    :param text: a simple string of characters
    :return: a list of the different elements

    example:
        >>> string2list("11  Reims  15  3  8  4  -5 17")
        ['11', 'Reims', '15', '3', '8', '4', '5', '17']
    """

    # initializes the variables
    alphabet = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZéìäê"
    temp_string = ""
    temp_list = list()

    # separates the element
    for character in text:
        if character in alphabet:
            temp_string += character
        else:
            if temp_string != "":
                temp_list.append(temp_string)
            temp_string = ""
    temp_list.append(temp_string)

    # if there is a compound word puts it in the same box
    run = True
    while run:
        if not temp_list[2].isdigit():
            tmp_ch = temp_list[2]
            temp_list[1] += f" {tmp_ch}"
            temp_list.pop(2)
        else:
            run = False

    return temp_list

def get_ranking_by_league(league: str):

    """
    This function return the ranking of a league.

    :param league: The name of the league
    :return: a list of the ranking

    example:
        >>> get_ranking_by_league("Ligue 1")
        __________________Ligue 1__________________

         1 | PSG | G: 15 | W: 13 | D: 2 | L: 0 | GA: 34| P: 41
         2 | Lens | G: 15 | W: 11 | D: 3 | L: 1 | GA: 16| P: 36
         3 | Rennes | G: 15 | W: 9 | D: 4 | L: 2 | GA: 17| P: 31
         4 | Olympique de Marseille | G: 15 | W: 9 | D: 3 | L: 3 | GA: 13| P: 30
         5 | Lorient | G: 15 | W: 8 | D: 4 | L: 3 | GA: 5| P: 28
         6 | AS Monaco | G: 15 | W: 8 | D: 3 | L: 4 | GA: 8| P: 27
         7 | Lille | G: 15 | W: 8 | D: 2 | L: 5 | GA: 4| P: 26
         8 | Olympique Lyonnais | G: 15 | W: 6 | D: 3 | L: 6 | GA: 5| P: 21
         9 | Nice | G: 15 | W: 5 | D: 5 | L: 5 | GA: 2| P: 20
         10 | Clermont | G: 15 | W: 5 | D: 4 | L: 6 | GA: 4| P: 19
         11 | Reims | G: 15 | W: 3 | D: 8 | L: 4 | GA: 5| P: 17
         12 | Toulouse | G: 15 | W: 4 | D: 4 | L: 7 | GA: 7| P: 16
         13 | ESTAC Troyes | G: 15 | W: 3 | D: 5 | L: 7 | GA: 5| P: 14
         14 | Montpellier | G: 15 | W: 4 | D: 2 | L: 9 | GA: 5| P: 14
         15 | Nantes | G: 15 | W: 2 | D: 7 | L: 6 | GA: 7| P: 13
         16 | Brest | G: 15 | W: 3 | D: 4 | L: 8 | GA: 12| P: 13
         17 | Auxerre | G: 15 | W: 3 | D: 4 | L: 8 | GA: 17| P: 13
         18 | AC Ajaccio | G: 15 | W: 3 | D: 3 | L: 9 | GA: 10| P: 12
         19 | Strasbourg | G: 15 | W: 1 | D: 8 | L: 6 | GA: 9| P: 11
         20 | Angers | G: 15 | W: 2 | D: 2 | L: 11 | GA: 19| P: 8

    """

    # get the league url
    match league:
        case "Ligue 1":
            url = leagues_data["Ligue 1"]["url"]
        case "Premier League":
            url = leagues_data["Premier League"]["url"]
        case "La Liga":
            url = leagues_data["La Liga"]["url"]
        case "Bundesliga":
            url = leagues_data["Bundesliga"]["url"]
        case "Serie A":
            url = leagues_data["Serie A"]["url"]
        case _:
            return "Error: This league is not reconized"

    # get the ressources for scrap the site
    source = requests.get(url).text
    page = BeautifulSoup(source, "lxml")
    data = list()

    # get the datas
    for a in page.find_all("a", class_="standings__row-grid"):
        temp_text = a.text.strip()
        data.append(string2list(temp_text))

    # processes the data for better display
    result = League(league, list())
    for i, team in enumerate(data):
        temp_team = Team(team[0], team[1], team[2], team[3], team[4], team[5], team[6], team[7])
        result.add_team(temp_team)

    # display the ranking
    print(result)
    return data

def get_ranking_all():

    """
    This function returns the ranking of the 5 main

    :return: a list of the list of all the leagues ranking
    """

    data = list()

    # call the get_ranking_by_league() function for eacch league and add the datas to a data list
    for league in ["Ligue 1", "Premier League", "La Liga", "Bundesliga", "Serie A"]:
        data.append(get_ranking_by_league(league))

    return data