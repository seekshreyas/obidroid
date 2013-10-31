obidroid
========

Obi Wan : "these aren't the droids that you are looking for"

Background:

Google’s Android platform is currently the most popular smartphone platform in the world, with over 50% of the market, and over 10 billion app downloads. Due in part to the platform’s popularity, Android malware is a pervasive and increasingly troublesome problem. At its most benign, Android malware consists of adware. More malicious Android malware can potentially steal user information, transmit GPS data, insert banking Trojans, send premium texts, or transform the phone into a bot to be used in a denial of service attack or spam campaign. Laboratory studies provide some background on user motivation in installing apps and granting permission. Users prefer apps requesting fewer permissions, yet certain factors such as brand popularity often sway them to make the opposite choice. A separate study observed low attention and comprehension rates in the majority of users when reading information about privacy policy and app permissions. Most noticeably, permissions and privacy information are not available on the primary Google Play store screen. By the time a user learns about the permissions required by the app, they have already made the decision to buy it.   


Proposal: 

 We aim to sift through the android app store applications and build a flagging system based on key features to indicate applications that may be engaging in malicious software/policy practices.
Some of the key features that could serve as indicators could be stars, user permission settings and key application features (to ascertain if the requirements meet the consequences) as well as user comment feedback of people who have reviewed and or used those applications. 
We aim to develop this as a set of heuristics that could be employed to develop and active flagging auditing of app stores to protect user’s interests. 

Some things to look at
- Apps from the same developer:  receive greater trust – so maybe the most popular app is benign, but a developer might put malware on a later app. Apps can also each contain a piece of malware which is activated when multiple apps are downloaded. Many developers also use the same key to sign.
- Malware targets trends – ie around the Olympic Games, a lot of malware snuck onto Olympic apps
- Stars?
- Negative sentiment (comments) and user removal
- Positive sentiment despite app giving out information/ containing malware (user is unaware)


