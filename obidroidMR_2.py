from mrjob.job import MRJob
# from sentClassifier import sentClassify
from cPickle import load
import re
import nltk
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures as BAM
from nltk.metrics import TrigramAssocMeasures as TAM
from nltk import FreqDist



class ObidroidReview(MRJob):


	@staticmethod
	# def featureExtractor(sentStr):

	# 	def getWordsFromSent(sent):
	# 	    words = [w.lower() for w in word_tokenize(sent) if w not in stopwords.words('english') ]

	# 	    return words


	# 	def getTaggedSents(sentWords):
	# 		return nltk.pos_tag(sentWords)


	# 	def getCharlesScore(upperCount, negativeWordCount, positiveWordCount, bigramBeginWithNotCount):
	# 		new_vote = 0  - upperCount - negativeWordCount + positiveWordCount + 2 * bigramBeginWithNotCount

	# 		return new_vote


	# 	# feature extraction methods
	# 	def getReviewDict(sent):

	# 		# print parsedata[:5]
	# 		contain_features = {}
	# 		global top_words
	# 		for word in top_words:
	# 			contain_features['contains(%s)' % (word)] = (word in set(sent))

	# 		return contain_features



	# 	def getAdjOpinionScore(tagSent, opinioncorpus):
	# 	    score = 0
	# 	    for (word, tag) in tagSent:

	# 	        if tag == 'JJ' or tag == 'ADV' or tag == 'VBG' or tag == 'RB' or tag == 'VBZ' or tag == 'JJS':

	# 	            if word in opinioncorpus['positive']:

	# 	                score += 1
	# 	            if word in opinioncorpus['negative']:
	# 	                score -= 1

	# 	    return score




	# 	##
	# 	## Charles' Features
	# 	##

	# 	def getUpperCount(sent):
	# 	    uppercase_meaningless_words = ["A", "I", "IPOD", "USB", "MP3", "CD", "FM", "GB", "PC", "LCD", "MP-3", "WMA", "WMP",
	# 	                               "AC/DC", "PDA", "PXC250", "XP", "LED", "AC", "AGK", "DVD", "SD", "MB"]
	# 	    upperCount = 0
	# 	    for word in sent.split(" "):
	# 	        word = word.replace(".","").replace(",","").replace("!","").replace("?","").replace("##","").replace("(","").replace(")","").replace("**","")
	# 	        for letter in word:
	# 	            if letter.isdigit():
	# 	                word = word.replace(letter, "")
	# 	            else:
	# 	                break
	# 	        if word.isupper() and len(word) != 1 and not word in uppercase_meaningless_words:
	# 	            upperCount += 1
	# 	    return upperCount



	# 	def getPostiveWordCount(sent):
	# 	    positive_keywords = ["good", "happy", "love", "great", "reasonable", "glad", "simple", "outstanding", "easy",
	# 	                     "wonderful", "cool", "remarkably", "remarkable", "enjoy", "nice", "thoughtful", "pretty",
	# 	                     "responsive", "comforatable", "favorite", "desire", "best", "solid", "cool", "impressed",
	# 	                     "sleek", "appealing", "rocks", "blazing", "amazing", "plus", "blessing", "awesome", "loved",
	# 	                        "enjoyed", "desired", "impressive", "impress", "rocked", "bless", "positive", "fabulous"]
	# 	    postiveCount = 0
	# 	    for word in sent.split(" "):
	# 	        word = word.replace(".","").replace(",","").replace("!","").replace("?","").replace("##","").replace("(","").replace(")","").replace("**","")
	# 	        if word.lower() in positive_keywords:
	# 	            postiveCount += 1
	# 	    return postiveCount



	# 	def getNegativeWordCount(sent):
	# 	    negative_keywords = ["bad", "sad", "don't", "could not", "crappy", "unfortunately", "remove", "why", "poor",
	# 	                     "bothersome", "terrible", "although", "complaints", "outrageous", "isn't", "poorly",
	# 	                     "drawback", "annoying", "against", "irritating", "wouldn't", "won't", "wasn't", "couldn't",
	# 	                     "awful", "didn't", "hasn't", "difficult", "hate", "incorrect", "junk", "trash", "removed",
	# 	                         "complain", "complained", "hated", "negative"]
	# 	    negativeCount = 0
	# 	    for word in sent.split(" "):
	# 	        word = word.replace(".","").replace(",","").replace("!","").replace("?","").replace("##","").replace("(","").replace(")","").replace("**","")
	# 	        if word.lower() in negative_keywords:
	# 	            negativeCount += 1
	# 	    return negativeCount



	# 	def getBigramBeginWithNotCount(sent):
	# 	    negative_keywords = ["bad", "sad", "don't", "could not", "crappy", "unfortunately", "remove", "why", "poor",
	# 	                     "bothersome", "terrible", "although", "complaints", "outrageous", "isn't", "poorly",
	# 	                     "drawback", "annoying", "against", "irritating", "wouldn't", "won't", "wasn't", "couldn't",
	# 	                     "awful", "didn't", "hasn't", "difficult", "hate", "incorrect", "junk", "trash", "removed",
	# 	                         "complain", "complained", "hated", "negative"]
	# 	    bigramPostiveCount = 0

	# 	    for i, word in enumerate(word_tokenize(sent)):
	# 	        if word.lower() == "not":
	# 	            if word_tokenize(sent)[i + 1] in negative_keywords : # e.g. NOT bad
	# 	                bigramPostiveCount += 1
	# 	            if i < len(word_tokenize(sent)) - 2 and word_tokenize(sent)[i + 2] in negative_keywords: # e.g. NOT too bad
	# 	                bigramPostiveCount += 1
	# 	            else:                                                # e.g. NOT good
	# 	                bigramPostiveCount -= 1
	# 	    return bigramPostiveCount



	# 	def getUnigramWordFeatures(sent, words):
	# 	    return dict(('contains("%s")' % word, True) for word in words)



	# 	def getBigramWordFeatures(sent, words, score_fn=BAM.chi_sq, n=2000):


	# 	    filtered_words = [w for w in words if w != '.' and w != '?' and w != ')' and w != '(' and w != '-']

	# 	    bigram_finder = BigramCollocationFinder.from_words(filtered_words)
	# 	    # score = bigram_finder.score_ngrams(BAM.jaccard)

	# 	    bigrams = bigram_finder.nbest(score_fn, n)


	# 	    return dict((bg, True) for bg in chain(filtered_words, bigrams))








	# 	def getSentOverallOpinion(sent, words, opinioncorpus):


	# 	    score = 0.0

	# 	    if len(words) != 0:
	# 	        for w in words:
	# 	            if w in opinioncorpus['positive']:
	# 	                score += 1.0
	# 	            elif w in opinioncorpus['negative']:
	# 	                score -= 1.0

	# 	        return score
	# 	    else:
	# 	        return score




	# 	def getCharCount(sent):
	# 	    return int(len(sent))


	# 	def getWordCount(sent):
	# 	    return len(word_tokenize(sent))

	# 	def getCommaCount(sent):
	# 	    commaRegEx = re.compile(',')

	# 	    numoccur = len([a.start() for a in commaRegEx.finditer(sent)])

	# 	    return numoccur

	# 	def getExclaimCount(sent):
	# 	    exclaimRegEx = re.compile('!')

	# 	    numoccur = len([a.start() for a in exclaimRegEx.finditer(sent)])

	# 	    return numoccur

	# 	def getSemicolonCount(sent):
	# 	    semicolonRegEx = re.compile(';')

	# 	    numoccur = len([a.start() for a in semicolonRegEx.finditer(sent)])

	# 	    return numoccur

	# 	def getWhiteSpaceCount(sent):
	# 	    whitespaceRegEx = re.compile(' ')

	# 	    numoccur = len([a.start() for a in whitespaceRegEx.finditer(sent)])

	# 	    return numoccur

	# 	def getUpperCount(sent):
	# 	    numoccur=0
	# 	    for i in range(len(sent)):
	# 	        i=str(i)
	# 	        if i.isupper==True:
	# 	            numoccur+=1
	# 	    return numoccur

	# 	def getDigitCount(sent):
	# 	    numoccur=0
	# 	    for i in range(len(sent)):
	# 	        i=str(i)
	# 	        if i.isdigit==True:
	# 	            numoccur+=1
	# 	    return numoccur

	# 	def getTabCount(sent):
	# 	    tabRegEx = re.compile('    ')

	# 	    numoccur = len([a.start() for a in tabRegEx.finditer(sent)])

	# 	    return numoccur

	# 	def getPercentCount(sent):
	# 	    numoccur=0
	# 	    for i in sent:
	# 	        i=str(i)
	# 	        if i== '%':
	# 	            numoccur+=1
	# 	    return numoccur

	# 	def getEtcCount(sent):
	# 	    numoccur=0
	# 	    for i in sent:
	# 	        i=str(i)
	# 	        if i== 'etc.':
	# 	            numoccur+=1
	# 	    return numoccur

	# 	def getDollarCount(sent):
	# 	    numoccur=0
	# 	    for i in sent:
	# 	        i=str(i)
	# 	        if i== '$':
	# 	            numoccur+=1
	# 	    return numoccur

	# 	def getAvgWordLen(sent):
	# 	    avg, total = 0,0
	# 	    sent=sent.split(" ")
	# 	    ln= len(sent)
	# 	    if ln>0:
	# 	        for i in sent:
	# 	            i=str(i)
	# 	            lnword=len(i)
	# 	            total=total+lnword
	# 	        avg=total/ln
	# 	    return avg

	# 	def getWordLen6(sent):
	# 	    numoccur = 0
	# 	    for i in sent:
	# 	        if len(i)>= 6:
	# 	            numoccur+=1
	# 	    return numoccur

	# 	def getUniqueWords(sent):
	# 	    word=[]
	# 	    wunique=0
	# 	    for item in sent:
	# 	        if item not in word:
	# 	            wunique+=1
	# 	    return wunique

	# 	def getCountJJ(sent):
	# 	    countjj= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="JJ":
	# 	            countjj+=1
	# 	    return countjj

	# 	def getCountCC(sent):
	# 	    countcc= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="CC":
	# 	            countcc+=1
	# 	    return countcc

	# 	def getCountIN(sent):
	# 	    countin= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="IN":
	# 	            countin+=1
	# 	    return countin

	# 	def getCountRB(sent):
	# 	    countrb= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="RB":
	# 	            countrb+=1
	# 	    return countrb

	# 	def getCountPRP(sent):
	# 	    countprp= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="PRP":
	# 	            countprp+=1
	# 	    return countprp

	# 	def getCountTO(sent):
	# 	    countto= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="TO":
	# 	            countto+=1
	# 	    return countto

	# 	def getCountVBD(sent):
	# 	    countvbd= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="VBD":
	# 	            countvbd+=1
	# 	    return countvbd


	# 	def getCountJJR(sent):
	# 	    countjjr= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="JJR":
	# 	            countjjr+=1
	# 	    return countjjr

	# 	def getCountNN(sent):
	# 	    countnn= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="NN":
	# 	            countnn+=1
	# 	    return countnn

	# 	def getCountNNS(sent):
	# 	    countnns= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="NNS":
	# 	            countnns+=1
	# 	    return countnns

	# 	def getCountNNP(sent):
	# 	    countnnp= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="NNP":
	# 	            countnnp+=1
	# 	    return countnnp

	# 	def getCountRBR(sent):
	# 	    countrbr= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="RBR":
	# 	            countrbr+=1
	# 	    return countrbr

	# 	def getCountVB(sent):
	# 	    countvb= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="VB":
	# 	            countvb+=1
	# 	    return countvb

	# 	def getCountVBP(sent):
	# 	    countvbp= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="VBP":
	# 	            countvbp+=1
	# 	    return countvbp

	# 	def getCountVBZ(sent):
	# 	    countvbz= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="VBZ":
	# 	            countvbz+=1
	# 	    return countvbz

	# 	def getCountVBG(sent):
	# 	    countvbg= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="VBG":
	# 	            countvbg+=1
	# 	    return countvbg

	# 	def getCountVBN(sent):
	# 	    countvbn= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="VBN":
	# 	            countvbn+=1
	# 	    return countvbn

	# 	def getCountMD(sent):
	# 	    countmd= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="MD":
	# 	            countmd+=1
	# 	    return countmd

	# 	def getCountWDT(sent):
	# 	    countwdt= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="WDT":
	# 	            countwdt+=1
	# 	    return countwdt

	# 	def getCountPRPA(sent):
	# 	    countprpa= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(sent)):
	# 	        if text[i][1]=="PRP$":
	# 	            countprpa+=1
	# 	    return countprpa

	# 	def getCountJN(sent):
	# 	    countjn= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(text)):
	# 	        if text[i-1][1]=="JJ" and text[i][1] in ["NN","NNS"]: countjn+=1
	# 	    return countjn

	# 	def getCountRJ(sent):
	# 	    countrj= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(text)):
	# 	        if text[i-1][1] in ["RB","RBR","RBS"] and text[i][1]=="JJ": countrj+=1
	# 	    return countrj

	# 	def getCountJJC(sent):
	# 	    countjjc= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(text)):
	# 	        if text[i-1][1]=="JJ" and text[i][1]=="JJ": countjjc +=1
	# 	    return countjjc

	# 	def getCountNJ(sent):
	# 	    countnj= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(text)):
	# 	        if text[i-1][1]=="NNS" and text[i][1]=="jj": countnj+=1
	# 	    return countnj

	# 	def getCountRV(sent):
	# 	    countrv= 0
	# 	    sent= nltk.word_tokenize(sent)
	# 	    text=nltk.pos_tag(sent)
	# 	    for i in range(len(text)):
	# 	        if text[i-1][1]==["RR","RBS","RBR"] and text[i][1]==["VB", "VBN", "VBD", "VBG"]: countrv+=1
	# 	    return countrv


	# 	def getAfinn(sent):
	# 	    w=str(sent)
	# 	    w=w.lower()
	# 	    w=w.split()
	# 	    total, avg=0,0
	# 	    ln = len(w)
	# 	    if ln>0:
	# 	        for item in range(len(w)):
	# 	            for i in range(len(dc)):
	# 	                if dc.keys()[i]==w[item]:
	# 	                    temp = int(dc.values()[i])
	# 	                    total += temp
	# 	        avg=total/ln
	# 	        # print avg
	# 	    return avg


	# 	def pmiScore(sent):
	# 	    sent = nltk.word_tokenize(sent)
	# 	    x=nltk.pos_tag(sent)

	# 	    # print x

	# 	    countnn, countjj, countnj=0,0,0
	# 	    pnn, pjj, pjn=0,0,0
	# 	    for i in range(len(x)):
	# 	        if x[i][1] in ["NN", "NNP"]:countnn+=1
	# 	        if x[i][1]=="JJ":countjj+=1

	# 	    for i in range(len(x)):
	# 	        if str(x[i-1][1])in ["NN","NNP", "JJ"] and x[i][1]==["JJ","RB","NN","VB", "VBP", "VBD","VBR", "VBG","VBZ"]: countnj+=1
	# 	    if (len(sent)-1)>0:
	# 	        pnn=countnn/len(sent)
	# 	        pjj=countjj/len(sent)
	# 	        pnj=countnj/(len(sent)-1)

	# 	        # print pnn, pjj, pnj

	# 	        if pnj>0:
	# 	            pmi= math.log(pnj/(pnn*pjj))
	# 	            return pmi





	# 	def parseOpinionLexicon():

	# 	    # print os.getcwd()
	# 	    opinionLexPath = 'lexicon/opinionwords/'

	# 	    posfileObj = open(opinionLexPath + 'positive-words.txt')
	# 	    negfileObj = open(opinionLexPath + 'negative-words.txt')

	# 	    lexWords = {}
	# 	    lexWords['positive'] = [l[:-2] for l in posfileObj if not l.startswith(';') and l[:-2] is not '']
	# 	    lexWords['negative'] = [l[:-2] for l in negfileObj if not l.startswith(';') and l[:-2] is not '']

	# 	    posfileObj.close()
	# 	    negfileObj.close()

	# 	    return lexWords



	# sentwords = getWordsFromSent(sentStr)
	# taggedSent = getTaggedSents(sentwords)
	# # opinionWords = parseOpinionLexicon()


	# featList = {}

 #    # featList['charCount']       = getCharCount(sentStr)
	# featList['wordCount']       = getWordCount(sentStr)
	# # # featList['commaCount']      = getCommaCount(sentStr)
	# # # featList['semicolonCount']  = getSemicolonCount(sentStr)
	# # # featList['uppercount']      = getUpperCount(sentStr)
	# featList['digitcount']      = getDigitCount(sentStr)
	# featList['exclaimCount']    = getExclaimCount(sentStr)

	# featList["countJJ"]=getCountJJ(sentStr)
	# featList["countCC"]=getCountCC(sentStr)

	# featList["countVBD"]=getCountVBD(sentStr)

	# featList["countRB"]=getCountRB(sentStr)
	# featList["countVBG"]=getCountVBG(sentStr)
	# featList["countVBZ"]=getCountVBZ(sentStr)




	# #Charles' Features
	# 	featList['upperCount']   = getUpperCount(sentStr)
	# featList['postiveWordCount'] = getPostiveWordCount(sentStr)
	# featList['negativeWordCount'] = getNegativeWordCount(sentStr)
	# featList['bigramBeginWithNotCount'] = getBigramBeginWithNotCount(sentStr)
	# featList['charlesScore'] = getCharlesScore(
	# featList['upperCount'],
	# featList['postiveWordCount'],
	# featList['negativeWordCount'],
	# featList['bigramBeginWithNotCount'])





	# featList.update(getUnigramWordFeatures(sentStr, sentwords))
	# featList.update(getBigramWordFeatures(sentStr, sentwords))
	# return featList






    ## Sentiment Classifier
	# def tokenizeReviewsBySentence(revStr):
	# 	return nltk.tokenize.sent_tokenize(revStr)




	# def getReviewSentiment(tknRevs, classifier):
	# 	revAggSentiment = 0

	# 	for sent in tknRevs:
	# 		sent = unicode(sent.strip())

	# 		featdata = extractor.featureExtractor(sent)

	# 		cl= classifier.classify(featdata)

	# 		if cl == 'pos':
	# 			label = 1
	# 		elif cl == 'neutral':
	# 			label = 0
	# 		else:
	# 			label = -1

	#         revAggSentiment += label


	# 	return revAggSentiment




	# def sentClassify(sentStr):
	#     """
	#     Given a sentence string, classify the sentence
	#     """

	#     tokenizedReviews = tokenizeReviewsBySentence(sentStr)

	#     ## load the classifier pickle
	#     fObj = open('mySentClassifier.pickle')
	#     cl = load(fObj)
	#     fObj.close()

	#     revSent = getReviewSentiment(tokenizedReviews, cl)

	#     return revSent


















































































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


		## Sentiment Classifiers:
		# revSentAgg = sentClassify(rev)
		## overall production sentiment classifier
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

		appid = idpattern.split(record[0])


		features = ObidroidReview.getFeatures(record[1])


		yield appid[1], features


	def performAction(self,appid,appfeature): #Reducer 1
		yield appid, list(appfeature)




	def steps(self):
		return [
            self.mr(mapper=self.getRecord, reducer=self.performAction)
        ]



if __name__ == '__main__':
    ObidroidReview.run()
