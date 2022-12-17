"""
stores the data necessary for the proper functioning of the scripts
"""

from leagueClass import League

leagues_data = {
    "Ligue 1": {
        "League_class" :League("Ligue 1", ['PSG', 'Lens', 'Rennes', 'Olympique de Marseille', 'Lorient', 'AS Monaco', 'Lille', 'Olympique Lyonnais', 'Nice', 'Clermont', 'Reims', 'Toulouse', 'ESTAC Troyes', 'Montpellier', 'Nantes', 'Brest', 'Auxerre', 'AC Ajaccio', 'Strasbourg', 'Angers']),
        "url": "https://onefootball.com/fr/competition/ligue-1-uber-eats-23/classement",
        "api": "soccer_france_ligue_one"
    },
    "Premier League": {
        "League_class" :League("Premier League", ['Arsenal', 'Manchester City', 'Newcastle', 'Tottenham', 'Manchester United', 'Liverpool', 'Brighton Hove Albion FC', 'Chelsea', 'Fulham FC', 'Brentford FC', 'Crystal Palace', 'Aston Villa', 'Leicester City', 'Bournemouth', 'Leeds United', 'West Ham', 'Everton', 'Nottingham Forest', 'Southampton', 'Wolverhampton']),
        "url": "https://onefootball.com/fr/competition/premier-league-9/classement",
        "api": "soccer_epl"
    },
    "La Liga": {
        "League_class": League("La Liga", ['FC Barcelone', 'Real Madrid', 'Real Sociedad', 'Athletic Bilbao', 'Atlético Madrid', 'Real Betis Balompié', 'CA Osasuna', 'Rayo Vallecano', 'Villarreal', 'Valence CF', 'Majorque', 'Real Valladolid', 'Gérone', 'Almer a', 'Getafe', 'Espanyol de Barcelone', 'Celta Vigo', 'FC Séville', 'Cadix CF', 'Elche']),
        "url": "https://onefootball.com/fr/competition/laliga-10/classement",
        "api": "soccer_spain_la_liga"
    },
    "Bundesliga": {
        "League_class": League("Bundesliga", ['Bayern Munich', 'Fribourg', 'RB Leipzig', 'Eintracht Francfort', 'Union Berlin', 'Borussia Dortmund', 'Wolfsburg', 'Borussia M Gladbach', 'Werder Brême', 'Mayence', 'Hoffenheim', 'Bayer Leverkusen', 'Cologne', 'Augsbourg', 'Hertha Berlin', 'Stuttgart', 'Bochum', 'Schalke']),
        "url": "https://onefootball.com/fr/competition/bundesliga-1/classement",
        "api": "soccer_germany_bundesliga"
    },
    "Serie A": {
        "League_class": League("Serie A", ['Naples', 'AC Milan', 'Juventus Turin', 'Lazio Rome', 'Inter Milan', 'Atalanta Bergame', 'AS Rome', 'Udinese', 'Torino', 'Fiorentina', 'FC Bologne', 'US Salernitana', 'Empoli', 'AC Monza', 'Sassuolo', 'US Lecce', 'Spezia', 'US Cremonese', 'Sampdoria', 'Hellas Vérone']),
        "url": "https://onefootball.com/fr/competition/serie-a-13/classement",
        "api": "soccer_italy_serie_a"
    }
}