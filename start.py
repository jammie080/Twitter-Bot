#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from twitter import twitter, user, search, logger, auth
from settings import config

class start:
    def __init__(self):
        self.set_up()

        self.twitter_scraped_users = self.logger.get_data(config.twitter['files']['twitter-users'])
        self.twitter_follow_users = self.logger.get_data(config.twitter['files']['follow-users'])
        self.twitter_dont_follow_users = self.logger.get_data(config.twitter['files']['dont-follow-users'])
        self.twitter_users = []


    def set_up(self):
        self.firefox_profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox()

        self.twitter = twitter.twitter(self.driver)
        self.twitter_user = user.user(self.driver)
        self.logger = logger.logger()
        self.auth = auth.auth(self.driver)

    def tear_down(self):
        self.driver.close()
        self.driver.quit()

    def auto_update(self):
        pass

    def bot(self):
        for user in self.twitter_scraped_users:
            if user not in self.twitter_follow_users:
                if user not in self.twitter_dont_follow_users:
                    self.twitter_users.append(user)
        #login in
        self.auth.login()
        
        i = 0
        try:
            while i < len(self.twitter_users):
                try:
                    print "[+] Profile : Username : {}".format(self.twitter_users[i])
                    print "[+] Profile : Protected : {}".format(self.twitter_user.is_protected(twitter_users[i]))
                    print "[+] Profile : Default pic : {}".format(self.twitter_user.is_default_pic(twitter_users[i]))
                    print "[+] Profile : Followers : {}".format(self.twitter_user.followers(twitter_users[i]))
                    print "[+] Profile : Following : {}".format(self.twitter_user.following(twitter_users[i]))
                    print "[+] Profile : Last Tweet : {} days ago".format(self.twitter_user.days_ago(twitter_users[i]))
                    self.twitter_user.follow_back_score(self.twitter_users[i])
                    i+=1
                except:
                    self.twitter_dont_follow_users.append(self.twitter_users[i])
                    self.logger.write_data(config.twitter['dont-follow-users'],self.twitter_users[i])
        except IndexError:
            self.tear_down()
        print "[+] Completed"
