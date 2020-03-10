#import necessary modules
import csv
nbaTeams=["New York Knicks","Brooklyn Nets","Sacramento Kings"]
with open('/Users/bryancamilo/Desktop/teamStats.csv','rt')as f:
	data = csv.reader(f)
	for row in data:
		if row[1] == nbaTeams[0]:
			print(row)
		else:
			print("Not the New York Knicks")