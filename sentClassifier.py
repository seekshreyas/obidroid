#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Given a sentence, classify that sentence into
+1 : positive
 0 : neutral
-1 : negative
"""

from __future__ import division
import nltk
from cPickle import load

import extractor


def tokenizeReviewsBySentence(revStr):
    return nltk.tokenize.sent_tokenize(revStr)




def getReviewSentiment(tknRevs, classifier):
    revAggSentiment = 0

    for sent in tknRevs:
        sent = unicode(sent.strip())

        featdata = extractor.featureExtractor(sent)

        cl= classifier.classify(featdata)

        if cl == 'pos':
            label = 1
        elif cl == 'neutral':
            label = 0
        else:
            label = -1

        revAggSentiment += label


    return revAggSentiment




def sentClassify(sentStr):
    """
    Given a sentence string, classify the sentence
    """

    tokenizedReviews = tokenizeReviewsBySentence(sentStr)

    ## load the classifier pickle
    fObj = open('mySentClassifier.pickle')
    cl = load(fObj)
    fObj.close()

    revSent = getReviewSentiment(tokenizedReviews, cl)

    return revSent




def main():
    sent = sentClassify("This is a great app. I love it. ")

    print sent



if __name__ == '__main__':
    main()
