#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from settings import config
import version
import time,os,requests
from os import rmdir, listdir
from os.path import join
from bs4 import BeautifulSoup
import re
import zipfile
from shutil import move

class updater:
    def __init__(self):
        self.version = self.client_version()
        self.serverVersion = self.server_version()

    def check(self):
        
        if self.version != self.serverVersion:
            if self.version <= self.serverVersion:
                print "Update available"
                print "Current version {}".format(self.serverVersion)
                print "Downloading update"
                self.download('https://github.com/jammie080/Twitter-Bot/archive/master.zip')
                if os.path.isfile('Twitter-Bot.zip'):
                    os.remove('Twitter-Bot.zip')
                os.rename('master.zip','Twitter-Bot.zip')
                self.setup('Twitter-Bot.zip')
        else:
            print "Latest Update"
            print "Current version {}".format(self.version)

    def download(self,url):
        
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter
        browser = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in browser.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return local_filename
    
    def backup(self):
        pass

    def setup(self,filename):
        fh = open(filename, 'rb')
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            os.chdir('..')
            src_dir = os.path.abspath(os.curdir)
            z.extract(name, src_dir)
        fh.close()
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(os.path.dirname(dname))
       
      
        for filename in listdir(join(src_dir, 'Twitter-Bot-Master')):
            move(join(src_dir, 'Twitter-Bot-Master', filename), join(src_dir, filename))
        rmdir(src_dir + '\Twitter-Bot-Master')
        

    def client_version(self):
        current_version = version.__version__
        return current_version

    def server_version(self):
        browser = requests.get('https://github.com/jammie080/Twitter-Bot/releases/latest')
        soup = BeautifulSoup(browser.content,"html5lib")
        m = re.search(r"(v\d.\d.\d.\d|v\d.\d.\d)",soup.title.encode('utf-8'))
        serverVersion = m.group()
        return serverVersion