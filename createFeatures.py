import pandas as pd
import math

def playerFeat1(player, game):


	returnData = {}

	# initalize
	returnData['Home'] = 0 
	returnData['MP'] = 0 
	returnData['FG'] = 0 
	returnData['FGA'] = 0 
	returnData['FG%'] = 0 
	returnData['3P'] = 0 
	returnData['3PA'] = 0 
	returnData['3P%'] = 0 
	returnData['FT'] = 0 
	returnData['FTA'] = 0 
	returnData['FT%'] = 0 
	returnData['ORB'] = 0 
	returnData['DRB'] = 0 
	returnData['TRB'] = 0 
	returnData['AST'] = 0 
	returnData['STL'] = 0 
	returnData['BLK'] = 0 
	returnData['TOV'] = 0 
	returnData['PF'] = 0 
	returnData['PTS'] = 0 
	returnData['+/-'] = 0 
	returnData['TS%'] = 0 
	returnData['eFG%'] = 0 
	returnData['3PAr'] = 0 
	returnData['FTr'] = 0 
	returnData['ORB%'] = 0 
	returnData['DRB%'] = 0 
	returnData['TRB%'] = 0 
	returnData['AST%'] = 0 
	returnData['STL%'] = 0 
	returnData['BLK%'] = 0 
	returnData['TOV%'] = 0 
	returnData['USG%'] = 0 
	returnData['ORtg'] = 0 
	returnData['DRtg'] = 0 


	data = pd.read_csv('data/LakersPlayerData.csv')

	prevGame = game - 1

	for index, row in data.iterrows():
		
		if ((row['Players'] == player) and (row['Game'] == prevGame)):

			returnData['Home'] = float(row['Home'])
			realTime = 0

			time = row['MP']
				
			min1 = time[0]

			if min1.isdigit():

				if (time[1] != ':'):

					min2 = time[1]
					sec1 = time[3]
					sec2 = time[4]

					realTime = float(min1) * 10
					realTime += float(min2)

					sec = float(sec1) * 10
					sec += float(sec2)

					sec = sec / 60
					
					realTime += (sec / 100)

				else :

					sec1 = time[2]
					sec2 = time[3]

					realTime = float(min1) * 10

					sec = float(sec1) * 10
					sec += float(sec2)

					sec = sec / 60
					
					realTime += (sec / 100)

			returnData['MP'] = realTime

			if realTime == 0:
				continue


			returnData['FG'] = checkNaN(float(row['FG']))
			returnData['FGA'] = checkNaN(float(row['FGA']))
			returnData['FG%'] = checkNaN(float(row['FG%']))
			returnData['3P'] = checkNaN(float(row['3P']))
			returnData['3PA'] = checkNaN(float(row['3PA']))
			returnData['3P%'] = checkNaN(float(row['3P%']))
			returnData['FT'] = checkNaN(float(row['FT']))
			returnData['FTA'] = checkNaN(float(row['FTA']))
			returnData['FT%'] = checkNaN(float(row['FT%']))
			returnData['ORB'] = checkNaN(float(row['ORB']))
			returnData['DRB'] = checkNaN(float(row['DRB']))
			returnData['TRB'] = checkNaN(float(row['TRB']))
			returnData['AST'] = checkNaN(float(row['AST']))
			returnData['STL'] = checkNaN(float(row['STL']))
			returnData['BLK'] = checkNaN(float(row['BLK']))
			returnData['TOV'] = checkNaN(float(row['TOV']))
			returnData['PF'] = checkNaN(float(row['PF']))
			returnData['PTS'] = checkNaN(float(row['PTS']))
			returnData['+/-'] = checkNaN(float(row['+/-']))
			returnData['TS%'] = checkNaN(float(row['TS%']))
			returnData['eFG%'] = checkNaN(float(row['eFG%']))
			returnData['3PAr'] = checkNaN(float(row['3PAr']))
			returnData['FTr'] = checkNaN(float(row['FTr']))
			returnData['ORB%'] = checkNaN(float(row['ORB%']))
			returnData['DRB%'] = checkNaN(float(row['DRB%']))
			returnData['TRB%'] = checkNaN(float(row['TRB%']))
			returnData['AST%'] = checkNaN(float(row['AST%']))
			returnData['STL%'] = checkNaN(float(row['STL%']))
			returnData['BLK%'] = checkNaN(float(row['BLK%']))
			returnData['TOV%'] = checkNaN(float(row['TOV%']))
			returnData['USG%'] = checkNaN(float(row['USG%']))
			returnData['ORtg'] = checkNaN(float(row['ORtg']))
			returnData['DRtg'] = checkNaN(float(row['DRtg']))

	return returnData


def playerFeat2(player, game):

	returnData = {}

	data = pd.read_csv('data/LakersPlayerData.csv')

	currentGame = game - 5

	# initalize
	returnData['Home'] = 0 
	returnData['MP'] = 0 
	returnData['FG'] = 0 
	returnData['FGA'] = 0 
	returnData['FG%'] = 0 
	returnData['3P'] = 0 
	returnData['3PA'] = 0 
	returnData['3P%'] = 0 
	returnData['FT'] = 0 
	returnData['FTA'] = 0 
	returnData['FT%'] = 0 
	returnData['ORB'] = 0 
	returnData['DRB'] = 0 
	returnData['TRB'] = 0 
	returnData['AST'] = 0 
	returnData['STL'] = 0 
	returnData['BLK'] = 0 
	returnData['TOV'] = 0 
	returnData['PF'] = 0 
	returnData['PTS'] = 0 
	returnData['+/-'] = 0 
	returnData['TS%'] = 0 
	returnData['eFG%'] = 0 
	returnData['3PAr'] = 0 
	returnData['FTr'] = 0 
	returnData['ORB%'] = 0 
	returnData['DRB%'] = 0 
	returnData['TRB%'] = 0 
	returnData['AST%'] = 0 
	returnData['STL%'] = 0 
	returnData['BLK%'] = 0 
	returnData['TOV%'] = 0 
	returnData['USG%'] = 0 
	returnData['ORtg'] = 0 
	returnData['DRtg'] = 0 


	for index, row in data.iterrows():
		
		if (currentGame == game):
			
			for feat in returnData: 	
				returnData[feat] /= 5

			return returnData

		if ((row['Players'] == player) and (row['Game'] == currentGame)):

			returnData['Home'] = float(row['Home'])
			
			realTime = 0

			time = row['MP']
				
			min1 = time[0]

			if min1.isdigit():

				if (time[1] != ':'):

					min2 = time[1]
					sec1 = time[3]
					sec2 = time[4]

					realTime = float(min1) * 10
					realTime += float(min2)

					sec = float(sec1) * 10
					sec += float(sec2)

					sec = sec / 60
					
					realTime += (sec / 100)

				else :

					sec1 = time[2]
					sec2 = time[3]

					realTime = float(min1) * 10

					sec = float(sec1) * 10
					sec += float(sec2)

					sec = sec / 60
					
					realTime += (sec / 100)

			returnData['MP'] = realTime

			if realTime == 0:
				continue
			
			returnData['FG'] = checkNaN(float(row['FG']))
			returnData['FGA'] = checkNaN(float(row['FGA']))
			returnData['FG%'] = checkNaN(float(row['FG%']))
			returnData['3P'] = checkNaN(float(row['3P']))
			returnData['3PA'] = checkNaN(float(row['3PA']))
			returnData['3P%'] = checkNaN(float(row['3P%']))
			returnData['FT'] = checkNaN(float(row['FT']))
			returnData['FTA'] = checkNaN(float(row['FTA']))
			returnData['FT%'] = checkNaN(float(row['FT%']))
			returnData['ORB'] = checkNaN(float(row['ORB']))
			returnData['DRB'] = checkNaN(float(row['DRB']))
			returnData['TRB'] = checkNaN(float(row['TRB']))
			returnData['AST'] = checkNaN(float(row['AST']))
			returnData['STL'] = checkNaN(float(row['STL']))
			returnData['BLK'] = checkNaN(float(row['BLK']))
			returnData['TOV'] = checkNaN(float(row['TOV']))
			returnData['PF'] = checkNaN(float(row['PF']))
			returnData['PTS'] = checkNaN(float(row['PTS']))
			returnData['+/-'] = checkNaN(float(row['+/-']))
			returnData['TS%'] = checkNaN(float(row['TS%']))
			returnData['eFG%'] = checkNaN(float(row['eFG%']))
			returnData['3PAr'] = checkNaN(float(row['3PAr']))
			returnData['FTr'] = checkNaN(float(row['FTr']))
			returnData['ORB%'] = checkNaN(float(row['ORB%']))
			returnData['DRB%'] = checkNaN(float(row['DRB%']))
			returnData['TRB%'] = checkNaN(float(row['TRB%']))
			returnData['AST%'] = checkNaN(float(row['AST%']))
			returnData['STL%'] = checkNaN(float(row['STL%']))
			returnData['BLK%'] = checkNaN(float(row['BLK%']))
			returnData['TOV%'] = checkNaN(float(row['TOV%']))
			returnData['USG%'] = checkNaN(float(row['USG%']))
			returnData['ORtg'] = checkNaN(float(row['ORtg']))
			returnData['DRtg'] = checkNaN(float(row['DRtg']))

			currentgame = currentGame + 1

	return returnData


def oppFeat1(game):

	returnData = {}

	data = pd.read_csv('data/lakersOpp/game' + str(game) + '.csv')


	maxGame = 0
	for index, row in data.iterrows():
		maxGame = row["Rk"]


	currentGame = maxGame - 5

	returnData['Home'] = 0
	returnData['ORtg'] = 0
	returnData['FTr'] = 0 
	returnData['3PAr'] = 0 
	returnData['TS%'] = 0 
	returnData['eFG%'] = 0 
	returnData['FT/FGA'] = 0 
	returnData['FG'] = 0 
	returnData['FGA'] = 0 
	returnData['FG%'] = 0 
	returnData['2P'] = 0 
	returnData['2PA'] = 0 
	returnData['2P%'] = 0 
	returnData['3P'] = 0 
	returnData['3PA'] = 0 
	returnData['3P%'] = 0 
	returnData['FT'] = 0 
	returnData['FTA'] = 0 
	returnData['FT%'] = 0 
	returnData['PTS'] = 0 
	returnData['ORB%'] = 0
	returnData['TRB%'] = 0 
	returnData['AST%'] = 0 
	returnData['STL%'] = 0 
	returnData['BLK%'] = 0 
	returnData['TOV%'] = 0 

	for index, row in data.iterrows():
		
		if (currentGame == maxGame):
			
			for feat in returnData: 	
				returnData[feat] /= 5

			return returnData

		if row['Rk'] == currentGame:

			if row['Home'] == "@":
				returnData['Home'] += 0
			else:
				returnData['Home'] += 1

			returnData['ORtg'] += checkGood(row['ORtg'])
			returnData['FTr'] += checkGood(row['FTr'])
			returnData['3PAr'] += checkGood(row['3PAr'])
			returnData['TS%'] += checkGood(row['TS%'])
			returnData['eFG%'] += checkGood(row['eFG%'])
			returnData['FT/FGA'] += checkGood(row['FT/FGA'])
			returnData['FG'] += checkGood(row['FG'])
			returnData['FGA'] += checkGood(row['FGA'])
			returnData['FG%'] += checkGood(row['FG%'])
			returnData['2P'] += checkGood(row['2P'])
			returnData['2PA'] += checkGood(row['2PA'])
			returnData['2P%'] += checkGood(row['2P%'])
			returnData['3P'] += checkGood(row['3P'])
			returnData['3PA'] += checkGood(row['3PA'])
			returnData['3P%'] += checkGood(row['3P%'])
			returnData['FT'] += checkGood(row['FT'])
			returnData['FTA'] += checkGood(row['FTA'])
			returnData['FT%'] += checkGood(row['FT%'])
			returnData['PTS'] += checkGood(row['PTS'])
			returnData['ORB%'] += checkGood(row['ORB%'])
			returnData['TRB%'] += checkGood(row['TRB%'])
			returnData['AST%'] += checkGood(row['AST%'])
			returnData['STL%'] += checkGood(row['STL%'])
			returnData['BLK%'] += checkGood(row['BLK%'])
			returnData['TOV%'] += checkGood(row['TOV%'])

			currentGame = currentGame + 1

	return returnData


def oppFeat2(game):

	returnData = {}

	data = pd.read_csv('data/lakersOpp/game' + str(game) + '.csv')

	gameCount = 0

	returnData['Home'] = 0
	returnData['ORtg'] = 0
	returnData['FTr'] = 0 
	returnData['3PAr'] = 0 
	returnData['TS%'] = 0 
	returnData['eFG%'] = 0 
	returnData['FT/FGA'] = 0 
	returnData['FG'] = 0 
	returnData['FGA'] = 0 
	returnData['FG%'] = 0 
	returnData['2P'] = 0 
	returnData['2PA'] = 0 
	returnData['2P%'] = 0 
	returnData['3P'] = 0 
	returnData['3PA'] = 0 
	returnData['3P%'] = 0 
	returnData['FT'] = 0 
	returnData['FTA'] = 0 
	returnData['FT%'] = 0 
	returnData['PTS'] = 0 
	returnData['ORB%'] = 0
	returnData['TRB%'] = 0 
	returnData['AST%'] = 0 
	returnData['STL%'] = 0 
	returnData['BLK%'] = 0 
	returnData['TOV%'] = 0 


	for index, row in data.iterrows():

		if row['Home'] == "@":
			returnData['Home'] += 0
		else:
			returnData['Home'] += 1



		returnData['ORtg'] += checkGood(row['ORtg'])
		returnData['FTr'] += checkGood(row['FTr'])
		returnData['3PAr'] += checkGood(row['3PAr'])
		returnData['TS%'] += checkGood(row['TS%'])
		returnData['eFG%'] += checkGood(row['eFG%'])
		returnData['FT/FGA'] += checkGood(row['FT/FGA'])
		returnData['FG'] += checkGood(row['FG'])
		returnData['FGA'] += checkGood(row['FGA'])
		returnData['FG%'] += checkGood(row['FG%'])
		returnData['2P'] += checkGood(row['2P'])
		returnData['2PA'] += checkGood(row['2PA'])
		returnData['2P%'] += checkGood(row['2P%'])
		returnData['3P'] += checkGood(row['3P'])
		returnData['3PA'] += checkGood(row['3PA'])
		returnData['3P%'] += checkGood(row['3P%'])
		returnData['FT'] += checkGood(row['FT'])
		returnData['FTA'] += checkGood(row['FTA'])
		returnData['FT%'] += checkGood(row['FT%'])
		returnData['PTS'] += checkGood(row['PTS'])
		returnData['ORB%'] += checkGood(row['ORB%'])
		returnData['TRB%'] += checkGood(row['TRB%'])
		returnData['AST%'] += checkGood(row['AST%'])
		returnData['STL%'] += checkGood(row['STL%'])
		returnData['BLK%'] += checkGood(row['BLK%'])
		returnData['TOV%'] += checkGood(row['TOV%'])

		gameCount = gameCount + 1

	for feat in returnData: 	
		returnData[feat] /= gameCount

	return returnData


def checkGood(val):
	
	if val == "":
		return 0
	else:
		return val

def checkNaN(val):
	
	if math.isnan(val):
		return 0
	else:
		return val


def createTest(player, game, var, features):

	trainData = pd.read_csv('testData/' + var  "/" + player + '.csv')

	newDataSheet = []

	for index, row in trainData.iterrows():

		if (row['Game'] == game):

			newDataSheet.append(row)
			break

	with open('test/' + var + '/' +  str(player) + game + '.csv', mode='w') as playerFile:
		playerWriter = csv.writer(playerFile, delimiter=',')	
		playerWriter.writerow(features)
		playerWriter.writerow(newDataSheet)
