#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Clustering
==========
Cluster the data after extracting features from them
"""
from __future__ import division
from optparse import OptionParser
from pprint import pprint
from classifier import getAnalysisData
from nltk import cluster
import numpy as np


def getUserInput():
    optionparser = OptionParser()


    optionparser.add_option('-d', '--dir', dest='directory')
    optionparser.add_option('-c', '--cluster', dest='cluster', default="GAAC")


    (option, args) = optionparser.parse_args()

    if not option.directory:
        return optionparser.error('html file input not provided.\n Usage: --url="path.to.appurl"')

    return { 'dir' : option.directory, 'cl' : option.cluster }






def createCluster(data, cltype):
    # pprint(data)

    vectors = []

    for row in data:
        rowval = []
        for k,v in row[0].iteritems():

            if k == 'hasPrivacy' or k == 'hasDeveloperEmail' or k == 'hasDeveloperWebsite':
                v = bool(v)

            rowval.append(v)

        vectors.append(np.array(rowval))

    pprint(vectors)

    means = [vectors[20].tolist(), vectors[21].tolist()]

    if cltype == 'GAAC':
        clusterer = cluster.GAAClusterer(num_clusters=4)
        clusters = clusterer.cluster(vectors, True)
        clusterer.dendrogram().show()
    elif cltype == 'kmeans':
        clusterer = cluster.EMClusterer(initial_means=means)
        clusters = clusterer.cluster(vectors, assign_clusters=True, trace=False)

        for c in range(2):
            print 'Clustered:', vectors
            print 'As:', clusters
            print 'Cluster:', c
            print 'Prior:  ', clusterer._priors[c]
            print 'Mean:   ', clusterer._means[c]
            print 'Covar:  ', clusterer._covariance_matrices[c]





    # print 'Clusterer:', clusterer
    # print 'Clustered:', vectors
    # print 'As:', clusters








def main():
    userinput = getUserInput()

    data = getAnalysisData(userinput)

    createCluster(data, userinput['cl'])








if __name__ == '__main__':
    main()
