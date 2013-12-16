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



def featureExtractor(app):
    featDict = {}
    tokenizedReviews = tokenizeReviewsBySentence(app['reviews'])
    posReviews = posReviewsBySentence(tokenizedReviews)



    # fObj = open('mySentClassifier.pickle')
    # cl = load(fObj)
    # fObj.close()



    featDict['price'] = getAppPrice(app)
    featDict['revlength'] = getReviewLength(app)
    # featDict['1starrating'] = getOneStarRating(app)
    # featDict['2starrating'] = getTwoStarRating(app)
    # featDict['3starRating'] = getThreeStarRating(app)
    # featDict['4starRating'] = getFourStarRating(app)
    # featDict['5starRating'] = getFiveStarRating(app)
    featDict['avgRating'] = getAverageRating(app)
    featDict['hasPrivacy'] = getPrivacyState(app)
    # featDict['revSent'] = getReviewSentiment(tokenizedReviews, cl)
    featDict['hasDeveloperEmail'] = getDeveloperEmailState(app)
    featDict['hasDeveloperWebsite'] = getDeveloperWebsiteState(app)
    featDict['hasMultipleApps'] = getDeveloperHasMultipleApps(app)
    featDict['installRange'] = getInstallRange(app)
    featDict['exclamationCount'] = getExclamationCount(app)
    featDict['adjectiveCount'] = getAdjectiveCount(posReviews)

    return { 'appFeatures': featDict, 'appName': app['name'] }

def getAdjectiveCount(pos_revs):
    adj_counter = 0
    #pdb.set_trace()
    for pos_sent in pos_revs:
        adj_counter += Counter(tag for word, tag in pos_sent)['JJ']

    return int(adj_counter)

def getExclamationCount(app):
    exclaimCount = 0
    for rev in app['reviews']:
        exclaimCount += rev.count('!')
    return exclaimCount

def getDeveloperHasMultipleApps(app):
    if app['moreFromDev'] == 'None':
        return False
    else:
        return True

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


def getReviewSentiment(tknRevs, classifier):
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

    print "review Sentiment: ", revAggSentiment
    return revAggSentiment




def classifier(alldata, fold=4):

    # name = alldata[0]
    data = alldata[1]


    random.shuffle(data)
    pprint(data)

    claccuracy = []
    size = int(math.floor(len(data) / 10.0))

    for i in range(fold):
        test_this_round = data[i*size:][:size]
        train_this_round = data[:i*size] + data[(i+1)*size:]
        #pdb.set_trace()
        acc = myclassifier(train_this_round, test_this_round)

        claccuracy.append(acc)


    pprint(claccuracy)






def myclassifier(train_data, test_data):
    print "Train Data"
    print "=" * 79
    print len(train_data)
    pprint(train_data[0])


    print "Test Data"
    print "=" * 79
    print len(test_data)
    pprint(test_data[0])




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




    # extract = fileExtractor(userinput['file'])

    # pprint(data)
    # features = featureAggregator(extract)
    classifier(data)


if __name__ == "__main__":
    main()
