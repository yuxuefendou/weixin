#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 15:29 2018/1/26 

@author: acer
'''

import urllib
import urllib2
import time

today= time.strftime('%Y-%m-%d',time.localtime(time.time()))
threeyearago = time.strftime('%Y-%m-%d',time.localtime(time.time()-3600*25*365*3))
threeyearlater = time.strftime('%Y-%m-%d',time.localtime(time.time()+3600*25*365*3))

# url = "http://202.195.128.88:60080/120Manage/vehicle!findAllVehicle.action"
url = "http://202.195.128.88:60080/120Manage/hospital_addHospital.action"
cookie = 'JSESSIONID=BF7BE7541699D76B6595566B9DA25F27; appliation-themeadmin=blue'
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie',cookie))

hospitalaccountusername='gfyyy'
hospitalname='广附一'
data={
    'hospital.account.username':hospitalaccountusername,
    'hospital.account.password':'111111',
    'hospital.name':hospitalname,
    'hospital.specialty':'',
    'hospital.CHospitalLevel.id':'1a',
    'hospital.phone':'',
    'hospital.address':''
      }
data = urllib.urlencode(data)
f= opener.open(url,data)
print f.read()