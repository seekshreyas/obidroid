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
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pylab as pl
from sklearn import metrics
from time import time
from scipy.cluster import vq
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from scipy.spatial.distance import pdist, squareform
import scipy.cluster.hierarchy as hy



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
    labels = []

    for row in data:
        rowval = []
        labels = []
        labelval = True
        if row[1] == 'unfair':
            labelval = False
        labels.append(labelval)

        for k,v in row[0].iteritems():

            if k == 'hasPrivacy' or k == 'hasDeveloperEmail' or k == 'hasDeveloperWebsite':
                v = int(bool(v))
            rowval.append(v)

        vectors.append(np.array(rowval))

    pprint(vectors)
    # vectors = np.asarray(vectors)
    data = np.vstack(vectors)


    means = [vectors[20].tolist(), vectors[21].tolist()]

    if cltype == 'GAAC':
        clusterer = cluster.GAAClusterer(num_clusters=4)
        clusters = clusterer.cluster(vectors, True)
        clusterer.dendrogram().show()
    elif cltype == 'kmeans':
        centroids, variance = vq.kmeans(data, 3)
        identified, distance = vq.vq(data, centroids)

        print identified
        print centroids

        print variance


    elif cltype == 'hy':
        # Creating a cluster of clusters function
        def clusters(number=20, cnumber=5, csize=10):
            # Note that the way the clusters are positioned is Gaussian randomness.
            rnum = np.random.rand(cnumber, 2)
            rn = rnum[:, 0] * number
            rn = rn.astype(int)
            rn[np.where(rn < 5)] = 5
            rn[np.where(rn > number / 2.)] = round(number / 2., 0)
            ra = rnum[:, 1] * 2.9
            ra[np.where(ra < 1.5)] = 1.5

            cls = np.random.randn(number, 3) * csize

            # Random multipliers for central point of cluster
            rxyz = np.random.randn(cnumber - 1, 3)
            for i in xrange(cnumber - 1):
                tmp = np.random.randn(rn[i + 1], 3)
                x = tmp[:, 0] + (rxyz[i, 0] * csize)
                y = tmp[:, 1] + (rxyz[i, 1] * csize)
                z = tmp[:, 2] + (rxyz[i, 2] * csize)
                tmp = np.column_stack([x, y, z])
                cls = np.vstack([cls, tmp])
            return cls

        # Generate a cluster of clusters and distance matrix.
        cls = clusters()
        D = pdist(cls[:, 0:2])
        D = squareform(D)

        # Compute and plot first dendrogram.
        fig = plt.figure(figsize=(8, 8))
        ax1 = fig.add_axes([0.09, 0.1, 0.2, 0.6])
        Y1 = hy.linkage(D, method='complete')
        cutoff = 0.3 * np.max(Y1[:, 2])
        Z1 = hy.dendrogram(Y1, orientation='right', color_threshold=cutoff)
        ax1.xaxis.set_visible(False)
        ax1.yaxis.set_visible(False)

        # Compute and plot second dendrogram.
        ax2 = fig.add_axes([0.3, 0.71, 0.6, 0.2])
        Y2 = hy.linkage(D, method='average')
        cutoff = 0.3 * np.max(Y2[:, 2])
        Z2 = hy.dendrogram(Y2, color_threshold=cutoff)
        ax2.xaxis.set_visible(False)
        ax2.yaxis.set_visible(False)

        # Plot distance matrix.
        ax3 = fig.add_axes([0.3, 0.1, 0.6, 0.6])
        idx1 = Z1['leaves']
        idx2 = Z2['leaves']
        D = D[idx1, :]
        D = D[:, idx2]
        ax3.matshow(D, aspect='auto', origin='lower', cmap=plt.cm.YlGnBu)
        ax3.xaxis.set_visible(False)
        ax3.yaxis.set_visible(False)

        # Plot colorbar.
        fig.savefig('scipy_352_ex1.pdf', bbox='tight')













    # print 'Clusterer:', clusterer
    # print 'Clustered:', vectors
    # print 'As:', clusters








def main():
    userinput = getUserInput()

    data = getAnalysisData(userinput)

    createCluster(data, userinput['cl'])








if __name__ == '__main__':
    main()
