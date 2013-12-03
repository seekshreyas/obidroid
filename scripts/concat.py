import json,os

#ie mergeAllFiles('/Users/Artemis/Desktop/gpstore')

def mergeAllFiles(directory):
	"""Searches through current directory and merges 
	the files that contain app info with the corresponding
	reviews from the matching "reviews.json" file.
	"""
	allDirFiles = os.listdir(directory)
	for jsonFile in allDirFiles:
		if "_all.json" in jsonFile:
			reviewFile = jsonFile[:-8] + "reviews.json"
			mergeJson(jsonFile,reviewFile,directory)
	return 

def mergeJson(allJson,reviewJson,directory):
	"""Modifies the json file containing the 
	main information about the apps to also include 
	the information contained in the reviews"""
	results = []

	allFile = json.load(open(directory + "/" + allJson))
	reviewFile = json.load(open(directory + "/" + reviewJson))

	for app in zip(allFile,reviewFile):
		for field in app[1].keys():
			app[0][field] = app[1][field]
		results +=[app[0]]

	with open(directory + "/" + allJson[:-8]+"merged.json",'w') as f:
		json.dump(results,f,sort_keys=True)

	print "Results written to",directory+"/"+allJson[:-8]+"merged.json"
	return



