from mrjob.job import MRJob
from sentClassifier import sentClassify
# from mrjob.protocol import JSONValueProtocol,RawValueProtocol

class ObidroidReview(MRJob):
	# INPUT_PROTOCOL = RawValueProtocol



	def sentiment(review): #helper
		return review

	def wordcount(review): #helper
		return review
		
	def reviewLength(review): #helper
		review = review.split(" ")
		return len(review)


	def getRecord(self, _, record): #Mapper 1
		record = record.split(',')
		def getFeatures(rev):
			sent = sentClassify(rev)
			
			return sent 

		features = getFeatures(record[1])
		appid = record[0]
		yield appid, features

	
	def performAction(self,appid,appfeature): #Reducer 1
		yield appid, list(appfeature)
	
	def steps(self):
		return [
            self.mr(mapper=self.getRecord, reducer=self.performAction)
        ]

if __name__ == '__main__':
    
    ObidroidReview.run()
