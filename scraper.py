#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Scraper
==========
Given, the ANDROID-APP-URL, this module is meant to be able
to extract an agreed upon set of features about the app
- Name
- Company
- AppCategory
- AppId
- Price
- Rating
    - [
        (OneStarRating, OneStarRatingCount),
        (TwoStarRating, TwoStarRatingCount)
        ...
      ]
- Total Reviewers
- PlusOneCount
- CountOfScreenShots
- Description
- Installs
- ContentRating
- SimilarApps:
    [SimAppId1, SimAppId2, ..]
- MoreAppsFromDev
    [OtherAppId1, OtherAppId2, .. ]



author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""

from __future__ import division
from optparse import OptionParser
from bs4 import BeautifulSoup
from urllib import urlopen
from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



def getAppUrl():
    optionparser = OptionParser()

    optionparser.add_option('-u', '--url', dest='appurl')

    (option, args) = optionparser.parse_args()

    if not option.appurl:
        return optionparser.error('data not provided.\n Usage: --url="path.to.appurl"')

    return { 'url' : option.appurl }



def getAppFeatures(app):
    """
    Given the Application URL, Extract the desired features
    """
    pageHtml = urlopen(app).read()

    pageSoup = BeautifulSoup(pageHtml)

    # Application Id
    appIdStr = app.split('?')[1]
    appId = appIdStr[3:]

    # Application Name
    appNameHTML = pageSoup.findAll('div', {"itemprop":"name", "class":"document-title"})
    appName = strip_tags(appNameHTML[0].renderContents())


    # Application Company
    appCompHTML = pageSoup.findAll('a', {"itemprop":"name"})
    appComp = appCompHTML[0].renderContents()

    # Application Rating
    rating5star_html = pageSoup.findAll('div', {"class":"rating-bar-container", "class":"five"})
    rating5star = strip_tags(rating5star_html[0].renderContents())

    print rating5star_html, len(rating5star_html), rating5star

    appDetails = {}
    appDetails['appId'] = appId.strip()
    appDetails['appName'] = appName.strip()
    appDetails['appComp'] = appComp.strip()

    return appDetails


def main():
    # print __doc__

    appUrl = getAppUrl()
    features = getAppFeatures(appUrl['url'])

    print features


if __name__ == '__main__':
    main()
