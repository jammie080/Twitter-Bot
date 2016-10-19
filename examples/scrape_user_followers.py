#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,inspect

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0,parentdir)

from twitter import twitter, scrape, auth, logger, user, updater

firefox_profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile)

auth = auth.auth(driver)

auth.login()

scrape = scrape.scrape(driver)

scrape.user_followers('')