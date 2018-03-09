#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 16:44 2018/1/26 

@author: acer
'''


import urllib
import urllib2
import time
import xlrd

'''
urlRoot:请求根路径
cookie：登录系统后获取cookie值
today：当天时间
threeyearago：3年前时间
tenyearlater：10年后时间
'''
urlRoot='http://202.195.128.88:60080/'
cookie = 'JSESSIONID=670956507147E1447842B0AF9D03A28D; appliation-themeadmin=blue'
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
threeyearago = time.strftime('%Y-%m-%d', time.localtime(time.time() - 3600 * 25 * 365 * 3))
tenyearlater = time.strftime('%Y-%m-%d', time.localtime(time.time() + 3600 * 25 * 365 * 10))

def getEmployee(empname='',empjobnumber='',accountusername=''):
    '''
    :param empname: 员工名 '无名'
    :param empjobnumber: 员工编号 '532'
    :param accountusername: 员工账号 '532'
    :return: data post请求数据项，url 请求链接
    '''
    url =urlRoot+"120Manage/employee_saveEmployee.action"
    data = {'emp.name': empname,
            'emp.jobnumber': empjobnumber,
            'account.username': accountusername,
            'emp.pinyinShort': '',
            'emp.sex': '男',
            'account.password': '111111',
            'emp.departmentByDepartmentId.id': '1',
            'emp.timecard': '',
            'emp.jobPosition': '无',
            'emp_CJobType_id': '',
            'emp_CPositionType_id': 'xingzheng',
            'emp.isRegular': '1',
            'emp.nativePlace': '',
            'emp.politicalAffiliation': '其他',
            'emp.joinParty': threeyearago,
            'emp.degree': '',
            'emp.graduation': '',
            'emp.joinDate': '',
            'emp.isRefer': '1',
            'emp.presentJob': today,
            'emp.includeDate': today,
            'emp.drivingLicense': '',
            'emp.workPhone': '',
            'emp.homePhone': '',
            'emp.email': '',
            'emp.departmentByDepartmentId.id': '1',
            'emp.address': '',
            'emp.permanentResidenceAddress': '',
            'emp.emergencyContactPerson': '',
            'emp.emergencyContactRelation': '',
            'regularSalary.salary1': '0.0',
            'regularSalary.salary2': '0.0',
            'regularSalary.salary3': '0.0',
            'regularSalary.salary4': '0.0',
            'regularSalary.salary5': '0.0',
            'regularSalary.salary6': '0.0',
            'regularSalary.salary7': '0.0',
            'regularSalary.salary8': '0.0',
            'regularSalary.salary9': '0.0',
            'regularSalary.salary10': '0.0',
            'regularSalary.salary11': '0.0',
            'regularSalary.salary12': '0.0',
            'regularSalary.salary13': '0.0',
            'regularSalary.salary14': '0.0',
            'regularSalary.salary15': '0.0',
            'regularSalary.salary16': '0.0',
            'regularSalary.deduction1': '0.0',
            'regularSalary.deduction2': '0.0',
            'regularSalary.deduction3': '0.0',
            'regularSalary.deduction4': '0.0',
            'regularSalary.deduction5': '0.0',
            'regularSalary.deduction6': '0.0',
            'regularSalary.deduction7': '0.0',
            'emp.comments': '',
            }
    return data,url
def getHospital(hospitalaccountusername='',hospitalname=''):
    '''
    :param hospitalaccountusername: 医院账号 'gfyyy'
    :param hospitalname: 医院名称 '广附一'
    :return: data post请求数据项，url 请求链接
    '''
    url = urlRoot+"120Manage/hospital_addHospital.action"
    data = {
        'hospital.account.username': hospitalaccountusername,
        'hospital.account.password': '111111',
        'hospital.name': hospitalname,
        'hospital.specialty': '',
        'hospital.CHospitalLevel.id': '1a',
        'hospital.phone': '',
        'hospital.address': ''
    }
    return data,url
def getVehicleInfo(accountusername,maccountusername,vehicleplateNumber,assetsdepartmentid):
    '''
    :param accountusername: 车牌名（车牌号）'粤5221'
    :param maccountusername: 车辆MA账号名 'm5221'
    :param vehicleplateNumber: 车辆账号名 '5221'
    :param assetsdepartmentid: 所属分站 '121'
    :return: data post请求数据项，url 请求链接
    '''
    url = urlRoot+"120Manage/vehicle_addVehicle.action"
    data = {'account.username': accountusername,
            'maccount.username': maccountusername,
            'vehicle.plateNumber': vehicleplateNumber,
            'vehicle.weight': '',
            'vehicle.frameNo': '',
            'assets.accessionDate': today,
            'vehicle.phone': '',
            'vehicle.CVehicleUsage.id': '1st_line',
            'assets.location': '',
            'assets.location': '',
            'vehicle.propertyUnit': '',
            'vehicle.isSafeguard': '',
            'vehicle.comments': '',
            'account.password': '111111',
            'maccount.password': '111111',
            'vehicle.seating': '',
            'vehicle.engineNo': '',
            'assets.herstelldatum': threeyearago,
            'vehicle.model': '',
            'assets.factory': '',
            'assets.department.id': assetsdepartmentid,
            'vehicle.annualCheckDate': today,
            'vehicle.retirementDate': tenyearlater,
            }
    return data,url

def getDepartment(accountusername='',name=''):
    '''
    :param accountusername: 分站账号 'gfy'
    :param name: 分站名称 '广附一'
    :return: data post请求数据项，url 请求链接
    '''
    url = urlRoot+"120Manage/department_addSave.action"
    data = {
        'CDepartmentType.id': 'branch',
        'account.username': accountusername,
        'account.password': '111111',
        'password1': '111111',
        'name': name,
        'phone': '',
        'number': '',
        'deptManager.account.id': '',
        'comments': ''
    }
    return data,url

def add(data,url):
    try:
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', cookie))
        data = urllib.urlencode(data)
        f=opener.open(url, data)
        return f.read()
    except Exception as e:
        print e
        return "添加失败"

def analysisExcel(file='fie.xlsx',sheet=0):
    '''
    :param file: excle 文件位置 
    :param sheet: 第几个工作簿
    :return: table 工作簿内容
    '''
    try:
        data = xlrd.open_workbook(file)
        table = data.sheets()[sheet]
        return table
    except Exception as e:
        print e
        return 0
if __name__ == '__main__':

    table = analysisExcel('che.xls',0)
    # table = analysisExcel('zhangdian.xls',0)
    nrows= table.nrows
    i=1
    while i<nrows:
        info = table.row_values(i)
        if 5<len(info[0])<=7:
            vehicleplateNumber = str(info[0].encode('utf-8'))
            maccountusername = str('m' + info[0][1:].upper())
            accountusername = str(info[0][1:].upper())
            assetsdepartmentid =str(info[2])
            i=i+1
        elif len(info[0])==8:
            vehicleplateNumber=str(info[0].encode('utf-8'))
            maccountusername = str('mA'+info[0][-5:].upper())
            accountusername = str('A'+info[0][-5:].upper())
            assetsdepartmentid = str(info[2])
            i=i+1
        else:
            i=i+1
            continue
        print accountusername, maccountusername, vehicleplateNumber,assetsdepartmentid
        data,url = getVehicleInfo(accountusername,maccountusername,vehicleplateNumber,assetsdepartmentid)
        add_info=add(data,url)
        print add_info





    # while i<nrows:
    #   info = table.row_values(i)
    #   print info[3],info[4]
    #   accountusername= str(info[3])
    #   name = str(info[4].encode('utf-8'))
    #   i=i+1
    #   data,url = getDepartment(accountusername,name)
    #   # print data
    #   add_info = add(data,url)
    #   print add_info
    #

