#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path, sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from twitter import scrape,updater, auth

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox_profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile)

auth = auth.auth(driver)

auth.login()

scrape = scrape.scrape(driver)

scrape.user_followers('test')
