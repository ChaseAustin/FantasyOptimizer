import pandas as pd
import csv
import os

from createFeatures import *

def createTrainingData():
	# read player data games 9-38
	playerData = pd.read_csv('data/LakersPlayerData.csv')

	playerList = []

	# add each player to player list
	for index, row in playerData.iterrows():
		player = row['Players']

		if player not in playerList:
			playerList.append(player)


	#traing data for games 14-28
	startTraining = 14
	endTraining = 28		# one more so inclusive

	startTest = 29
	endTest = 39			# one more so inclusive

	playerData = {}

	print("Starting to Create Data...")

	# create directories
	responseVars = ['FG', '3P', 'FT', 'ORB', 'DRB', 'AST', 'BLK', 'STL', 'TOV']

	playerKeys = ['Home', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT',
				 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 
				 'PF', 'PTS', '+/-', 'TS%', 'eFG%', '3PAr', 'FTr', 'ORB%', 'DRB%', 
				 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'ORtg','DRtg']

	opponetKeys = ['Home', 'ORtg', 'FTr', '3PAr', 'TS%', 'eFG%', 'FT/FGA', 'FG',
				   'FGA', 'FG%', '2P', '2PA', '2P%', '3P', '3PA', '3P%', 'FT', 
				   'FTA', 'FT%', 'PTS', 'ORB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 
				   'TOV%'] 

	for var in responseVars:
		os.mkdir('trainingData/' + str(var))

	for var in responseVars:
		os.mkdir('testData/' + str(var))


	# create csv's for training data
	for var in responseVars:

		#print ("Training " + var + " data...")

		for player in playerList:

			headerList = []

			headerList.append("Game")

			rows = []

			# create header
			for h in playerKeys:
				if (h != var):
					headerList.append("last_" + h)
				else:
					headerList.append("RESPONSEVAR")
			
			for h in playerKeys:
				headerList.append("avg_" + h)

			for h in opponetKeys:
				headerList.append("avg_def_" + h)

			for h in opponetKeys:
				headerList.append("season_def_" + h)


			print ("Training " + str(player.split('\\')[0]) + " " + var + " data...")

			for game in range(startTraining, endTraining):

				#player statistical performance in last game
				data1 = playerFeat1(player, game)

				# player average statistical performance in last 5 games
				data2 = playerFeat2(player, game)

				# opposing team defense average statistical performance in last 5 games
				data3 = oppFeat1(game)
				
				# opposing team defense average statistical performance across season
				data4 = oppFeat1(game)

				dataList = []

				dataList.append(game)

				for h in data1:
					dataList.append(data1[h])

				for h in playerKeys:
					dataList.append(data2[h])

				for h in opponetKeys:
					dataList.append(data3[h])

				for h in opponetKeys:
					dataList.append(data4[h])


				rows.append(dataList)


			# turn features into csv file with one line
			# turn features into csv file with one line
			with open('trainingData/' + var + '/' +  str(player.split('\\')[0]) + '.csv', mode='w') as playerFile:
				playerWriter = csv.writer(playerFile, delimiter=',')
				
				playerWriter.writerow(headerList)
				
				for line in rows:
					playerWriter.writerow(line)


			print ("Test " + str(player.split('\\')[0]) + " " + var + " data...")

			rows.clear()

			for game in range(startTest, endTest):

				#player statistical performance in last game
				data1 = playerFeat1(player, game)

				# player average statistical performance in last 5 games
				data2 = playerFeat2(player, game)

				# opposing team defense average statistical performance in last 5 games
				data3 = oppFeat1(game)
				
				# opposing team defense average statistical performance across season
				data4 = oppFeat1(game)

				dataList = []

				dataList.append(game)

				for h in data1:
					dataList.append(data1[h])

				for h in playerKeys:
					dataList.append(data2[h])

				for h in opponetKeys:
					dataList.append(data3[h])

				for h in opponetKeys:
					dataList.append(data4[h])


				rows.append(dataList)

			# turn features into csv file with one line
			# turn features into csv file with one line
			with open('testData/' + var + '/' +  str(player.split('\\')[0]) + '.csv', mode='w') as playerFile:
				playerWriter = csv.writer(playerFile, delimiter=',')
				
				playerWriter.writerow(headerList)
				
				for line in rows:
					playerWriter.writerow(line)




		#print ("Done training " + var + " data...")
	print("Finished Creating Data")
