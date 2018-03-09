#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 11:02 2018/1/26 

@author: acer
'''

import time
import  xdrlib,sys
import  xlrd

data = xlrd.open_workbook('file.xlsx')

table = data.sheets()[1]

# print table.nrows
i=0
nrow=table.nrows
while i<nrow:
    for info in  table.row_values(i):
        print info,
    print
    i=i+1
# today= time.strftime('%Y-%m-%d',time.localtime(time.time()))
# threeyearago = time.strftime('%Y-%m-%d',time.localtime(time.time()-3600*25*365*3))
# threeyearlater = time.strftime('%Y-%m-%d',time.localtime(time.time()+3600*25*365*3))
# print threeyearago
# print threeyearlater


