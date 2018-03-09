#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 9:06 2017/10/18 

@author: acer
'''
# import re
#
# pattern = re.compile(r'hello')
#
# result1 = re.match(pattern,'hello')
# result2 = re.match(pattern,'hello0 XK!')
# print result1.group()
# print result2.group()




import re

# 匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')
