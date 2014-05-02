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
import MySQLdb
import pandas as pd
import pandas.io.sql as psql

def getUserInput():
    """
    Get User Input
    """
    optionparser = OptionParser()

    optionparser.add_option('-f', '--file', dest='file')
    optionparser.add_option('-d', '--db', dest='db')
    optionparser.add_option('-s', '--server', dest='server')
    optionparser.add_option('-u', '--username', dest='un')
    optionparser.add_option('-p', '--password', dest='pw')

    (option, args) = optionparser.parse_args()

    #if not option.file:
    #    return optionparser.error('Data File path not provided.\n Usage: --file="path.to.appData"')
    #elif not option


    return {
        'file': option.file,
        'db': option.db,
        'server': option.server,
        'username': option.un,
        'password': option.pw
    }




def checkApps(df):
    """
    Input a dataframe of app ids and check if the apps exist
    in the store
    """

    def getApp(id):
        relaxtime = 1 # 5 s timeout
        time.sleep(relaxtime)

        print 'I\'m checking: ' + id
        r = requests.get(stores['google']+id)

        print id, r.status_code

        return r.status_code

    stores = {
        'google' :'https://play.google.com//store/apps/details?id='
    }

    print df.head(10)
    # df['appId'].apply(getApp)
    df['status'] = df['package'].apply(getApp)

    return df


def getDataframeFromDatabase(host, db, un, pw):
    query = "SELECT package from potential_unfair_apps LIMIT 100;"
    conn = MySQLdb.connect(host = host, user = un, passwd = pw, db = db)
    unfair_apps_df = psql.frame_query(query, conn)
    return unfair_apps_df

def pushDataframeToDatabase(df, host, db, un, pw):
    conn = MySQLdb.connect(host = host, user = un, passwd = pw, db = db)
    df.to_sql(con=conn, name='potential_unfair_apps', if_exists='replace', flavor='mysql')

def main():
    userInput = getUserInput()
    unfair_df = None

    print userInput
    if userInput['file'] != None:
        ptl_unfair_df = pd.read_csv(userInput['file'])
    else:
        ptl_unfair_df = getDataframeFromDatabase(userInput['server'], userInput['db'],
        userInput['username'], userInput['password'])

    unfair_df = checkApps(ptl_unfair_df)
    pushDataframeToDatabase(unfair_df, userInput['server'], userInput['db'],
        userInput['username'], userInput['password'])


if __name__ == '__main__':
    main()
