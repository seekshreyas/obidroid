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
import datetime
import requests
import MySQLdb
import pandas as pd
import numpy as np
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
    #query = "SELECT package from potential_unfair_apps LIMIT 1000;"
    query = "SELECT package from potential_unfair_apps;"
    print query
    conn = MySQLdb.connect(host = host, user = un, passwd = pw, db = db)


    unfair_apps_df = psql.frame_query(query, conn)

    return unfair_apps_df

def pushDataframeToDatabase(df, host, db, un, pw, date):    
    print "Date: ", date

    table_name = 'potential_unfair_apps_' + date

    print "Database name: ", table_name
    conn = MySQLdb.connect(host = host, user = un, passwd = pw, db = db)
    df.to_sql(con=conn, name=table_name, if_exists='append', flavor='mysql')

def main():
    userInput = getUserInput()
    unfair_df = None
    timestamp = time.time()
    date_str = datetime.datetime.fromtimestamp(timestamp).strftime("%Y%m%d_%H%M%S")

    print userInput
    if userInput['file'] != None:
        ptl_unfair_df = pd.read_csv(userInput['file'])
    else:
        ptl_unfair_df = getDataframeFromDatabase(userInput['server'], userInput['db'],
        userInput['username'], userInput['password'])

    # split dataframe to a manageable size
    ptl_unfair_df_list =  np.array_split(ptl_unfair_df, len(ptl_unfair_df)/100)

    for x in range(len(ptl_unfair_df_list)):
        print 'processing batch ' + str(x)
        unfair_df = checkApps(ptl_unfair_df_list[x])
        pushDataframeToDatabase(unfair_df, userInput['server'], userInput['db'],
            userInput['username'], userInput['password'], date_str)

if __name__ == '__main__':
    main()
