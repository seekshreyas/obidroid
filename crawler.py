#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Crawler
=========
Give an APP-CATEGORY, it should try crawling the app store for similar
applications in the category and compile the links of the applications
into a text file, that can then be used in the Scraper.py script for
extracting the requisite features.

app-games.txt
-------------
https://play.google.com/store/apps/details?id=[APP-ID]
https://play.google.com/store/apps/details?id=[APP-ID]
https://play.google.com/store/apps/details?id=[APP-ID]
https://play.google.com/store/apps/details?id=[APP-ID]
https://play.google.com/store/apps/details?id=[APP-ID]
"""
from __future__ import division
from optparse import OptionParser


def getAppCategory():
    optionparser = OptionParser()

    optionparser.add_option('-c', '--category', dest='appCategory')

    (option, args) = optionparser.parse_args()

    if not option.appCategory:
        return optionparser.error('Application Category not provided.\n Usage: --url="path.to.appurl"')

    return { 'cat' : option.appCategory }


def main():
    # print __doc__

    appCat = getAppCategory()

    print appCat


if __name__ == '__main__':
    main()
