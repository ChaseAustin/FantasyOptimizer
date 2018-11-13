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

		response = requests.get("https://rotogrinders.com/team-stats/nba-earned?site=draftkings&range=season")
		soup = BeautifulSoup(response.content, 'html.parser')
		proj_stats = soup.find('section', {'class': 'pag bdy'})
		script = proj_stats.find('script')
		script = str(script)
		script = script[67:]
		script = script[:-231]
		stats = json.loads(script)

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
# --------------------------------------------------


# Roto Wire

# Draftkings Daily Optimizer
# https://www.rotowire.com/daily/nba/optimizer.php
class wire_Player:
		def __init__(self):
			self.name = ""
			self.pos = ""
			self.team = ""
			self.opp = ""
			self.ml = 0
			self.ou = 0
			self.sprd = 0
			self.tmp = 0
			self.minutes = 0
			self.sal = 0
			self.fpts = 0
			self.val = 0

class wire_OptimizerStats:
	def __init__(self):
		self.players = []

		
		response = requests.get("https://www.rotowire.com/daily/tables/optimizer-nba.php?sport=NBA&site=FanDuel&projections=&type=main&slate=Main")
		stats = json.loads(response.text)
		
		for player in stats:
			
			p = wire_Player()

			p.name = player['player']
			p.pos = player['position']
			p.team = player['team']
			p.opp = player['opponent']
			p.ml = player['money_line']
			p.ou = player['over_under']
			p.sprd = player['point_spread']
			p.tmp = player['team_points']
			p.minutes = player['minutes']
			p.sal = player['salary']
			p.fpts = player['proj_rotowire']
			p.val = player['value']

			self.players.append(p)

# Defense vs Position Stats
# https://www.rotowire.com/daily/nba/defense-vspos.php?amp%3Bpos=PG&amp%3Bstatview=last10&site=FanDuel
class wire_DefenseStats:

	class wire_Team:
		def __init__(self):
			self.team = ""
			self.pos = ""
			self.fpts_allowed = 0
			self.pts = 0
			self.reb = 0
			self.ast = 0
			self.stl = 0
			self.blk = 0
			self.to = 0
			self.pm3 = 0
			self.fg = 0
			self.ft = 0

	def __init__(self):
		self.teams =[]
	
		response = requests.get("https://www.rotowire.com//daily/tables/defense-vspos-nba.php?sport=NBA&site=DraftKings&projections=&type=main&slate=all&pos=ALL&games=82")
		stats = json.loads(response.text)

		 #full table not available from this link. need to login

		'''
		for player in stats:
			
			p = wire_Player()

			p.name = player['player']
			p.pos = player['position']
			p.team = player['team']
			p.opp = player['opponent']
			p.ml = player['money_line']
			p.ou = player['over_under']
			p.sprd = player['point_spread']
			p.tmp = player['team_points']
			p.minutes = player['minutes']
			p.sal = player['salary']
			p.fpts = player['proj_rotowire']
			p.val = player['value']

			self.players.append(p)'''
'''		
# ----------------------------------------


# Stats.NBA

# PlayersGeneral Scoring
# https://stats.nba.com/players/scoring/?sort=GP&amp;dir=-1&dir=-1
class nba_GeneralStats:

	class nba_scoring:
		def __init__(self):
			self.name = ""
			self.team = ""
			self.age = 0
			self.gp = 0
			self.w = 0
			self.l = 0
			self.minutes = 0 
			self.fga2 = 0
			self.fga3 = 0
			self.pts2 = 0
			self.pts2MR = 0
			self.pts3 = 0
			self.ptsFBPS = 0
			self.ptsFT = 0
			self.ptsOFFTO = 0
			self.ptsPITP = 0
			self.fgm2AST = 0
			self.fgm2UAST = 0
			self.fgm3AST = 0
			self.fgm3UAST = 0
			self.fgmAST = 0
			self.fgmUAST = 0



	def __init__(self):
		self.players =[]

	def load_data(self):

		response = re.get("https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season")
		soup = BeautifulSoup(response.content, "html.parser")

		proj_stats = soup.find('div', {'id': 'projstats'})
		script = proj_stats.find('script')
		data = re.search(r"var data\s*=\s*(.*);", script.text).group(1)
		stats = json.loads(data)



# Players General Advanced
# https://stats.nba.com/players/advanced/?sort=GP&amp;dir=-1&dir=-1
class nba_AdvancedStats:

	class nba_Advanced:
		def __init__(self):
			self.name = ""
			self.team = ""
			self.age = 0
			self.gp = 0
			self.w = 0
			self.l = 0
			self.minutes = 0 
			self.offrtg = 0
			self.defrtg = 0
			self.netrtg = 0
			self.ast = 0
			self.ast_to = 0 
			self.ast_ratio = 0 
			self.oreb = 0
			self.dreb = 0
			self.red = 0
			self.to_ratio = 0 
			self.efg = 0
			self.ts = 0
			self.usg = 0
			self.pace = 0
			self.pie = 0


	def __init__(self):
		self.players =[]

	def load_data(self):

		response = re.get("https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season")
		soup = BeautifulSoup(response.content, "html.parser")


# Players Tracking Touches
# https://stats.nba.com/players/touches/
class nba_TouchesStats:

	class nba_Touches:
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

	def __init__(self):
		self.players =[]

	def load_data(self):

		response = re.get("https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season")
		soup = BeautifulSoup(response.content, "html.parser")

# ----------------------------------------

# Basketball Reference

# 2017-18 Player Stats Advanced
# https://www.basketball-reference.com/leagues/NBA_2018_advanced.html
class reference_Stats:

	class reference_playerss:
		def __init__(self):
			self.rank = 0
			self.name = ""
			self.team = ""
			self.gp = 0 
			self.w = 0
			self.l = 0
			self.minutes = 0 
			self.pts = 0
			self.touches = 0
			self.front_CT = 0
			self.top = 0
			self.avg_sec = 0
			self.avg_dpt = 0
			self.ppt = 0
			self.et = 0
			self.pu = 0
			self.paint = 0
			self.ppeb = 0
			self.pppt = 0
			self.pp_paint = 0

	def __init__(self):
		self.players =[]

	def load_data(self):

		response = re.get("https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season")
		soup = BeautifulSoup(response.content, "html.parser")


# ----------------------------------------
