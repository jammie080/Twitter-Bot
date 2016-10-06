#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from settings import config
import logger
import auth
from bs4 import BeautifulSoup
import time,os
import os.path


class scrape():
    def __init__(self,driver):
        self.driver = driver
        self.browser = self.driver
        self.logger = logger.logger()
        self.auth = auth.auth(self.driver)
        self.data = []
        self.user_data = []

    def html(self,user_id,url):
        oldData = self.data
        newData = ""

        if (user_id not in self.user_data):
            self.browser.get(url)
            self.data = self.browser.page_source
            self.user_data.append(user_id)
            #print "Using new data"
       
        else:
            self.data = oldData
            #print "Using old Data"
        return self.data

    def filter_data(self,user_id,url):
        soup = BeautifulSoup(self.html(user_id,url),"html.parser")
        return soup

    def user_followers(self,user_id):
        
        USER_FOLLOWERS = self.logger.get_data("\\output\\Follow\\{}\\followers.txt".format(user_id))
        NOW_FOLLOW = []
        ALL_TARGETS = []

        if self.auth.check() != False:
            try:
                filename = "\\output\\Follow\\{}".format(user_id)
                src_dir = os.path.dirname(os.path.realpath(__file__))
                filename = os.path.abspath(src_dir + filename)
                if not os.path.exists(filename):
                    os.makedirs(filename)
                else:
                    print "[+] {} Folder created".format(user_id)

                filename = "\\output\\Follow\\{}\\followers.txt".format(user_id)
                src_dir = os.path.dirname(os.path.realpath(__file__))
                filename = os.path.abspath(src_dir + filename)
                if not os.path.isfile(filename):
                    followers_txt = open(filename,"a")
                    followers_txt.write('')
                    followers_txt.close()
            except:
                pass
            self.filter_data(user_id,"https://twitter.com/%s/followers" % user_id)
            #self.scroll_page(0,50)

            profile = self.browser.find_elements_by_class_name("ProfileCard-screenname")
            for links in profile:
                link = links.find_elements_by_class_name("u-linkComplex")
                for targets in link:
                    all_targets = targets.find_elements_by_class_name("u-linkComplex-target")
                    for a_target in all_targets:
                        print a_target.text
                        ALL_TARGETS.append(a_target.text)

            
            for target in ALL_TARGETS:
                if target not in USER_FOLLOWERS:
                    if '#' not in target:
                        if target not in NOW_FOLLOW:
                            if target != '':
                                if target != user_id:
                                    self.logger.write_data("\\output\\Follow\\{}\\followers.txt".format(user_id),target + '\n')
                                    NOW_FOLLOW.append(target)
                    print "[+] Profile : %s : Added" % target
                else:
                    print "[+] Profile : %s : Added Already" % target.text

    def scroll_page(self,min_scroll=0,max_scroll=50):
        self.min_scroll = min_scroll
        self.max_scroll = max_scroll
        print "[+] Scroll : Started"
        print "[+] Scroll : {}".format(self.max_scroll)
        while self.min_scroll < self.max_scroll:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(.1)
            self.min_scroll += 1
        print "[+] Scroll : Completed"
