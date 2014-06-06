from mrjob.job import MRJob
# from sentClassifier import sentClassify
# from cPickle import load
import re
# import nltk
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import sys
# import math


class ObidroidReview(MRJob):
	# INPUT_PROTOCOL = RawValueProtocol

	@staticmethod
	def getFeatures(rev):

		wordpattern = re.compile('\w+')
		capspattern = re.compile('([A-Z])+\w')
		exclaimpattern = re.compile('!')

		rev = rev.decode('utf-8', 'ignore')


		revCharLength = len(rev)

		words = wordpattern.findall(rev)
		revWordsLength = len(words)

		revUniqueWordLength = len(set(words))

		revCapCount = len(capspattern.findall(rev))

		revExclaimCount = len(exclaimpattern.findall(rev))

		revAdjCount = 0

		# revPosTokens = nltk.pos_tag(nltk.word_tokenize(rev))
		revBlob = TextBlob(rev)
		revPosTokens = revBlob.tags

		for w, pos in revPosTokens:
			if pos == 'JJ' or pos == 'VBP':
				revAdjCount += 1


		# Sentiment Classifiers:
		# revSentAgg = sentClassify(rev)

		# overall production sentiment classifier
		# blob = TextBlob(rev, analyzer=NaiveBayesAnalyzer())
		# blobSent = blob.sentiment



		# print blobSent

		# if blobSent[0] == 'pos':
		# 	revSent = 1 * blobSent[1]
		# elif blobSent[0] == 'neg':
		# 	revSent = -1 * blobSent[2]
		# else:
		# 	revSent = 0


		# revSent = round(revSent, 4)

		return [
			revCharLength,
			revWordsLength,
			revUniqueWordLength,
			revCapCount,
			revAdjCount,
			# revSentAgg,
			# revSent,
			revExclaimCount
		]





	def getRecord(self, _, record): #Mapper 1
		record = record.split(',')

		idpattern = re.compile('(\w+\.+\w+[(\.+)(\w+)]+)')

		reviewid = record[0]
		appidmatches = idpattern.split(record[1])
		appid = appidmatches[1]


		features = ObidroidReview.getFeatures(record[2])

		features.append(reviewid)

		sys.stderr.write("MAPPER OUTPUT: ({0},{1})\n".format(appid,features))

		yield appid, features


	def performAction(self,appid,revfeatures): #Reducer 1
		sys.stderr.write("REDUCER INPUT: ({0},{1})\n".format(appid,revfeatures))
		yield appid, list(revfeatures)




	def steps(self):
		return [
            self.mr(mapper=self.getRecord, reducer=self.performAction)
        ]



if __name__ == '__main__':
    ObidroidReview.run()
