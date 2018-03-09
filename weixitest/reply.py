#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 10:24 2017/10/17 

@author: acer
'''
import time
from tuliing import reboot
import json
import chardet

class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        #获取图灵机器数据
        # content = reboot(content)
        rebootdata=reboot(content)
        dic_json = json.loads(rebootdata)
        self.code = dic_json['code']
        print self.code
        if self.code ==100000:
            print dic_json['text']
            self.__dict['Content'] = dic_json['text'].encode('utf-8')

        else:
            self.__dict['Title']=content
            self.__dict['Description'] = dic_json['text'].encode('utf-8')
            self.__dict['picurl'] = 'http://blog.yuxuefendou.cn:8080/static/media/uploads/2017/11/05/femgzl.jpg'
            self.__dict['Url']=dic_json['url'].encode('utf-8')

    def send(self):
        XmlForm1 = """
        <xml>
         <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
         <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
         <CreateTime>{CreateTime}</CreateTime>
         <MsgType><![CDATA[news]]></MsgType>
         <ArticleCount>1</ArticleCount>
         <Articles>
         <item>
         <Title><![CDATA[{Title}]]></Title> 
         <Description><![CDATA[{Description}]]></Description>
         <PicUrl><![CDATA[{picurl}]]></PicUrl>
         <Url><![CDATA[{Url}]]></Url>
         </item>
         </Articles>
        </xml>      
        """
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        if self.code ==100000:
            print self.__dict
            print XmlForm.format(**self.__dict)
            return XmlForm.format(**self.__dict)
        else:
            print XmlForm1.format(**self.__dict)
            return XmlForm1.format(**self.__dict)


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)


class EvenMsg(Msg):
    def __init__(self, toUserName, fromUserName, Event):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        # self.__dict['Event'] = Event
        print u'进入event事件处理：'
        # print chardet.detect(Event)
        # str ='abc'
        if Event == 'subscribe':
            # self.__dict['Content']='欢迎关注浴血奋斗微信公共号'
            # print self.Content
            # pass
            print 'hell4'
        elif Event == 'unsubscribe':
            print 'hell3'
            # pass
            # self.__dict['Content'] ='您已取消关注将清楚您所有记录'
            # print self.Content
        else:
            print 'hello1'
            # self.__dict['Content'] = str.encode('ascii')
            # print self.Content
            print 'hello'
    def send(self):
        XmlForm = """
         <xml>
         <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
         <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
         <CreateTime>{CreateTime}</CreateTime>
         <MsgType><![CDATA[text]]></MsgType>
         <Content><![CDATA[你好]]></Content>
         </xml>
         """
        print u'进入发送模块'
        print self.__dict
        # print self.Content
        print XmlForm.format(**self.__dict)
        return XmlForm.format(**self.__dict)