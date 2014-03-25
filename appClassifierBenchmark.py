#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Benchmark different classifiers

Classifiers tried:

- Naive Bayes
- Random Forest
- SVM
    - linear
    - kernelized
"""

from __future__ import division
from optparse import OptionParser
import pandas as pd
import numpy as np
from sklearn import metrics, preprocessing
from sklearn import svm, naive_bayes

def getUserInput():
    """
    Get User Input
    """
    optionparser = OptionParser()

    optionparser.add_option('-m', '--model', dest='model', default="all")
    optionparser.add_option('-f', '--file', dest='file')


    (option, args) = optionparser.parse_args()

    if not option.file:
        return optionparser.error('Data File path not provided.\n Usage: --file="path.to.appData"')

    return { 'model' : option.model, 'file': option.file }





def loadAppData(datafile):
    """
    Data File added
    {
        'fair' : False,
        'unfair': True
    }
    """
    df = pd.read_csv(datafile)

    ## Remove the unnamed column as not sure
    cols = set(df.columns)
    cols.remove('Unnamed: 7')
    df = df[list(cols)]

    ## Convert appLabel to boolean: True for 'unfair'
    df['appLabel'] = df['appLabel'].map(lambda x: x=='unfair')

    return df


def trimDf(df):
    """
    Trim the dataframe provided
    Remove features that we don't think are helping
    """
    cols = set(df.columns)

    cols.remove('exclamationCount') # bug in our feature extraction code
    cols.remove('price') # considered only free apps
    cols.remove('appName') # removing appNames

    return df[list(cols)]




def prepareClassifier(df):
    """
    Classify the apps
    """


    def classify(cDf):
        """
        Given the dataframe combined with equal fair and unfair apps,
        classify them
        """
        cDf = cDf.reindex(np.random.permutation(cDf.index)) # shuffle the dataframe
        featCols = set(cDf.columns)
        featCols.remove('appLabel')

        features = cDf[list(featCols)].values
        ## Scale the features to a common range
        min_max_scaler = preprocessing.MinMaxScaler()
        X = min_max_scaler.fit_transform(features)

        Y = cDf['appLabel'].values


        n_samples = 40


        print "\n\nGaussian NaiveBayes Classification"
        print "#" * 79
        classifier_gnb = naive_bayes.GaussianNB() # initiating the SVM based classifier
        Y_pred_gnb = classifier_gnb.fit(X[:n_samples], Y[:n_samples]) # train on first n_samples and test on last 10

        expected_gnb = Y[n_samples:]
        predicted_gnb = classifier_gnb.predict(X[n_samples:])
        print("Classification report for classifier %s:\n%s\n" % (classifier_gnb, metrics.classification_report(expected_gnb, predicted_gnb)))
        print("\nConfusion matrix:\n%s" % metrics.confusion_matrix(expected_gnb, predicted_gnb))



        print "\n\nSVM-linear Classification"
        print "#" * 79
        classifier_svm = svm.SVC() # initiating the SVM based classifier
        Y_pred_svm = classifier_svm.fit(X[:n_samples], Y[:n_samples]) # train on first n_samples and test on last 10

        expected_svm = Y[n_samples:]
        predicted_svm = classifier_svm.predict(X[n_samples:])
        print("Classification report for classifier %s:\n%s\n" % (classifier_svm, metrics.classification_report(expected_svm, predicted_svm)))
        print("\nConfusion matrix:\n%s" % metrics.confusion_matrix(expected_svm, predicted_svm))


        print "\n\nSVM-Non-linear Classification"
        print "#" * 79
        classifier_nusvm = svm.NuSVC() # initiating the SVM based classifier
        Y_pred_nusvm = classifier_nusvm.fit(X[:n_samples], Y[:n_samples]) # train on first n_samples and test on last 10

        expected_nusvm = Y[n_samples:]
        predicted_nusvm = classifier_nusvm.predict(X[n_samples:])
        print("Classification report for classifier %s:\n%s\n" % (classifier_nusvm, metrics.classification_report(expected_nusvm, predicted_nusvm)))
        print("\nConfusion matrix:\n%s" % metrics.confusion_matrix(expected_nusvm, predicted_nusvm))







    fairDf = df[df['appLabel'] == False]
    unfairDf = df[df['appLabel'] == True]


    # calculate total possible splits of fair data frame relatie to
    # size of unfair dataframe
    splits = len(fairDf) // len(unfairDf)

    for i in range(splits):
        clDf = fairDf[i : i+len(unfairDf)].append(unfairDf)

        # print fairDf.values, unfairDf.values
        print "Classifying %d th split of fair apps with unfair app" % (i)
        print "-" * 79
        classify(clDf)
        print "\n\n"







def main():
    print __doc__

    userInput = getUserInput()
    appDf = loadAppData(userInput['file'])
    appDf = trimDf(appDf)





    print "Sample Data"
    print "-" * 79
    print appDf.head()

    # print
    # print "Data Columns"
    # print "-" * 79
    # for (i,col) in enumerate(appDf.columns):
    #     print "%2s %30s %10s" % (i,col, appDf[col].dtype)


    prepareClassifier(appDf)




if __name__ == '__main__':
    main()
