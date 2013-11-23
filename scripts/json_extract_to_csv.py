#json extract to csv
import json
import csv

#Get extracted JSON data
with open("../exports/alldata.json","r") as f:
	json_export=json.load(f)

# print json_export[0]["name"]

#Get subset for to test process - disable later
json_export=json_export[:10]
# print json_export[0].keys()

def average_rating(rating_list):
	total=0
	all_ratings=0
	for rank in rating_list:
		rating=int(rank[0].strip())
		num_ratings=rating*rank[1]
		weight=rating*num_ratings
		all_ratings+=num_ratings
		total+=weight
	return total/all_ratings 




with open("../apps_to_label_(csv)/allapps.csv","wb") as csvfile:
	writeObj=csv.writer(csvfile)
	
	#write header row to file
	header=["label (fair/unfiar)"
			   'name',
			   'id',
			   'category',
			   'rating',
			   'review',
			   'num_5_stars',
			   'num_4_stars', 
			   'num_3_stars',
			   'num_2_stars',
			   'num_1_stars',
			   'screenCount',
			   'description', 
			   'company', 
			   'moreFromDev', 
			   'contentRating', 
			   'price',  
			   'version', 
			   'install', 
			   'totalReviewers', 
			   'size', 
			   'similar']
	writeObj.writerow(header)


	for app in json_export:
		#fist iteration through apps - just reformat
		for attr in app:

			# attributes that have lists and are not reviews and rating are condensed.
			if attr != "reviews" and attr != "rating":
				
				#Make sure attribute values that are lists 
				#display as simcolon delimited strings
				if type(app[attr]) is list:
					# print app[attr]
					x= ';'.join(app[attr])
					# print x
					app[attr]=x

			#reviews are lists of title and body- this converts them to one string
			if attr=="reviews":
				# print attr
				for i in range(len(app[attr])):
					app[attr][i]=";".join(app[attr][i])
			# if attr =="rating":
			# 	while len(attr)!=5:
			# 		if attr[4][0]!=4:
		#second iteration to write to csv
		for attr in app:
			#write row for every review
			if attr=="reviews":
				for i in range(len(attr)):
					try:
						row=["",
							 app['name'],
							 app["id"],
							 app['category'],
							 average_rating(app['rating']),
							 app['reviews'][i],
							 app['rating'][0][1],
							 app['rating'][1][1],
							 app['rating'][2][1],
							 app['rating'][3][1],
							 app['rating'][4][1],
							 app['screenCount'],
							 app['description'],
							 app['company'],
							 app['moreFromDev'],
							 app['contentRating'],
							 app['price'],
							 app['version'],
							 app['install'],
							 app['totalReviewers'],
							 app['size'],
							 app['similar']]
					except:
							print app['id']+" had an error"
							print app['rating']
					for i in range(len(row)):
						try:row[i]=row[i].encode('ascii','ignore')
						except:pass
					writeObj.writerow(row)



