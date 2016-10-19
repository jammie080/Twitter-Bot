#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from settings import config
import os

class logger:
    def __init__(self):
        pass

    def write_data(self,filename,data=[]):
        src_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.abspath(src_dir + filename)

        with open(filename,'a') as users:
            users.write(data)
        

    def get_data(self,filename):
        self.data = []
        cur_path = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.abspath(cur_path + filename)

        with open(filename,'r') as users:
            for user in users:
                self.data.append(user)

        return self.data