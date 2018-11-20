import inputClasses
from bs4 import BeautifulSoup
import requests as requests
import re
import pandas as pd
import json
import urllib.request
# Rotogrinders

#  Draft Kings Player Stats
# https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season
class grinder_Player:
    def __init__(self):
        self.name = ""
        self.team = ""
        self.pos = ""
        self.salary = 0
        self.minutes = 0
        self.reb = 0
        self.ast = 0
        self.stl = 0
        self.blk = 0
        self.to = 0
        self.pts = 0
        self.usg = 0
        self.fpts = 0

class grinder_PlayerStats:
    def __init__(self):
        self.players = []

        response = requests.get("https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season")
        soup = BeautifulSoup(response.content, 'html.parser')
        proj_stats = soup.find('div', {'id': 'proj-stats'})
        script = proj_stats.find('script')
        data = re.search(r"var data\s*=\s*(.*);", script.text)
        stats = json.loads(data)

        prnt ("starting\n")

        for player in stats:
            
            p = grinder_Player()

            numGames = player['gp']

            p.name = player['player']
            p.team = player['team']
            p.pos = player['player']
            p.salary = player['salary']
            p.minutes = float(player['min']) / numGames
            p.reb = player['reb'] / numGames
            p.ast = player['ast'] / numGames
            p.stl = player['stl'] / numGames
            p.blk = player['blk'] / numGames
            p.to = player['to'] / numGames
            p.pts = player['pts'] / numGames
            p.usg = player['usg']
            p.fpts = float(player['fpts']) / numGames
            


            self.players.append(p)
        # -------------------------

# Team Stats
# https://rotogrinders.com/team-stats/nba-earned?site=draftkings&range=season
class grinder_Team:
    def __init__(self):
        self.name = ""
        self.gp = 0
        self.minutes = 0
        self.reb = 0
        self.ast = 0
        self.stl = 0
        self.blk = 0
        self.to = 0
        self.pts = 0
        self.pace = 0
        self.fpts = 0

class grinder_TeamStats:
    def __init__(self):
        self.teams = []

        response = requests.get("https://rotogrinders.com/team-stats/nba-earned?site=fanduel&range=season")
        soup = BeautifulSoup(response.content, 'html.parser')
        proj_stats = soup.find('section', {'class': 'pag bdy'})
        script = proj_stats.find('script')
        script = str(script)
        script = script[67:]
        script = script[:-231]
        stats = json.loads(script)

        print ("starting\n")

        for team in stats:
            
            t = grinder_Team()

            numGames = team['gp']

            t.name = team['team']
            t.gp = team['gp']
            t.minutes = float(team['min']) / numGames
            t.reb = team['reb'] / numGames
            t.ast = team['ast'] / numGames
            t.stl = team['stl'] / numGames
            t.blk = team['blk'] / numGames
            t.to = team['to'] / numGames
            t.pts = team['pts'] / numGames
            t.pace = team['usg']
            t.fpts = float(team['fpts']) / numGames
            
            self.teams.append(t)
            print (t.name)
            print ("\n")
        print ("done")

# --------------------------------------------------
'''
# Stats.NBA

# Players Tracking Touches
# https://stats.nba.com/players/touches/
class nba_TouchesStats:

    class nba_Touches:
        def __init__(self):
            

    def __init__(self):
        self.players =[]

    def load_data(self):

        response = re.get("https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season")
        soup = BeautifulSoup(response.content, "html.parser")

# ----------------------------------------

# Basketball Reference

# 2017-18 Player Stats Advanced
# https://www.basketball-reference.com/leagues/NBA_2018_advanced.html
class reference_player:
    def __init__(self):
        self.name = ""
        self.pos = ""
        self.age = 0
        self.team = ""
        self.g = 0 
        self.mp = 0
        self.per = 0
        self.ts = 0 
        self.par3 = 0
        self.ftr= 0
        self.obr = 0
        self.drb = 0
        self.trb = 0
        self.ast = 0
        self.stl = 0
        self.blk = 0
        self.tov = 0
        self.usg = 0
        self.ows = 0
        self.dws = 0
        self.ws = 0
        self.ws48 = 0
        self.obpm = 0
        self.dbpm = 0
        self.bpm = 0
        self.vorp = 0


class reference_Stats:
    def __init__(self):
        self.players = []

        response = requests.get("https://www.basketball-reference.com/leagues/NBA_2018_advanced.html")
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find('table', attrs={'class':'sortable stats_table'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        
        for row in rows:
            columns = row.find_all('td')
            
            p = reference_player()

            for column in columns:
                p.name = column.get_text()
                p.pos = column.get_text()
                p.age = column.get_text()
                p.team = column.get_text()
                p.g = column.get_text()
                p.mp = column.get_text()
                p.per = column.get_text()
                p.ts = column.get_text()
                p.par3 = column.get_text()
                p.ftr = column.get_text()
                p.obr = column.get_text()
                p.drb = column.get_text()
                p.trb = column.get_text()
                p.ast = column.get_text()
                p.stl = column.get_text()
                p.blk = column.get_text()
                p.tov = column.get_text()
                p.usg = column.get_text()
                
                trash = column.get_text()
                
                p.ows = column.get_text()
                p.dws = column.get_text()
                p.ws = column.get_text()
                p.ws48 = column.get_text()
                
                trash = column.get_text()

                p.obpm = column.get_text()
                p.dbpm = column.get_text()
                p.bpm = column.get_text()
                p.vorp = column.get_text()
                self.players.append(p)
# ----------------------------------------
'''