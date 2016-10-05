#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from settings import config
import logger
import auth
from bs4 import BeautifulSoup
import time,os


class scrape():
    def __init__(self,driver):
        self.driver = driver
        self.browser = self.driver
        self.logger = logger.logger()
        self.auth = auth.auth(self.driver)
        self.data = []
        self.user_data = []

    def html(self,user_id):
        oldData = self.data
        newData = ""

        if (user_id not in self.user_data):
            self.browser.get("https://www.twitter.com/{}".format(user_id))
            self.data = self.browser.page_source
            self.user_data.append(user_id)
            #print "Using new data"
       
        else:
            self.data = oldData
            #print "Using old Data"
        return self.data

    def filter_data(self,user_id):
        soup = BeautifulSoup(self.html(user_id),"html.parser")
        return soup

    def user_followers(self,user_id):
        self.auth.login()
        if self.auth.check() != False:
            try:
                self.logger.get_data('\\output\\Follow\\{}\\followers.txt'.format(user_id))
                pass
            except:
                if not os.path.isdir("\\output\\Follow\\%s" % user_id):
                    os.makedirs("\\output\\Follow\\%s" % user_id)
                self.logger.write_data('\\output\\Follow\\{}\\followers'.format(user_id),'')
                pass

            self.scroll_page(0,50)

            all_targets = self.browser.find_elements_by_class_name("u-linkComplex-target")
            USER_FOLLOWERS = self.logger.get_data('\\output\\Follow\\{}\\followers.txt'.format(user_id))
            NOW_FOLLOW = []
            
            for a_target in all_targets:
                if a_target.text not in USER_FOLLOWERS:
                    if '#' not in a_target.text:
                        if a_target.text not in NOW_FOLLOW:
                            if a_target.text != '':
                                self.logger.write_data('\\output\\Follow\\{}\\followers.txt'.format(user_id),a_target.text + '\n')
                                NOW_FOLLOW.append(a_target.text)
                    print "[+] Profile : %s : Added" % a_target.text
                else:
                    print "[+] Profile : %s : Added Already" % a_target.text

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
