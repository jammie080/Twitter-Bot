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

scrape.user_followers('sallybeauty')