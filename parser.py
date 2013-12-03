#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Parser
========
Parse the txt files for outputting the reviews as a list of tuples
where each tuple is
(filename, linenumber, aggregatevote, sentence)

author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""
from __future__ import division
from optparse import OptionParser

import os
import re



def getInput():
    optionparser = OptionParser()

    optionparser.add_option('-t', '--train', dest='train')

    (option, args) = optionparser.parse_args()

    if not option.train:
        return optionparser.error('data not provided.\n Usage: --data="path.to.data"')

    return { 'train' : option.train }


def getFiles(dir):
    # os.lisdir(dir)
    os.chdir(dir)
    datafiles = [f for f in os.listdir('.') if f.endswith('.txt')]
    return datafiles


def parseFiles(fList):
    allSents = []

    for f in fList:
        fileObj = open(f)
        linenum = 0
        for l in fileObj:
            linenum += 1
            if not l.startswith('*'):


                #find all occurrence of ## in the sentence
                delimPos = [(a.start(), a.end()) for a in list(re.finditer('##', l))]

                if len(delimPos) == 0:
                    # no reviews in a sentence
                    feat = 'None'
                    rev = '[t]'
                    vote = 'neutral'


                    allSents.append((f, linenum, vote, rev))
                    # print l
                elif len(delimPos) == 1:
                    #simple case of only 1 sentence
                    feat = l.split('##')[0]
                    vote = getVotes(feat)
                    rev = l.split('##')[1]

                    new_vote = standardizeVote(vote)

                    rev = re.sub('\\r\\n', '', rev)


                    allSents.append((f, linenum, new_vote, rev))

                else:
                    # more than 1 reviews in a sentence
                    feat1 = l.split('##')[0]
                    rev2 = l.split('##')[2]
                    rev2 = re.sub('\\r\\n', '', rev2)

                    rev1_feat2 = l.split('##')[1]
                    rev1 = cleanReview(rev1_feat2)
                    rev1 = re.sub('\\r\\n', '', rev1)

                    vote1 = getVotes(feat1)
                    vote2 = getVotes(rev1_feat2)


                    new_vote1 = standardizeVote(vote1)
                    new_vote2 = standardizeVote(vote2)

                    allSents.append((f, linenum, new_vote1, rev1))
                    allSents.append((f, linenum, new_vote2, rev2))

                    # print allSents[-1]

                    # to check error handling uncomment the code below
                    # print vote1, rev1
                    # print vote2, rev2



        fileObj.close()

    return allSents





def standardizeVote(v):
    new_v = ''

    if v > 0:
        new_v = 'pos'
    elif v == 0:
        new_v = 'neutral'
    else:
        new_v = 'neg'

    return new_v

def cleanReview(revstr):
    """
    return the cleaned up review after getting a raw string
    """
    eolregEx = re.compile('[\.|\?]')
    voteregEx = re.compile('\[[\+\-][0-3]?\]')

    eol = [int(a.end()) for a in eolregEx.finditer(revstr)]


    # print eol

    if eol:
        cleanrev = revstr[:eol[-1]]
        temp = revstr[eol[-1]:]

        if not voteregEx.search(temp):
            cleanrev.join(temp)
    else:
        cleanrev = 'N.A.'


    # print revstr
    # print cleanrev, '\n'
    return cleanrev




def getVotes(rawstr):
    voteregEx = re.compile('\[[\+\-][0-3]?\]')
    vote_raw = voteregEx.findall(rawstr)

    if len(vote_raw) == 0:
        # rev1 = rawstr
        # feat2 = 0
        aggrvote = 0.0

    else:
        votes = []
        for vote in vote_raw:
            v = vote[1:-1]
            if v == '+':
                vt = 1
            elif v == '-':
                vt = -1
            else:
                vt = int(v)

            votes.append(vt)

        # meanvote = sum(votes)/len(votes)
        aggrvote = sum(votes)

    return aggrvote + 0.0





def main():
    userInput = getInput()
    fileList = getFiles(userInput['train'])
    sents = parseFiles(fileList)



    # print fileList

    print "-" * 79
    print "No. of files parsed: %d" % (len(fileList))
    print sents[:2]
    print "Total No of sentences: %d" % (len(sents))




if __name__ == "__main__":
    main()

