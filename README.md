# Twitter-Bot Python
One day I was looking for a twitter bot or at least an open source one written in python. Found serveral but either it was out of date, discontinued or relayed heavy on twitters api. I didn't like this so I've decided to buid my own.


# How to use
Okay so here's a quick write up on how to use this. 
make sure you go to settings and open config Replace 
```python
    # Replace this
    TWITTER_STUFF["TWITTER_USERNAME"]
    TWITTER_STUFF["TWITTER_PASSWORD"]

    # with this
    TWITTER_STUFF["TWITTER_USERNAME"] = yourusernamehere
    TWITTER_STUFF["TWITTER_PASSWORD"] = yourpasswordhere

```
<h2> change these settings or this bot will stop working </h2>

# How to install
Download the file from zip as is (Working on a setup folder)
Extract to any directory 

```python
pip install -r requirements.txt
```

# Dependencies
* Python 2.7.*
* BeautifulSoup
* Selenium
* python-dotenv

# Example
Make a test file in the same folder as the start file
ex. test.py

insert the following

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from twitter import twitter, scraper, auth, logger, user, updater

firefox_profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile)
```
# Scrape
```python
auth = auth.auth(driver)

auth.login()

scrape = scrape.scrape(driver)

scrape.user_followers(TWITER_HANDLE)
```
This creates a folder in twitter/output/TWITER_HANDLE/followers.txt

# To Do
* Clean up user_following code too much duplicate code
* Clean up folder structure
* Add more code examples to readme
* Start making document
* Port code over to linux
* Add setup file for automated installs (**current one is 42% complete**)

# Features comming soon
* Proxy support
* Headless support
* Disable images to save memory
* Profile support
* Custom browser support
* Save organized data to excel (Username, Follower_count, Following_count) ect.
* Follow by keyword
* Auto Unfollower
* Auto add to blacklist
* Auto Like tweet
* Auto Favorite
* Advance Scraper
* Auto Updater

# About Project
<h4> **Please note this is a work in progress and something I'm doing on my spare time. 
This Bot is built in a windows enviroment. Will port over to linux once most of the
functions has be added. </h4>