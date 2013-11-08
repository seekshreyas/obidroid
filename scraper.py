#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Scraper
==========
Given, the ANDROID-APP-URL, this module is meant to be able
to extract an agreed upon set of features about the app
- [x] Name
- [x] Company
- [x] AppCategory
- [x] AppId
- [x] AppVer
- [x] Price
- [ ] Rating
    - [
        (OneStarRating, OneStarRatingCount),
        (TwoStarRating, TwoStarRatingCount)
        (ThreeStarRating, ThreeStarRatingCount)
        (FourStarRating, FourStarRatingCount)
        (FiveStarRating, FiveStarRatingCount)
      ]
- [ ] Total Reviewers
- [ ] PlusOneCount
- [ ] CountOfScreenShots
- [x] Description
- [x] Installs
- [x] ContentRating
- [ ] SimilarApps:
    [S[ ] imAppId1, SimAppId2, ..]
- [ ] MoreAppsFromDev
    [O[ ] therAppId1, OtherAppId2, .. ]



author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""

from __future__ import division
from optparse import OptionParser
from bs4 import BeautifulSoup
from urllib import urlopen
from HTMLParser import HTMLParser

import pprint


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



def getAppPrice(pageSoup):
    """
    Given soup of the html page, extract the price of the app
    """
    priceSoup = pageSoup.find('span', {"class" : "price", "class":"buy"})

    priceList = list(priceSoup.contents)
    price = priceList[-2].get_text().strip()

    print "price", price

    if price == 'Install':
        priceVal = 0.0
    else:
        priceVal = float(str(price[1:4]))

    return priceVal



def getAppRating(pageSoup):
    """
    Given the page soup, extract the app ratings and the count of
    people who gave those ratings
    """

    return 0



def getAppFeatures(app):
    """
    Given the Application URL, Extract the desired features
    """
    pageHtml = urlopen(app).read()

    pageSoup = BeautifulSoup(pageHtml)

    # Application Id
    appIdStr = app.split('?')[1]
    appId = appIdStr[3:]


    # Application Description
    appDescHTML = pageSoup.findAll('div', {"class":"app-orig-desc"})
    appDesc = appDescHTML[0].get_text()

    # Application Company
    appCompHTML = pageSoup.findAll('a', {"itemprop":"name"})
    appComp = appCompHTML[0].get_text()

    # Application Name
    appNameHTML = pageSoup.findAll('div', {"itemprop":"name"})
    appName = appNameHTML[0].get_text()


    # Application Rating
    # rating5star_html = pageSoup.findAll('div', {"class":"rating-bar-container", "class":"five"})
    # rating5star = strip_tags(rating5star_html[0].renderContents())


    appPrice            = getAppPrice(pageSoup) # Application Price
    appRating           = getAppRating(pageSoup) # Application Rating


    appCat              = pageSoup.find(itemprop='genre').get_text() # Application Category
    appVer              = pageSoup.find(itemprop='softwareVersion').get_text() # Application Version
    appInstall          = pageSoup.find(itemprop='numDownloads').get_text() # Application Installs
    appContentRating    = pageSoup.find(itemprop='contentRating').get_text() # Application Content Rating
    appSize             = pageSoup.find(itemprop='fileSize').get_text() # Application Content Rating




    # print rating5star_html, len(rating5star_html), rating5star

    appDetails = {}
    appDetails['id'] = appId.strip()
    appDetails['name'] = appName.strip()
    appDetails['cat'] = appCat.strip()
    appDetails['size'] = appSize.strip()
    appDetails['price'] = appPrice
    appDetails['desc'] = appDesc.strip()
    appDetails['comp'] = appComp.strip()
    appDetails['ver'] = appVer.strip()
    appDetails['install'] = appInstall.strip()
    appDetails['contentrating'] = appContentRating.strip()


    return appDetails





def main():
    # print __doc__

    appUrl = getAppUrl()
    features = getAppFeatures(appUrl['url'])

    pprint.pprint(features)


if __name__ == '__main__':
    main()
