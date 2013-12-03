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

def getUserInput():
    optionparser = OptionParser()

    optionparser.add_option('-i', '--input', dest='inputfile')


    (option, args) = optionparser.parse_args()

    if not option.inputfile:
        return optionparser.error('html file input not provided.\n Usage: --url="path.to.appurl"')

    return { 'file' : option.inputfile }



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

    # featList['price'] = getAppPrice(app)
    # featList['numrev'] = getNumReviews(app)
    featDict['1starrating'] = getOneStarRating(app)
    featDict['2starrating'] = getTwoStarRating(app)
    featDict['3starRating'] = getThreeStarRating(app)
    featDict['4starRating'] = getFourStarRating(app)
    featDict['5starRating'] = getFiveStarRating(app)
    featDict['hasPrivacy'] = getPrivacyState(app)

    return featDict




def getAppPrice(app):
    return app['price']

def getNumReviews(app):
    return len(app['reviews'])


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
    if app['devprivacyurl'] == 'N.A':
        return False
    else:
        return True


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


    # pprint(data)

    random.shuffle(data)

    claccuracy = []
    size = int(math.floor(len(data) / 10.0))

    for i in range(fold):
        test_this_round = data[i*size:][:size]
        train_this_round = data[:i*size] + data[(i+1)*size:]

        acc = myclassifier(train_this_round, test_this_round)

        claccuracy.append(acc)



def myclassifier(train_data, test_data):
    classifier = nltk.NaiveBayesClassifier.train(train_data)


    # print classifier.show_most_informative_features()
    return nltk.classify.accuracy(classifier, test_data)







def main():
    userinput = getUserInput()
    print userinput['file']

    extract = fileExtractor(userinput['file'])
    # features = featureAggregator(extract)
    classifier(extract)


if __name__ == "__main__":
    main()
