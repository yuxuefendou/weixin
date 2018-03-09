#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 22:56 2017/10/19 

@author: acer
'''
import re
from test2 import download
def crawl_sitemap(url):
    sitemap = download(url)
    print sitemap
    links = re.findall('<loc>(.*?)</loc>',sitemap)

    for link in links:
        html = download(links)


if __name__ == '__main__':
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')