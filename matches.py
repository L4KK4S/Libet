"""
Allows to get the next matches f the 5  main football championships.
"""

import lxml
import requests
from bs4 import BeautifulSoup
from todayClass import Today

def matches_by_day(day: str = " "):

    """
    
    Gets the matches of a day.

    :param day: the day for the matches, the expected format is MM/DD/AAAA, if the parameter is empty the date is today
    :return:
    
    example:
        >>> matches_by_day("10/10/2022")
        Results of 10/10/2022 :
            Premier League -> Nottingham Forest 1-1 Aston Villa / Finished 
            Serie A -> Fiorentina 0-4 Lazio / Finished 
    """
    # creates an Today object of the day
    today = Today()
    after = 0

    if day == " ":
        day = f"{today.m}/{today.d}/{today.y}"

    # get the url and the web datas
    url = f"https://www.pronosoft.com/fr/resultats/football/{day.split('/')[2]}-{day.split('/')[0]}-{day.split('/')[1]}/"
    source = requests.get(url).text
    soup = BeautifulSoup(source, "lxml")
    temp_data = list()
    data = list()

    # if the day is after, before or is today
    if int(today.y) > int(day.split('/')[2]):
        after = 1
    elif int(today.y) == int(day.split('/')[2]):
        if int(today.m) > int(day.split('/')[0]):
            after = 1
        elif int(today.m) == int(day.split('/')[0]):
            if int(today.d) > int(day.split('/')[1]):
                after = 1
            elif int(today.d) == int(day.split('/')[1]):
                after = 2

    # web scrap the datas
    for bloc in soup.find_all("table", class_="livescore table_league visible"):
        temp_l = list()
        temp_l.append(bloc.find_all("a")[1].text)
        temp_l.append(bloc.find_all("a")[2].text)
        for match in bloc.find_all("tr"):
            for elt in match.find_all("td", class_="home_l"):
                temp_l.append(elt.text.strip())
            for elt in match.find_all("td", class_="ext_l"):
                temp_l.append(elt.text.strip())
            for elt in match.find_all("a", href="javascript:;"):
                temp_l.append(elt.text.strip()[:3])
            if not temp_l[-1][0].isdigit():
                temp_l.append("?-?")
            if after == 2:
                if match.find("td", class_="time time_on") != None:
                    temp_l.append(match.find("td", class_="time time_on").text)
                elif match.find("td", class_="time time_ht") != None:
                    temp_l.append(match.find("td", class_="time time_ht").text)
                elif match.find("td", class_="time time_ft") != None:
                    temp_l.append("Fini")
                elif match.find("td", class_="time") != None and len(match.find_all("span")) > 1:
                    temp_l.append(match.find_all("span")[1].text)
                elif match.find("td", class_="time") != None and len(match.find_all("span")) == 1:
                    temp_l.append(match.find("span").text)
            elif after == 1:
                temp_l.append("Finished")
            elif after == 0:
                temp_l.append(match.find_all("span")[1].text)


        temp_data.append(temp_l)


    is_match = False
    for match in temp_data:
        if match[0] in ["France", "Angleterre", "Allemagne", "Italie", "Espagne"] and match[1] in ["Ligue 1", "Premier League", "Bundesliga", "Serie A", "La Liga"]:
            if not is_match :
                print(f"Results of {day} :")
                is_match = True
            nb_matchs = (len(match) - 2) // 4
            for i in range(nb_matchs):
                print(f"    {match[1]} -> {match[2 + (i*4)]} {match[4 + (i*4)]} {match[3 + (i*4)]} / {match[5 + (i*4)]} ")
                data.append([match[1], match[2 + (i*4)], match[3 + (i*4)], match[4 + (i*4)], match[5 + (i*4)]])

    if not is_match:
        print(f"There is no match the {day}")


    return data

