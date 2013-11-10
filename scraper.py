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
- [-] PlusOneCount
- [x] CountOfScreenShots
- [x] Description
- [x] Installs
- [x] ContentRating
- [ ] SimilarApps:
    [SimAppId1, SimAppId2, ..]
- [ ] MoreAppsFromDev
    [OtherAppId1, OtherAppId2, .. ]
- [ ] User Reviews
        [
            (Review Heading, Review Text),
            (Review Heading, Review Text),
            (Review Heading, Review Text)
        ]



author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""

from __future__ import division
from optparse import OptionParser
from bs4 import BeautifulSoup
from urllib import urlopen
from HTMLParser import HTMLParser
# from lxml import etree
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

        rat = strip_tags(str(ratElem[0]))
        ratcountraw = strip_tags(str(ratcountElem[0]))

        ratcount = formatStrToNum(ratcountraw)


        appRating.append((rat, ratcount))


    return appRating



def formatStrToNum(rawnum):
    """
    Handle different forms of string values that need to be converted to
    numbers
    1,000 -> 1000
    """

    if ',' in rawnum:
        rawnum = rawnum.replace(',', '')

    return int(rawnum)



def getTotalReviewers(ratingTup):
    """
    Given a tuple of ratings, sum the count of Reviewers
    """
    totalReviewers = 0

    for r in ratingTup:
        totalReviewers += r[1]

    return totalReviewers



def handleDataError(raw):
    """
    Handle raw values which could be empty or non existent or illformatted
    """
    try:
        clean = strip_tags(str(raw[0]))
    except:
        clean = 'N.A.'

    return clean


def getAppFeatures(app):
    """
    Given the Application URL, Extract the desired features
    """
    pageHtml = urlopen(app).read()

    # pageTree = etree.parse(pageHtml)
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

    appVerElem          = pageSoup.find_all('div', attrs={'itemprop':'softwareVersion'})

    appVer              = handleDataError(appVerElem)


    appInstallElem      = pageSoup.find_all('div', attrs={'itemprop':'numDownloads'})

    appInstall          = handleDataError(appInstallElem) #Application Installs


    appContentRatingElem= pageSoup.find_all('div', attrs={'itemprop':'contentRating'})
    appContentRating    = handleDataError(appContentRatingElem) #Application Content Rating

    appSizeElem         = pageSoup.find_all('div', attrs={'itemprop':'fileSize'})

    appSize             = handleDataError(appSizeElem) #Application Silze


    appScreenElem       = pageSoup.find_all('img', attrs={'itemprop':'screenshot'})

    # pprint(appScreenElem)
    appScreenCount      = len(appScreenElem)


    ## Get Similar Apps
    # similarAppList      = pageSoup.select('div.rec-cluster')
    # similarAppList      = pageTree.xpath('//*[@id="body-content"]/div[9]/div/div/div')
    # pprint(similarAppList)
    # for a in similarAppList:
    #     pprint(a['href'])


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
    appDetails['rating'] = list(set(appRating))
    appDetails['totalreviewers'] = appReviewers
    appDetails['screencount'] = appScreenCount


    return appDetails





def main():
    # print __doc__

    appUrl = getAppUrl()
    features = getAppFeatures(appUrl['url'])

    pprint(features)


if __name__ == '__main__':
    main()
