#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0,parentdir)

from twitter import updater

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

update = updater.updater()

update.check()