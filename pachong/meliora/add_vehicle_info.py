#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 9:49 2018/1/26 

@author: acer
'''

import urllib
import urllib2
import time

today= time.strftime('%Y-%m-%d',time.localtime(time.time()))
threeyearago = time.strftime('%Y-%m-%d',time.localtime(time.time()-3600*25*365*3))
threeyearlater = time.strftime('%Y-%m-%d',time.localtime(time.time()+3600*25*365*3))

# url = "http://202.195.128.88:60080/120Manage/vehicle!findAllVehicle.action"
url = "http://202.195.128.88:60080/120Manage/vehicle_addVehicle.action"
cookie = 'JSESSIONID=709E65C5D87E5173C4CF3B52368A639F; appliation-themeadmin=blue'
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie',cookie))

accountusername='粤5221'
maccountusername='m5221'
vehicleplateNumber='5221'
data={'account.username':accountusername,
      'maccount.username':maccountusername,
      'vehicle.plateNumber':vehicleplateNumber,
      'vehicle.weight':'',
      'vehicle.frameNo':'',
      'assets.accessionDate':today,
      'vehicle.phone':'',
      'vehicle.CVehicleUsage.id':'1st_line',
      'assets.location':'',
      'assets.location':'',
      'vehicle.propertyUnit':'',
      'vehicle.isSafeguard':'',
      'vehicle.comments':'',
      'account.password':'111111',
      'maccount.password':'111111',
      'vehicle.seating':'',
      'vehicle.engineNo':'',
      'assets.herstelldatum':threeyearago,
      'vehicle.model':'',
      'assets.factory':'',
      'assets.department.id':'49',
      'vehicle.annualCheckDate':today,
      'vehicle.retirementDate':threeyearlater,
      }
data = urllib.urlencode(data)
f= opener.open(url,data)
print f.read()