import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import csv

from createTrainingData import *

createTrainingData()



playerData = pd.read_csv('data/LakersPlayerData.csv')

playerList = []

# add each player to player list
for index, row in playerData.iterrows():
	player = row['Players']

	if player not in playerList:
		playerList.append(player)



# response vars
responseVars = ['FG', '3P', 'FT', 'ORB', 'DRB', 'AST', 'BLK', 'STL', 'TOV']
featureVars = ['Game', 'last_Home', 'last_MP', 'last_FG', 'last_FGA', 'last_FG%', 'last_3P', 'last_3PA', 'last_3P%', 'last_FT', 'last_FTA', 'last_FT%', 'last_ORB', 'last_DRB', 'last_TRB', 'last_AST', 'last_STL', 'last_BLK', 'last_TOV', 'last_PF', 'last_PTS', 'last_+/-', 'last_TS%', 'last_eFG%', 'last_3PAr', 'last_FTr', 'last_ORB%', 'last_DRB%', 'last_TRB%', 'last_AST%', 'last_STL%', 'last_BLK%', 'last_TOV%', 'last_USG%', 'last_ORtg', 'last_DRtg', 'avg_Home', 'avg_MP', 'avg_FG', 'avg_FGA', 'avg_FG%', 'avg_3P', 'avg_3PA', 'avg_3P%', 'avg_FT', 'avg_FTA', 'avg_FT%', 'avg_ORB', 'avg_DRB', 'avg_TRB', 'avg_AST', 'avg_STL', 'avg_BLK', 'avg_TOV', 'avg_PF', 'avg_PTS', 'avg_+/-', 'avg_TS%', 'avg_eFG%', 'avg_3PAr', 'avg_FTr', 'avg_ORB%', 'avg_DRB%', 'avg_TRB%', 'avg_AST%', 'avg_STL%', 'avg_BLK%', 'avg_TOV%', 'avg_USG%', 'avg_ORtg', 'avg_DRtg', 'avg_def_Home', 'avg_def_ORtg', 'avg_def_FTr', 'avg_def_3PAr', 'avg_def_TS%', 'avg_def_eFG%', 'avg_def_FT/FGA', 'avg_def_FG', 'avg_def_FGA', 'avg_def_FG%', 'avg_def_2P', 'avg_def_2PA', 'avg_def_2P%', 'avg_def_3P', 'avg_def_3PA', 'avg_def_3P%', 'avg_def_FT', 'avg_def_FTA', 'avg_def_FT%', 'avg_def_PTS', 'avg_def_ORB%', 'avg_def_TRB%', 'avg_def_AST%', 'avg_def_STL%', 'avg_def_BLK%', 'avg_def_TOV%', 'season_def_Home', 'season_def_ORtg', 'season_def_FTr', 'season_def_3PAr', 'season_def_TS%', 'season_def_eFG%', 'season_def_FT/FGA', 'season_def_FG', 'season_def_FGA', 'season_def_FG%', 'season_def_2P', 'season_def_2PA', 'season_def_2P%', 'season_def_3P', 'season_def_3PA', 'season_def_3P%', 'season_def_FT', 'season_def_FTA', 'season_def_FT%', 'season_def_PTS', 'season_def_ORB%', 'season_def_TRB%', 'season_def_AST%', 'season_def_STL%', 'season_def_BLK%', 'season_def_TOV%']


models = []

startTest = 29
endTest = 39			# one more so inclusive


# loop through each response var for each player
for var in responseVars:

	# remove response var from features
	features = featuresVars.remove('last_' + var)

	for player in playerList:

		for game in range(startTest, endTest):

			trainData = pd.read_csv('trainingData/' + vae + "/" + player + '.csv')

			X_Train = trainData[features]
			Y_Train = trainData['RESPONSEVAR']

			linreg = LinearRegression()
			linreg.fit(X_Train, Y_Train)


			# get row of test data corresponding to game
			createTest(player, game, var, featureVars):
			testData = pd.read_csv('test/' + var + '/' +  str(player) + game + '.csv')
			
			y_pred = linreg.predict(testData[features])
	




