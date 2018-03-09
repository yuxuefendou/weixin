#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 16:48 2017/10/20 

@author: acer
'''
import random
class Downloader:
    def __init__(self,delay=5,
                 user_agent='wswp',
                 proxies = None,
                 num_restries = 1,
                 cache = None):
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_restries
        self.cache = cache


    def __call__(self,url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries>0 and \
                    500 <=result['code']<600:
                    result = None


        if result is None:

            proxy = random.choice(self.proxies) if self.proxies else None

            headers = {'User-agent': self.user_agent}
            # result = self.dow


