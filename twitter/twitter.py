#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import Hack
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0,parentdir)

from settings import config

class twitter(object):
    def __init__(self,driver):
       self.driver = driver
       self.driver.get('https://www.twitter.com/')

