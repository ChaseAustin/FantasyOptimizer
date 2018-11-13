class final_lineup_players:

	class lineup_player:
		def __init__(self):
			self.name = ""
			self.minutes = 0
			self.points = 0
			self.rebounds = 0
			self.assists = 0
			self.steals = 0
			self.blocks = 0
			self.turnovers = 0
			self.projection = 0
			self.vlaue = 0;

	def __init__(self):
		self.players = []

	def load_data(self):
		
		response = re.get("https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season")
		soup = BeautifulSoup(response.content, "html.parser")

		for x in soup.find_all('"id'):