from mrjob.job import MRJob
from sentClassifier import sentClassify
import os
from cPickle import load
import re



class ObidroidReview(MRJob):
	# INPUT_PROTOCOL = RawValueProtocol

	@staticmethod
	def getFeatures(rev):
		revsent = sentClassify(rev)
		revCharLength = len(rev)

		wordpattern = re.compile('\w+')

		words = wordpattern.findall(rev)

		revWordsLength = len(words)

		return [revsent, revCharLength, revWordsLength]




	def getRecord(self, _, record): #Mapper 1
		record = record.split(',')

		appid = record[0]
		features = ObidroidReview.getFeatures(record[1])


		yield appid, features


	def performAction(self,appid,appfeature): #Reducer 1
		yield appid, list(appfeature)




	def steps(self):
		return [
            self.mr(mapper=self.getRecord, reducer=self.performAction)
        ]



if __name__ == '__main__':
    ObidroidReview.run()
