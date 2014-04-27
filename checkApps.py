#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@author: Shreyas <shreyas@ischool.berkeley.edu>

CheckApps
=========
Given an input of apps, check if the app exists
"""

from __future__ import division
from optparse import OptionParser
import time
import requests
import pandas as pd

def getUserInput():
    """
    Get User Input
    """
    optionparser = OptionParser()

    optionparser.add_option('-f', '--file', dest='file')

    (option, args) = optionparser.parse_args()

    if not option.file:
        return optionparser.error('Data File path not provided.\n Usage: --file="path.to.appData"')


    return {
        'file': option.file
    }




def checkApps(df):
    """
    Input a dataframe of app ids and check if the apps exist
    in the store
    """

    def getApp(id):
        relaxtime = 5 # 5 s timeout
        time.sleep(relaxtime)


        r = requests.get(stores['google']+id)

        return r.status_code

    stores = {
        'google' :'https://play.google.com//store/apps/details?id='
    }

    # df['appId'].apply(getApp)
    df['appStatus'] = df['appId'].apply(getApp)

    return df








def main():
    userInput = getUserInput()

    appDf = pd.read_csv(userInput['file'])

    newDf = checkApps(appDf)

    print newDf.head()


if __name__ == '__main__':
    main()
