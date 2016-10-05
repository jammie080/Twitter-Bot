#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from twitter import scrape,updater

"""
firefox_profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile)
twitter = scrape.scrape(driver)

twitter.user_followers('sallybeauty')
"""
update = updater.updater()
update.check()