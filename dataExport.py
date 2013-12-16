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

import json
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
    # vectors = []
    labels = []

    appFeaturesFileObj = open('exports/appFeatures.csv', 'wb')
    wr = csv.writer(appFeaturesFileObj)




    counter = 0
    for row in data:
        name = row[0][0]
        rowval = []
        labelval = True

        if counter == 0:
            header.append('appName')
        else:
            rowval.append(name)

        if row[1] == 'unfair':
            labelval = False




        for k,v in row[0][1].iteritems():
            if counter == 0:
                header.append(k)

            # if k == 'hasPrivacy' or k == 'hasDeveloperEmail' or k == 'hasDeveloperWebsite' or k == 'hasMultipleApps':
            if isinstance(v, bool):
                v = int(bool(v))
            else:
                try:
                    v = float(v)
                except:
                    print "exception: ", k, v

            rowval.append(v)

        if counter == 0:
            header.append('Fair')
            wr.writerow(header)

        rowval.append(labelval)


        try:
            wr.writerow(rowval)
        except:
            pprint(rowval)
        counter += 1



    appFeaturesFileObj.close()



def exportFile(data):

    headers = ['appName']


    featNames = sorted(data[0].keys())
    headers.append(featNames)
    headers.append('appLabel')


    appFeaturesFileObj = open('exports/appFeatures.csv', 'wb')
    wr = csv.writer(appFeaturesFileObj)

    wr.writerow(headers)

    for row in data:
        # pprint(row)
        # break
        rowvals = []
        name = row['appName'].encode('UTF-8').strip()
        rowvals.append(name)

        appFeatures = row['appFeatures']

        for k in sorted(appFeatures.keys()):
            value = appFeatures[k]
            rowvals.append(value)

        rowvals.append(row['appLabel'])

        # pprint(rowvals)

        try:
            wr.writerow(rowvals)
        except:
            print "Skipping %s app for ASCII error: " % (rowvals[0])

    appFeaturesFileObj.close()





def main():
    userinput = getUserInput()

    data = getAnalysisData(userinput)


    # pprint(data)

    # export(data)

    exportFile(data)







if __name__ == '__main__':
    main()
