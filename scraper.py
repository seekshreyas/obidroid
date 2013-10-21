#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Scraper
==========
Given, the url of an andoid application, this module is meant to be able
to extract an agreed upon set of features about the app
- Name
- Company
- AppCategory
- AppId
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


def getAppUrl():
    optionparser = OptionParser()

    optionparser.add_option('-u', '--url', dest='app')

    (option, args) = optionparser.parse_args()

    if not option.app:
        return optionparser.error('data not provided.\n Usage: --url="path.to.appurl"')

    return { 'url' : option.app }


def main():
    # print __doc__

    appUrl = getAppUrl()

    print appUrl


if __name__ == '__main__':
    main()
