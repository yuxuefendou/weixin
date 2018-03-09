# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
url = 'https://www.qiushibaike.com/article/118990772'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    # print content
    pattern = re.compile('<div.*?'+
                         'content-text">(.*?)</div>',re.S)
    items = re.findall(pattern,content)
    print items
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

