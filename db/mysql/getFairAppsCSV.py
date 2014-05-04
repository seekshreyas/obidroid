#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@author: Shreyas <shreyas@ischool.berkeley.edu>
@author:  Luis Aguilar <luis@ischool.berkeley.edu>

CheckApps
=========
Given an input of fair apps, create a csv file
"""

from __future__ import division
from optparse import OptionParser
import time
import datetime
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
    optionparser.add_option('-o', '--output', dest='output')

    (option, args) = optionparser.parse_args()

    #if not option.file:
    #    return optionparser.error('Data File path not provided.\n Usage: --file="path.to.appData"')
    #elif not option


    return {
        'file': option.file,
        'db': option.db,
        'server': option.server,
        'username': option.un,
        'password': option.pw,
        'output': option.output
    }

def getDataframeFromDatabase(host, db, un, pw):
    query = "SELECT pkgname from fair_apps;"
    conn = MySQLdb.connect(host = host, user = un, passwd = pw, db = db)
    fair_apps_df = psql.frame_query(query, conn)
    return fair_apps_df

def pushDataframeToCSV(df, f_csv):
    df.to_csv(f_csv, index=False, header=False, encoding='utf-8')

def main():
    userInput = getUserInput()
    df = getDataframeFromDatabase(userInput['server'], userInput['db'],
        userInput['username'], userInput['password'])
    pushDataframeToCSV(df, userInput['output'])


if __name__ == '__main__':
    main()
