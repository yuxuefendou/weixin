#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 18:39 2017/9/24 

@author: acer
'''
import web
import os
from handle import Handle

urls = (
    '/', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

