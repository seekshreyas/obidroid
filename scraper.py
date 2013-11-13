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
- [x] SimilarApps:
    set([SimAppId1, SimAppId2, ..])
- [x] MoreAppsFromDev
    set([OtherAppId1, OtherAppId2, .. ])
- [x] User Reviews
        [
            (Review Heading, Review Text),
            (Review Heading, Review Text),
            (Review Heading, Review Text),
            ...
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
import json
import time


# reference: http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
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






def getUserInput():
    optionparser = OptionParser()

    optionparser.add_option('-u', '--url', dest='appurl')
    optionparser.add_option('-f', '--file', dest='applist')

    (option, args) = optionparser.parse_args()

    if not option:
        return optionparser.error('data not provided.\n Usage: --url="path.to.appurl", --file to "path.to.file"')

    return { 'url' : option.appurl, 'file' : option.applist }











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
    pageSoup = BeautifulSoup(pageHtml, 'html5')

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


    appReviewElem       = pageSoup.find_all('div', attrs={'class':'review-text'})

    # Get App Reviews
    appReviews = []
    for elem in appReviewElem:
        revtitle = elem.span.get_text()
        elem.span.decompose() # to remove the title
        revtext = elem.get_text()

        appReviews.append((revtitle, revtext))



    # Get Similar and Dev app list
    # appRecos            = pageSoup.find_all('div', attrs={'class':'details-section recommendation '})
    appRecoElems = pageSoup.select('a[href^="/store/apps/details?id="]')

    # print "recommendation:", appRecos
    appSim = [] # apps that are similar and hence recommended
    appDev = [] # apps from same developer
    for app in appRecoElems:
        if '&' not in app['href']:
            appPathStr = app['href'].split('=')
            appPath = appPathStr[1]


            currentAppIdStr = appId.split('.')
            otherAppIdStr = appPath.split('.')


            if (currentAppIdStr[0] == otherAppIdStr[0]) & (currentAppIdStr[1] == otherAppIdStr[1]):
                ## apps from the same developer
                appDev.append(appPath)
            else:
                appSim.append(appPath)






    appDetails = {}
    appDetails['id']                = appId.strip()
    appDetails['name']              = appName.strip()
    appDetails['category']          = appCat.strip()
    appDetails['size']              = appSize.strip()
    appDetails['price']             = appPrice
    appDetails['description']       = appDesc.strip()
    appDetails['company']           = appComp.strip()
    appDetails['version']           = appVer.strip()
    appDetails['install']           = appInstall.strip()
    appDetails['contentRating']     = appContentRating.strip()
    appDetails['rating']            = list(set(appRating))
    appDetails['totalReviewers']    = appReviewers
    appDetails['screenCount']       = appScreenCount
    appDetails['reviews']           = appReviews


    appDetails['moreFromDev']       = 'None'  if (len(set(appDev)) == 0) else list(set(appDev))
    appDetails['similar']           = 'None'  if (len(set(appSim)) == 0) else list(set(appSim))





    return appDetails






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


def getTotalReviewers(ratingTup):
    """
    Given a tuple of ratings, sum the count of Reviewers
    """
    totalReviewers = 0

    for r in ratingTup:
        totalReviewers += r[1]

    return totalReviewers


def formatStrToNum(rawnum):
    """
    Handle different forms of string values that need to be converted to
    numbers
    1,000 -> 1000
    """

    if ',' in rawnum:
        rawnum = rawnum.replace(',', '')

    return int(rawnum)










def main():
    # print __doc__

    relaxtime = 5
    exportFileAll = 'exports/alldata.json'
    userInput = getUserInput()

    if userInput['file'] == None:
        ## Single url input given
        features = getAppFeatures(userInput['url'])

        pprint(features)
    else:
        ## File input given
        ## run through the list of url and
        with open(userInput['file']) as f:
            fileTxt = f.readlines()

        allRows = []
        fileProcessed = 0
        for line in fileTxt:
            # print "line: ", line
            features = getAppFeatures(line)
            allRows.append(features)
            fileProcessed += 1
            print "Finished processing %d / %d app urls" % (fileProcessed, len(fileTxt))

            time.sleep(relaxtime) ## pause for next request



        with open(exportFileAll, 'w+') as fp:
            json.dump(allRows, fp, sort_keys=True)
            print "Exported the data to: \t %s" % (exportFileAll)




if __name__ == '__main__':
    main()
