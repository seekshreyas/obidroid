from mrjob.job import MRJob
from sentClassifier import sentClassify
from cPickle import load
import re
import nltk
# import pattern
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import sys
# import simplejson


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

		revPosTokens = nltk.pos_tag(nltk.word_tokenize(rev))

		for _, pos in revPosTokens:
			if pos == 'JJ' or pos == 'VBP':
				revAdjCount += 1


		# Sentiment Classifiers:
		revSentAgg = sentClassify(rev)
		# overall production sentiment classifier
		blob = TextBlob(rev, analyzer=NaiveBayesAnalyzer())
		blobSent = blob.sentiment

		# print blobSent

		if blobSent[0] == 'pos':
			revSent = 1 * blobSent[1]
		elif blobSent[0] == 'neg':
			revSent = -1 * blobSent[2]
		else:
			revSent = 0




		return [
			revCharLength,
			revWordsLength,
			revUniqueWordLength,
			revCapCount,
			revExclaimCount,
			revAdjCount,
			revSentAgg,
			revSent
		]





	def getRecord(self, _, record): #Mapper 1
		record = record.split(',')

		idpattern = re.compile('(\w+\.+\w+[(\.+)(\w+)]+)')

		reviewid = record[0]
		appid = idpattern.split(record[1])


		features = ObidroidReview.getFeatures(record[2])

		features.append(appid[1])

		sys.stderr.write("MAPPER INPUT: ({0},{1})\n".format(reviewid,features))

		yield reviewid, features


	def performAction(self,revid,revfeatures): #Reducer 1
		sys.stderr.write("MAPPER INPUT: ({0},{1})\n".format(revid,revfeatures))
		yield revid, list(revfeatures)




	def steps(self):
		return [
            self.mr(mapper=self.getRecord, reducer=self.performAction)
        ]



if __name__ == '__main__':
    ObidroidReview.run()
