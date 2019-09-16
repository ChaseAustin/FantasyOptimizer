# program to get num of unique features in data set

import csv
import os


features = []

nonFeatures = ["Rk", "Player", "Pos", "Tm"]

for file in os.listdir("data/18-19"):

	print("reading " + file + "\n")
	
	with open("data/18-19/" + file, encoding="ISO-8859-1") as csv_file:
		reader = csv.reader(csv_file, delimiter=",")
		for row in reader:
			for column in row:
				if column not in nonFeatures:
					if column not in features:
						features.append(column)
			break

print(str(len(features)) + " features")

for feat in features:
	print(feat)
	