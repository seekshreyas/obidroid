#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
OutputParser
==========
Parse the output of map reduce jobs
"""

from __future__ import division
from optparse import OptionParser
from collections import defaultdict
import ast
import pandas as pd

def getUserInput():
    optionparser = OptionParser()

    optionparser.add_option('-f', '--file', dest='inputfile')
    optionparser.add_option('-d', '--dir', dest='directory')


    (option, args) = optionparser.parse_args()

    if not option.inputfile:
        return optionparser.error('html file input not provided.\n Usage: --url="path.to.appurl"')

    return { 'file' : option.inputfile, 'dir' : option.directory }



def parseInputFile(path):
    df = pd.read_table(path, names=['appid', 'appfeatures'])

    df['appfeatures'] = df['appfeatures'].apply(lambda x: ast.literal_eval(x))

    print df['appfeatures'].dtype

    return df



def getItem(x):
    y = ast.literal_eval(x)

    print type(y)

    return y[0][0]







def main():
    userInput = getUserInput()

    rawdf = parseInputFile(userInput['file'])

    rawdf['revCharLength'] = rawdf['appfeatures']

    rawdf['revCharLength'] = rawdf['revCharLength'].apply(lambda x: getItem(x))


    print rawdf.head()



if __name__ == '__main__':
    main()


