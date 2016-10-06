#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from settings import config

class twitter(object):
    def __init__(self,driver):
       self.driver = driver
       self.driver.get('https://www.twitter.com/')

