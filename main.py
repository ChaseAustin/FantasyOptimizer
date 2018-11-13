from bs4 import BeautifulSoup
import requests as re
import pandas as pd

import inputClasses


response = re.get("https://rotogrinders.com/game-stats/nba-player?site=draftkings&range=season")
soup = BeautifulSoup(response.content, 'html.parser')
proj_stats = soup.find('div', {'id': 'proj-stats'})
script = proj_stats.find('script')
data = re.search(r"var data\s*=\s*(.*);", script.text).group(1)
stats = json.loads(data)

print (stats)
