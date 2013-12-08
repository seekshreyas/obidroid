#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Clustering
==========
Cluster the data after extracting features from them
"""

from optparse import OptionParser
from pprint import pprint
from classifier import getAnalysisData
import numpy as np
from sklearn.cluster import DBSCAN


def getUserInput():
    optionparser = OptionParser()


    optionparser.add_option('-d', '--dir', dest='directory')


    (option, args) = optionparser.parse_args()

    if not option.directory:
        return optionparser.error('html file input not provided.\n Usage: --url="path.to.appurl"')

    return { 'dir' : option.directory }




def buildColumnData(data):

    for row in data:
        for fkey in row[1]:
            print row[1][fkey]




def main():
    userinput = getUserInput()

    data = getAnalysisData(userinput)

    datacol = buildColumnData(data)







if __name__ == '__main__':
    main()
