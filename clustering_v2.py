#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Clustering Version 2
=====================
After Feature Extraction, that returns a data of the format
[(filename, linenum, vote, sentence, feat1, feat2, ...)]

Improving the initial clustering mechanism (via R scripts) to
SciKit based clustering and producing plots

For clustering there shall be no resampling required.
We are looking for clues via unsupervised learning approach.

Attempting the following clustering operations
- [ ] k-means
- [ ] mini k-means

======================
"""

from __future__ import division
from optparse import OptionParser
from pprint import pprint

import pandas as pd



def getUserInput():
    """
    The following flags are supported

    -f or --file
            provide the path to the app features file extracted


    -c or --cluster
            choose a clustering engine

            - km (for kmeans)
            - mkm (for minikmeans)
    """


    optionparser = OptionParser()
    usage = "usage: $python clustering_v2.py arg1 arg2"

    optionparser.add_option('-c', '--cl', dest="cluster", default="km")
    optionparser.add_option('-f', '--file', dest="file")

    (option, args) = optionparser.parse_args()

    if not option.file:
        print "App Features file not provided"
        print usage
        print getUserInput.__doc__

        return
    else:

        return {'cluster': option.cluster, 'file': option.file}



def loadData(filepath):
    """
    load the features from the appfeatures file, where features have
    been stored after extraction
    """
    featDframe = pd.read_csv(filepath)

    print featDframe.columns

    return featDframe




def main():
    print __doc__

    userInput = getUserInput()

    ## a pandas dataframe object
    appData = loadData(userInput['file'])



if __name__ == "__main__":
    main()

