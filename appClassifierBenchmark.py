
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
import sys
import pandas as pd
import numpy as np
from optparse import OptionParser
from sklearn import metrics, preprocessing
from sklearn import svm, naive_bayes, neighbors, tree
from sklearn.ensemble import AdaBoostClassifier



def getUserInput(models):
    """
    Get User Input
    """
    optionparser = OptionParser(add_help_option=False, epilog="multiline")

    optionparser.add_option('-c', '--classifier', dest='classifier', default="all")
    optionparser.add_option('-h', '--help', dest='help', action='store_true',
                  help='show this help message and exit')
    optionparser.add_option('-f', '--file', dest='file')


    (option, args) = optionparser.parse_args()

    if option.help:
        print optionparser.print_help()
        print __doc__
        print "Supported Classifier Models:"


        # print models
        for index, key in enumerate(models):
            print "%2s % 20s" % (index, key)

        print "Default option: 'all'\n"

        print "To run the program, provide app features file path"
        print "Usage: --file='path.to.appData'"

        sys.exit()


    if not option.file:
            return optionparser.error('Data File path not provided.\n Usage: --file="path.to.appData"')


    return { 'classifier' : option.classifier, 'file': option.file }





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




def prepareClassifier(df, models, choice):
    """
    Classify the apps
    """


    def classificationOutput(clf, X, Y):
        """
        Fit the model and print the classification results
        - confusion_matrix
        - avg scores etc
        """
        n_samples = 40

        print "\n\nClassifier: \n %s" % (clf)
        print "#" * 79
        # classifier_gnb = naive_bayes.GaussianNB() # initiating the classifier

        Y_pred = clf.fit(X[:n_samples], Y[:n_samples]) # train on first n_samples and test on last 10

        expected = Y[n_samples:]
        predicted = clf.predict(X[n_samples:])
        print("Classification report:\n%s\n" % (metrics.classification_report(expected, predicted)))
        print("\nConfusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))




    def classify(cDf):
        """
        Given the dataframe combined with equal fair and unfair apps,
        classify them
        """
        cDf = cDf.reindex(np.random.permutation(cDf.index)) # shuffle the dataframe
        featCols = set(cDf.columns)
        featCols.remove('appLabel')

        features = cDf[list(featCols)].astype('float')
        ## Scale the features to a common range
        min_max_scaler = preprocessing.MinMaxScaler()
        X = min_max_scaler.fit_transform(features.values)

        Y = cDf['appLabel'].values


        if choice == 'all':
            for key in models:
                classifier = models[key]
                classificationOutput(classifier, X, Y)
        else:
            if choice in models:
                classifier = models[choice]
                classificationOutput(classifier, X, Y)
            else:
                print "Incorrect Choice"



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

    # Supported classifier models
    n_neighbors = 3
    models = {
                'nb' : naive_bayes.GaussianNB(),
                'svm-l' : svm.SVC(),
                'svm-nl' : svm.NuSVC(),
                'tree' : tree.DecisionTreeClassifier(),
                'forest': AdaBoostClassifier(tree.DecisionTreeClassifier(max_depth=1),algorithm="SAMME",n_estimators=200),
                'knn-uniform' : neighbors.KNeighborsClassifier(n_neighbors, weights='uniform'),
                'knn-distance' : neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
    }

    userInput = getUserInput(models)
    appDf = loadAppData(userInput['file'])
    appDf = trimDf(appDf)


    # print "Sample Data"
    # print "-" * 79
    # print appDf.head()


    prepareClassifier(appDf, models, userInput['classifier'])




if __name__ == '__main__':
    main()
