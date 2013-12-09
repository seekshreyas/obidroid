#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Export
=========

Export the extracted feature sets to a CSV file for exploration in R
"""
from __future__ import division
from optparse import OptionParser
from pprint import pprint
from classifier import getAnalysisData

import csv


def getUserInput():
    optionparser = OptionParser()


    optionparser.add_option('-d', '--dir', dest='directory')


    (option, args) = optionparser.parse_args()

    if not option.directory:
        return optionparser.error('html file input not provided.\n Usage: --url="path.to.appurl"')

    return { 'dir' : option.directory}



def export(data):
    # pprint(data)
    header = []
    vectors = []
    labels = []

    appFeaturesFileObj = open('appFeatures.csv', 'wb')
    wr = csv.writer(appFeaturesFileObj)

    counter = 0
    for row in data:
        rowval = []
        labels = []
        labelval = True


        if row[1] == 'unfair':
            labelval = False
        labels.append(labelval)

        for k,v in row[0].iteritems():

            if counter == 0:
                header.append(k)

            if k == 'hasPrivacy' or k == 'hasDeveloperEmail' or k == 'hasDeveloperWebsite' or k == 'hasMultipleApps':
                v = int(bool(v))
            else:
                v = float(v)
            rowval.append(v)

        if counter == 0:
            wr.writerow(header)

        vectors.append(rowval)
        wr.writerow(rowval)
        counter += 1


    pprint(vectors)
    appFeaturesFileObj.close()




def main():
    userinput = getUserInput()

    data = getAnalysisData(userinput)

    export(data)








if __name__ == '__main__':
    main()
