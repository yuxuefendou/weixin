#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 12:14 2018/1/26 

@author: acer
'''

import urllib
import urllib2
import time

today= time.strftime('%Y-%m-%d',time.localtime(time.time()))
threeyearago = time.strftime('%Y-%m-%d',time.localtime(time.time()-3600*25*365*3))
threeyearlater = time.strftime('%Y-%m-%d',time.localtime(time.time()+3600*25*365*3))
# url = "http://202.195.128.88:60080/120Manage/vehicle!findAllVehicle.action"
url = "http://202.195.128.88:60080/120Manage/employee_saveEmployee.action"
cookie = 'JSESSIONID=BF7BE7541699D76B6595566B9DA25F27; appliation-themeadmin=blue'
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie',cookie))

empname='无名'
empjobnumber='532'
accountusername='532'
data={'emp.name':empname,
      'emp.jobnumber':empjobnumber,
      'account.username':accountusername,
      'emp.pinyinShort':'',
      'emp.sex':'男',
      'account.password':'111111',
      'emp.departmentByDepartmentId.id':'1',
      'emp.timecard':'',
      'emp.jobPosition':'无',
      'emp_CJobType_id':'',
      'emp_CPositionType_id':'xingzheng',
      'emp.isRegular':'1',
      'emp.nativePlace':'广州',
      'emp.politicalAffiliation':'其他',
      'emp.joinParty':threeyearago,
      'emp.degree':'',
      'emp.graduation':'',
      'emp.joinDate':'',
      'emp.isRefer':'1',
      'emp.presentJob':today,
      'emp.includeDate':today,
      'emp.drivingLicense':'',
      'emp.workPhone':'',
      'emp.homePhone':'',
      'emp.email':'',
      'emp.departmentByDepartmentId.id':'1',
      'emp.address':'',
      'emp.permanentResidenceAddress':'',
      'emp.emergencyContactPerson':'',
      'emp.emergencyContactRelation':'',
      'regularSalary.salary1':'0.0',
      'regularSalary.salary2':'0.0',
      'regularSalary.salary3':'0.0',
      'regularSalary.salary4':'0.0',
      'regularSalary.salary5':'0.0',
      'regularSalary.salary6':'0.0',
      'regularSalary.salary7':'0.0',
      'regularSalary.salary8':'0.0',
      'regularSalary.salary9':'0.0',
      'regularSalary.salary10':'0.0',
      'regularSalary.salary11':'0.0',
      'regularSalary.salary12':'0.0',
      'regularSalary.salary13':'0.0',
      'regularSalary.salary14':'0.0',
      'regularSalary.salary15':'0.0',
      'regularSalary.salary16':'0.0',
      'regularSalary.deduction1':'0.0',
      'regularSalary.deduction2':'0.0',
      'regularSalary.deduction3':'0.0',
      'regularSalary.deduction4':'0.0',
      'regularSalary.deduction5':'0.0',
      'regularSalary.deduction6':'0.0',
      'regularSalary.deduction7':'0.0',
      'emp.comments':'',
      }
data = urllib.urlencode(data)
f= opener.open(url,data)
print f.read()