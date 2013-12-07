import csv
import os

unfair_apps=[]
with open("../applabel/allapps.csv") as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		if row[0].lower()=="unfair":
			unfair_apps.append(row)

print unfair_apps
with open("../docs/malapps.txt","a") as outfile:
	for app in unfair_apps:
		outfile.write(app+"\n")

