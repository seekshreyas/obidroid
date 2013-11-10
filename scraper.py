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
- [x] Rating
    - [
        (OneStarRating, OneStarRatingCount),
        (TwoStarRating, TwoStarRatingCount)
        (ThreeStarRating, ThreeStarRatingCount)
        (FourStarRating, FourStarRatingCount)
        (FiveStarRating, FiveStarRatingCount)
      ]
- [x] Total Reviewers
- [ ] PlusOneCount
- [ ] CountOfScreenShots
- [x] Description
- [x] Installs
- [x] ContentRating
- [ ] SimilarApps:
    [SimAppId1, SimAppId2, ..]
- [ ] MoreAppsFromDev
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
from pprint import pprint



# To strip html tags
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

    # print "price", price

    if price == 'Install':
        priceVal = 0.0
    else:
        priceVal = float(str(price[1:4])) # since first character is currrency

    return priceVal



def getAppRating(pageSoup):
    """
    Given the page soup, extract the app ratings and the count of
    people who gave those ratings
    """
    appRatingSoup = pageSoup.find_all('div', {'class':'rating-bar-container'})

    appRating = []


    for ratingContainer in appRatingSoup:
        # print type(ratingContainer)
        ratElem = ratingContainer.find_all("span", attrs={"class":"bar-label"})
        ratcountElem = ratingContainer.find_all("span", attrs={"class":"bar-number"})

        rat = str(strip_tags(str(ratElem[0])))
        ratcount = int(strip_tags(str(ratcountElem[0])))

        appRating.append((rat, ratcount))


    return appRating



def getTotalReviewers(ratingTup):
    """
    Given a tuple of ratings, sum the count of Reviewers
    """
    totalReviewers = 0

    for r in ratingTup:
        totalReviewers += r[1]

    return totalReviewers




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




    appPrice            = getAppPrice(pageSoup) # Application Price
    appRating           = getAppRating(pageSoup) # Application Rating

    appReviewers        = getTotalReviewers(appRating) # Total Reviewers


    appCat              = pageSoup.find(itemprop='genre').get_text() # Application Category
    appVer              = pageSoup.find(itemprop='softwareVersion').get_text() # Application Version

    appInstallElem      = pageSoup.find_all('div', attrs={'itemprop':'numDownloads'})
    appInstall          = str(strip_tags(str(appInstallElem))) #Application Installs



    appContentRating    = pageSoup.find(itemprop='contentRating').get_text() # Application Content Rating
    appSize             = pageSoup.find(itemprop='fileSize').get_text() # Application Content Rating
    appGplusCount       = pageSoup.find_all('span', attrs={'class':'A8 eja'}) # Application Content Rating

    print appGplusCount



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
    appDetails['rating'] = appRating
    appDetails['totalreviewers'] = appReviewers


    return appDetails





def main():
    # print __doc__

    appUrl = getAppUrl()
    features = getAppFeatures(appUrl['url'])

    pprint(features)


if __name__ == '__main__':
    main()
