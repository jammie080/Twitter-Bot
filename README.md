# Twitter-Bot Python
One day I was looking for a twitter bot or at least an open source one written in python. Found serveral but either it was out of date, discontinued or relayed heavy on twitters api. I didn't like this so I've decided to buid my own.
*Please note this a beta release and it's not ready for production yet. There'se many more things I need to
add before this can work properly. When I finish with most of the bugs I will ~~update~~ remove this message.*
<h4>Use at your risks until then....</h4>


# How to use
Okay so here's a quick write up on how to use this. 
make sure you go to settings and open config Replace 
```python
	
	#change these settings or this bot will stop working

    # Replace this
    TWITTER_USERNAME = ''
    TWITTER_PASSWORD = ''

    # with this
    TWITTER_USERNAME = yourusernamehere
    TWITTER_PASSWORD = yourpasswordhere

```

# How to install
Download the file from zip as is (Working on a setup folder)
Extract to any directory 

```html
pip install -U setuptools
pip install -r requirements.txt --upgrade
```

# Dependencies
* Python 2.7.*
* BeautifulSoup
* Selenium
* python-dotenv
* html5lib
* setuptools >= 28.2.0
* FireFox 46.0.1

# Example
Try out the test file
ex. test_file.py


```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from twitter import twitter, scrape, auth, logger, user, updater

```
# Scrape

<h4> Get User Followers </h4>

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from twitter import twitter, scrape, auth, logger, user, updater

firefox_profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile)

auth = auth.auth(driver)

auth.login()

scrape = scrape.scrape(driver)

scrape.user_followers(TWITER_HANDLE)
```
This creates a folder in twitter/output/TWITER_HANDLE/followers.txt

# Update
```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from twitter import twitter, scrape, auth, logger, user, updater

update = updater.updater()

update.check()
```
This will check for latest update on github

# To Do
* Clean up user_following code too much duplicate code
* Clean up folder structure
* Add more code examples to readme
* Start making document
* Port code over to linux
* Add setup file for automated installs (**current one is 42% complete**)

# Features coming soon
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
* ~~Auto Updater~~

# License
**[MIT](./LICENSE)**
&copy; 2016- </br>
Everything in this project is provided *as-is*

# About Project
<h4> Please note this is a work in progress and something I'm doing on my spare time. 
This Bot is built in a windows enviroment. Will port over to linux once most of the
functions has be added. </h4>
