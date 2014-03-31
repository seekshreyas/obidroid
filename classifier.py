#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Classifier
==========
After Feature Extraction, that returns a data of the format
[(filename, linenum, vote, sentence, feat1, feat2, ...)]
"""

from __future__ import division
from optparse import OptionParser
import json
from pprint import pprint
import random
import math
import nltk
from cPickle import dump
from cPickle import load
import parser
import extractor
from os import listdir
from decimal import Decimal
from collections import OrderedDict
from collections import Counter
import pdb
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import *
# from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures as BAM
from nltk.metrics import TrigramAssocMeasures as TAM
from itertools import chain
# from nltk.classify import apply_features


def getUserInput():
    optionparser = OptionParser()

    optionparser.add_option('-i', '--input', dest='inputfile')
    optionparser.add_option('-d', '--dir', dest='directory')


    (option, args) = optionparser.parse_args()

    if not option.directory:
        return optionparser.error('html file input not provided.\n Usage: --url="path.to.appurl"')

    return { 'file' : option.inputfile, 'dir' : option.directory }



def fileExtractor(f):
    fObj = open(f)
    data = json.load(fObj)

    fObj.close()

    return data


def featureAggregator(extract):
    outputdata = []

    for app in extract:
        outputdata.append(featureExtractor(app))

    return outputdata



def tokenizeReviewsBySentence(reviews):
    rev_tokenized = list()
    for rev in reviews:
        rev_tokenized.append(nltk.tokenize.sent_tokenize(rev[1]))
    return rev_tokenized

def posReviewsBySentence(tokenizedReviews):
    pos_sents = list()
    for review in tokenizedReviews:
        for sent in review:
            pos_sents.append(nltk.pos_tag(nltk.word_tokenize(sent)))
    return pos_sents



def getAllReviewsAsString(app):
    revStr = ''
    for rev in app['reviews']:
        # combine title and review sentence
        revStr += rev[0] + rev[1]

    return revStr


def featureExtractor(app):
    featDict = {}
    revStr = getAllReviewsAsString(app)
    revWords = [w.lower()
                    for w in word_tokenize(revStr)
                        if w not in stopwords.words('english') ]

    tokenizedReviews = tokenizeReviewsBySentence(app['reviews'])
    posReviews = posReviewsBySentence(tokenizedReviews)



    fObj = open('mySentClassifier.pickle')
    cl = load(fObj)
    fObj.close()



    featDict['price'] = getAppPrice(app)
    featDict['revlength'] = getReviewLength(app)
    # featDict['1starrating'] = getOneStarRating(app)
    # featDict['2starrating'] = getTwoStarRating(app)
    # featDict['3starRating'] = getThreeStarRating(app)
    # featDict['4starRating'] = getFourStarRating(app)
    # featDict['5starRating'] = getFiveStarRating(app)
    featDict['avgRating'] = getAverageRating(app)
    featDict['hasPrivacy'] = getPrivacyState(app)
    featDict['revSent'] = getReviewSentiment(app, tokenizedReviews, cl)
    featDict['hasDeveloperEmail'] = getDeveloperEmailState(app)
    featDict['hasDeveloperWebsite'] = getDeveloperWebsiteState(app)
    featDict['countMultipleApps'] = getDeveloperHasMultipleApps(app)
    featDict['installs'] = getInstallRange(app)
    featDict['exclamationCount'] = getExclamationCount(app)
    featDict['countCapital'] = getCountCapitals(revStr)
    featDict['adjectiveCount'] = getAdjectiveCount(posReviews)
    featDict['positiveWordCount'] = getPostiveWordCount(revStr)
    featDict['negativeWordCount'] = getNegativeWordCount(revStr)

    # featDict.update(getUnigramWordFeatures(revWords))
    # featDict.update(getBigramWordFeatures(revWords))
    # featDict.update(getTrigramWordFeatures(revWords))



    return { 'appFeatures': featDict, 'appName': app['name'] }

def getAdjectiveCount(pos_revs):
    adj_counter = 0
    #pdb.set_trace()
    for pos_sent in pos_revs:
        adj_counter += Counter(tag for word, tag in pos_sent)['JJ']

    return int(adj_counter)






def getCountCapitals(revStr):
    capitalWords = [w for w in nltk.word_tokenize(revStr) if w.isupper()]

    return len(capitalWords)



def getPostiveWordCount(sent):
    positive_keywords = ["good", "happy", "love", "great", "reasonable", "glad", "simple", "outstanding", "easy",
                     "wonderful", "cool", "remarkably", "remarkable", "enjoy", "nice", "thoughtful", "pretty",
                     "responsive", "comforatable", "favorite", "desire", "best", "solid", "cool", "impressed",
                     "sleek", "appealing", "rocks", "blazing", "amazing", "plus", "blessing", "awesome", "loved",
                        "enjoyed", "desired", "impressive", "impress", "rocked", "bless", "positive", "fabulous"]
    postiveCount = 0
    for word in sent.split(" "):
        word = word.replace(".","").replace(",","").replace("!","").replace("?","").replace("##","").replace("(","").replace(")","").replace("**","")
        if word.lower() in positive_keywords:
            postiveCount += 1
    return postiveCount



def getNegativeWordCount(sent):
    negative_keywords = ["bad", "sad", "don't", "could not", "crappy", "unfortunately", "remove", "why", "poor",
                     "bothersome", "terrible", "although", "complaints", "outrageous", "isn't", "poorly",
                     "drawback", "annoying", "against", "irritating", "wouldn't", "won't", "wasn't", "couldn't",
                     "awful", "didn't", "hasn't", "difficult", "hate", "incorrect", "junk", "trash", "removed",
                         "complain", "complained", "hated", "negative"]
    negativeCount = 0
    for word in sent.split(" "):
        word = word.replace(".","").replace(",","").replace("!","").replace("?","").replace("##","").replace("(","").replace(")","").replace("**","")
        if word.lower() in negative_keywords:
            negativeCount += 1
    return negativeCount




def getUnigramWordFeatures(words):
    """
    Unigrams of the apps reviews
    """
    malIndicatorWords = ['spam', 'virus', 'viruses' 'permissions', 'security',
        'spying', 'access', 'warning', 'facebook', 'contacts', 'fake', 'permission',
        'beware', 'lies', 'liar', 'why', 'age']
    return dict(('contains("%s")' % word, True) for word in words if word in malIndicatorWords)



def getBigramWordFeatures(words):
    """
    Get Relevant Bigrams
    """

    filtered_words = [w for w in words if w != '.' and w != '?' and w != ')' and w != '(' and w != '-']

    bigram_finder = BigramCollocationFinder.from_words(filtered_words)



    # bigram_finder = BigramCollocationFinder.from_words(filtered_words)
    # score = bigram_finder.score_ngrams(BAM.jaccard)

    bigrams =  bigram_finder.nbest(BAM.likelihood_ratio, 20)


    return dict((bg, True) for bg in chain(words, bigrams))




def getTrigramWordFeatures(words):
    """
    Return relevant Trigrams
    """

    filtered_words = [w for w in words if w != '.' and w != '?' and w != ')' and w != '(' and w != '-']
    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    trigram_finder = TrigramCollocationFinder.from_words(filtered_words)
    trigrams = trigram_finder.nbest(trigram_measures.raw_freq, 3)

    return dict((tg, True) for tg in chain(words, trigrams))




def getExclamationCount(app):
    exclaimCount = 0
    for rev in app['reviews']:
        exclaimCount += rev.count('!')
    return exclaimCount

def getDeveloperHasMultipleApps(app):
    if app['moreFromDev'] == 'None':
        return 0
    else:
        return len(app['moreFromDev'])

def getInstallRange(app):
    installs = app['install'].split(' - ')
    avginstalls = (int(installs[0].replace(',', '')) + int(installs[1].replace(',', ''))) / 2.0

    return round(Decimal(avginstalls), 2) # I just need


def getDeveloperEmailState(app):
    """Implement a domain lookup to see if email domain is 'safe'
    """
    if app['devmail'] == 'N.A.':
        return False
    else:
        return True

def getDeveloperWebsiteState(app):
    """Implement a domain lookup to see if url is functional.
    """
    if app['devurl'] == 'N.A.':
        return False
    else:
        return True

def getAppPrice(app):
    return app['price']


def getReviewLength(app):
    revLength = 0
    #pdb.set_trace()

    for rev in app['reviews']:
        #sentList = nltk.tokenize.sent_tokenize(rev[1])

        revLength += len(rev[1])
    return revLength

def getAverageRating(app):
    total = 0; count = 0
    for rating in app['rating']:
        total = total + (int(rating[0].strip()) * int(rating[1]))
        count = count + int(rating[1])
    return round(Decimal(total/float(count)), 3)

def getOneStarRating(app):
    for appRatingCount in app['rating']:
        if appRatingCount[0] == ' 1 ':
            return appRatingCount[1]


def getTwoStarRating(app):
    for appRatingCount in app['rating']:
        if appRatingCount[0] == ' 2 ':
            return appRatingCount[1]


def getThreeStarRating(app):
    for appRatingCount in app['rating']:
        if appRatingCount[0] == ' 3 ':
            return appRatingCount[1]

def getFourStarRating(app):
    for appRatingCount in app['rating']:
        if appRatingCount[0] == ' 4 ':
            return appRatingCount[1]


def getFiveStarRating(app):
    for appRatingCount in app['rating']:
        if appRatingCount[0] == ' 5 ':
            return appRatingCount[1]


def getPrivacyState(app):
    """Implement a domain lookup to see if url is functional.
    """
    if app['devprivacyurl'] == 'N.A.':
        return False
    else:
        return True


def getReviewSentiment(app, tknRevs, classifier):
    revAggSentiment = 0

    for revList in tknRevs:

        sentAggSentiment = 0

        for sent in revList:

            sent = unicode(sent.strip())
            # print sent
            featdata = extractor.featureExtractor(sent)

            # pprint(featdata)
            #pdb.set_trace()
            cl= classifier.classify(featdata)

            if cl == 'pos':
                label = 1
            elif cl == 'neutral':
                label = 0
            else:
                label = -1

            sentAggSentiment += label

        revAggSentiment += sentAggSentiment

    name = app['name'].encode('utf-8')
    print "App: \t %s, Aggregate Review Sentiment: \t %s" % (name , revAggSentiment)
    return revAggSentiment




def classifier(alldata, fold=4):

    data = [(row['appFeatures'], row['appLabel']) for row in alldata]


    random.shuffle(data)
    # pprint(data)

    claccuracy = []
    size = int(math.floor(len(data) / fold))

    for i in range(fold):
        test_this_round = data[i*size:][:size]
        train_this_round = data[:i*size] + data[(i+1)*size:]

        acc = myclassifier(train_this_round, test_this_round)

        claccuracy.append(acc)


    pprint(claccuracy)






def myclassifier(train_data, test_data):
    print "Train Data"
    print "=" * 79
    print len(train_data)
    # pprint(train_data[0])


    print "Test Data"
    print "=" * 79
    print len(test_data)
    # pprint(test_data[0])




    classifier = nltk.NaiveBayesClassifier.train(train_data)
    # gnb = GaussianNB()
    # y_pred = gnb.fit(train_data).predict(test_data)


    print classifier.show_most_informative_features()

    # for app in test_data:
    #     print app[0], classifier.classify(app[0])
    return nltk.classify.accuracy(classifier, test_data)





def getAnalysisData(uinput):
    appData = []
    for f in listdir(uinput['dir']):
        fname = f.split('_')

        if fname[-1] == 'all.json':
            print uinput['dir'] + f
            fdata = fileExtractor(uinput['dir'] + f)
            appAggData = featureAggregator(fdata)

            # appDict = {}

            for apps in appAggData:

                if fname[0] == 'malapps':
                    apps['appLabel'] = 'unfair'
                else:
                    apps['appLabel'] = 'fair'

                # appDict['appName'] = apps['appName']
                # appDict['appFeatures'] = apps['appFeatures']


                appData.append(apps)



    return appData






def main():
    userinput = getUserInput()
    data = getAnalysisData(userinput)


    classifier(data)


if __name__ == "__main__":
    main()
