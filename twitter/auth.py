#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from settings import config
from bs4 import BeautifulSoup
import time, os

class auth:
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        self.driver.get(config.twitter['url']['home'])

        username = self.driver.find_element_by_class_name("js-username-field")
        password = self.driver.find_element_by_class_name("js-password-field")

        username.send_keys(config.twitter['auth']['twitter']['username'])
        username.send_keys(config.twitter['auth']['twitter']['password'])

        self.driver.find_element_by_css_selector("button.submit.btn.primary-btn").click()

    def check(self):
        return True