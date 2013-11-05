_i256 Applied NLP_ : Project Proposal


OBIDROID :: "These aren't the Droids you're looking for"
========================================================

## Team Members & Roles


| Team Members | Team Roles | Contact |
|:-------------|:-----------|:--------|
| Luis Aguilar | Coding & Development | luis@berkeley.edu |
| Shreyas | Coding & Development | shreyas@ischool.berkeley.edu |


## Background
Google's Android platform is currently one of the most popular smartphone platforms in the world, with over 81% market share [^note-1] and over 10 billion app downloads. Due in part to platform's popularity, Android malware is a pervasive and increasingly troublesome problem.

At its most benign, Android malware consists of adware. More malicious Android malware can potentially steal user information, transmit GPS data, insert banking Trojans, send premium texts, or transform the phone into a bot to be used in a denial of service attack or spam campaign. Also, there could be times where popular, fair apps might be indulging in practices of unfainess [^note-2] & deception [^note-3], which most users may not even be aware of. 

FTC tries to protect the users against such apps by enforcing their policies of unfairness and deception. But this process is still passive. Because of the scale of the app store, the FTC relies on user complaints to examine an application, and hence it is a passive activity not an active pursuit of __unfair__ applications. 



## Project Details
We aim to examine an app based on its description and user reviews to sift through a large collection of applications and flag applications that are indulging in unfair practices. We aim to flag the applications based on user grievances. 

Some of the indicators could be:

- App description
- User reviews

We aim to examine the above largely through sentiment analysis, aided by information extraction about features that are being talked about in the conversation and cross-checking it with description of the app, if that is an indicator of an unfair practice. For eg, a _torch_ app for android may be a popular app, and the sentiment around it could largely positive, but if a few negative comments raise concern about its contact list hijack practice, it should be flagged. But we do wish to account for the fact that _all negative_ comments do not amount to a grievance. 



## Project Goals
Our main aim is develop a __filter__ system for flagging _unfair_ apps, via customer reviews and app descriptions. 
We do not aim to _predict_ if an app is unfair or not using the reviews/description. Instead we aim to help scale down the problem of policing every app periodically on the app store by building a good indicator/flagging system.



## Assessment of Project Goals

#### Acceptable Ground Rules

- From our point of view, we would like to aim for casting a wider net overall so as to flag most of the potentially unfair apps. Hence, __False Positives__ for good apps that may be flagged for closer view is an acceptable scenario.
- Also, if an unfair app doesn't have sufficient user reviews, it would be hard to ascertain their unfairness.

#### Assessment Scenarios
- a known malware with sufficient user reviews indicating user grievances should not be missed.
- the tool should be _sustainable_ as the user reviews are updated often, and it should be able to apply the assessment metrics periodically 
- The assessment of our tool should be examined in overall general category of apps as well as in individual app categories like _games_ etc


## Deliverables
- Since there is no public API for accessing data about Android App Store apps, we have to build a 
    - _crawler_ : to be able to crawl and compile a list of apps in overall and general categories periodically from the app store
    - _scraper_ : to be able to take a list of Android apps and scrape their significant features (app description & user reviews)
    - _analyzer_ : analyze each app on a NLP based metrics to assess if assess grievances of users.
    - _metric/rubric_ : a set of metrics that are being employed to assess the unfairness of apps. 


#### Work Breakdown 
| Task | Description | Duration (week(s)) |
|:-----|:------------|-------------------:|
| Project Scaffolding | Crawler & Scraper Scaffolding, DataBase Design | 1 week |
| Labeling & Feature Extraction | Create Training Set with manually attached labels, extract features | 1 week |
| Develop Feature Models | Develop models for supervised classification | 2 week |
| Finalization | Assessment & finalization | 1 week |



## Declaration

This project is being jointly pursued by [Luis Aguilar], [Kristine A Yoshihara] & [Shreyas] in [Info 219 Privacy, Security & Cryptography](http://www.ischool.berkeley.edu/courses/i219) under the guidance of Prof Doug Tygar.


[^note-1]: [Android takes record smartphone share at expense of iPhone and BlackBerry](http://www.theguardian.com/technology/2013/oct/31/android-record-smartphone-share-iphone-blackberry)

[^note-2]: __FTC Unfairness__: What is Deception? Representation, omission or practice that is likely to mislead the consumer; __Perspective of 'Reasonableness'__ - if the practice affects a certain group, then evaluate reasonableness from the perspective of that group; __'Material'__ - does it affect customer decision with regard to a product or service

[^note-3]: __FTC Deception__ practices that cause or are likely to cause substantial injury to consumers that are not outweighed by the benefits to consumers or competition and are not reasonably avoided by consumers.

[Luis Aguilar]: luis@berkeley.edu
[Kristine A Yoshihara]: 100kristine@berkeley.edu
[Shreyas]: shreyas@ischool.berkeley.edu