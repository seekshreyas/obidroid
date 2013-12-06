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


def featureExtractor(app):
    featDict = {}

    fObj = open('mySentClassifier.pickle')
    cl = load(fObj)
    fObj.close()


    featDict['price'] = getAppPrice(app)
    # featList['numrev'] = getNumReviews(app)
    featDict['1starrating'] = getOneStarRating(app)
    featDict['2starrating'] = getTwoStarRating(app)
    featDict['3starRating'] = getThreeStarRating(app)
    featDict['4starRating'] = getFourStarRating(app)
    featDict['5starRating'] = getFiveStarRating(app)
    featDict['avgRating'] = getAverageRating(app)
    featDict['hasPrivacy'] = getPrivacyState(app)
    featDict['revSent'] = getReviewSentiment(app, cl)
    # add to check for developer website
    featDict['hasDeveloperEmail'] = getDeveloperEmailState(app)
    # add to check for developer email address
    featDict['hasDeveloperWebsite'] = getDeveloperWebsiteState(app)
    featDict['installRange'] = getInstallRange(app)
    
    return featDict


def getInstallRange(app):
    return app['install']

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

def getNumReviews(app):
    return len(app['reviews'])

def getAverageRating(app):
    total = 0; count = 0
    for rating in app['rating']:
        total = total + (int(rating[0].strip()) * int(rating[1]))
        count = count + int(rating[1])
    return total/float(count)    

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
    if app['devprivacyurl'] == 'N.A.':
        return False
    else:
        return True



def getReviewSentiment(app, classifier):
    revAggSentiment = 0
    for rev in app['reviews']:
        sentList = nltk.tokenize.sent_tokenize(rev[1])

        sentAggSentiment = 0

        for sent in sentList:

            sent = unicode(sent.strip())
            # print sent
            featdata = extractor.featureExtractor(sent)

            # pprint(featdata)
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




def classifier(extract, fold=10):

    labeldata = 'fair'

    data = []
    for app in extract:
        for rev in app['reviews']:
            revlower = rev[1].lower()

            # print "reviews" , revlower
            if revlower.find('fake') != -1:
                labeldata = 'unfair'

        features = featureExtractor(app)

        data.append([labeldata, list(features.values())])


    pprint(data)

    # for d in data:
    #     if d[1][1] == False:
    #         pprint(d)

    # random.shuffle(data)

    # claccuracy = []
    # size = int(math.floor(len(data) / 10.0))

    # for i in range(fold):
    #     test_this_round = data[i*size:][:size]
    #     train_this_round = data[:i*size] + data[(i+1)*size:]

    #     acc = myclassifier(train_this_round, test_this_round)

    #     claccuracy.append(acc)



def myclassifier(train_data, test_data):
    classifier = nltk.NaiveBayesClassifier.train(train_data)


    # print classifier.show_most_informative_features()
    return nltk.classify.accuracy(classifier, test_data)









def main():
    userinput = getUserInput()
    print userinput

    for f in listdir(userinput['dir']):
        print f

    # extract = fileExtractor(userinput['file'])

    # pprint(extract)
    # features = featureAggregator(extract)
    # classifier(extract)


if __name__ == "__main__":
    main()
