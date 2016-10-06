#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from settings import config
import scrape, logger
from datetime import datetime

class user(object):
    def __init__(self,driver):
        self.scrape = scrape.scrape(driver)
        self.logger = logger.logger()
        self.url = "https://www.twitter.com/"

    def is_protected(self,user_id):
        soup = self.scrape.filter_data(user_id,self.url+user_id)
        is_protected = ""

        try:
            protected = soup.find('span',class_="Icon--protected")
            protects = protected.find('span',class_="u-hiddenVisually")
            if "Protected Tweets" in protects.text:
                return True
        except:
            return False

    def follow_back_score(self,user_id):
        followers = self.followers(user_id)
        following = self.following(user_id)
        profile_pic = self.is_default_pic(user_id)
        protected = self.is_protected(user_id)
        last_tweet = self.last_tweeted_more_than(user_id,4)
        days_ago = self.days_ago(user_id)
        
        try:
            ratio = float(followers.encode('utf-8')) / float(following.encode("utf-8"))
            self.ratio = ratio
            if (ratio > .60 and ratio < 1.20):
                if (following >= followers or ratio < 1.20):
                    ratio *= 100
                    print "[+] Profile : Ratio : {0:000.0f}%".format(ratio)

                    if (profile_pic != True):
                        if (protected != True):
                            if (last_tweet != True):
                                print "[+] Profile : add to list \n"
                                self.logger.write_data(config.twitter['files']['follow-users'],user_id)
                            else:
                                print "[+] Profile : Don't follow \n"
                                self.logger.write_data(config.twitter['files']['dont-follow-users'],user_id)
            else:
                ratio *= 100
                print "[+] Profile : Ratio : {0:000.0f}%".format(ratio)
                print "[+] Profile : Don't follow \n"
                self.logger.write_data(config.twitter['files']['dont-follow-users'],user_id)
        except:
            self.ratio *= 100
            print "[+] Profile : Ratio : {0:000.0f}%".format(self.ratio)
            print "[+] Profile : Don't follow \n"
            self.logger.write_data(config.twitter['files']['dont-follow-users'],user_id)

    def is_default_pic(self,user_id):
        soup = self.scrape.filter_data(user_id,self.url+user_id)
        profile_pic = soup.find('img',class_="ProfileAvatar-image")
      
        if "default_profile_images" in profile_pic["src"]:
            return True
        else:
            return False

    def followers(self,user_id):
        soup = self.scrape.filter_data(user_id,self.url+user_id)
        try:
            profile_nav = soup.find('li',class_="ProfileNav-item--followers")
            profile_stats = profile_nav.find('a',class_="ProfileNav-stat")
            followers = profile_stats.find('span',class_="ProfileNav-value")
            
            if "K" in followers.text:
                
                followers = profile_nav.find('a',{"class":"ProfileNav-stat"})['title']
                followers = followers.encode('utf-8').replace(",","")
                followers = followers.encode('utf-8').replace(" Followers","")
            else:
                followers = followers.text
                followers = followers.encode('utf-8').replace(",","")
        except:
            followers = 0.0
        return followers

    def following(self,user_id):
        soup = self.scrape.filter_data(user_id,self.url+user_id)

        try:
            profile_nav = soup.find('li',class_="ProfileNav-item--following")
            profile_stats = profile_nav.find('a',class_="ProfileNav-stat")
            followers = profile_stats.find('span',class_="ProfileNav-value")
            
            if "K" in followers.text:
                
                followers = profile_nav.find('a',{"class":"ProfileNav-stat"})['title']
                followers = followers.encode('utf-8').replace(",","")
                followers = followers.encode('utf-8').replace(" Following","")
            else:
                followers = followers.text
                followers = followers.encode('utf-8').replace(",","")
        except:
            followers = 0.0
        return followers

    def last_tweet(self,user_id):
        soup = self.scrape.filter_data(user_id,self.url+user_id)
        last_tweet = soup.find("p",class_="tweet-text")
        return last_tweet.text 

    def last_tweet_date(self,user_id):
        soup = self.scrape.filter_data(user_id,self.url+user_id)
        try:
            date_time = soup.find('small',class_="time")
            date = date_time.find('a',class_="tweet-timestamp")
            date_a = date.find('span',class_="_timestamp")
            timestamp = date_a['data-time']
        except:
            timestamp = 1453291262
        return timestamp

    def last_tweeted_more_than(self,user_id,days=3):
        mytime = self.last_tweet_date(user_id)
        date = datetime.fromtimestamp(float(mytime))
        if(datetime.today() - date).days > days:
            
            return True 
        else:
            return False

    def days_since_last_tweet(self,user_id):
        mytime = self.last_tweet_date(user_id)
        date = datetime.fromtimestamp(float(mytime))
        today = datetime.today()
        diff = today - date
        days_ago = diff.days
        return days_ago

    def days_ago(self,user_id):
        mytime = self.last_tweet_date(user_id)
        date = datetime.fromtimestamp(float(mytime))
        today = datetime.today()
        diff = today - date
        days_ago = diff.days
        return days_ago