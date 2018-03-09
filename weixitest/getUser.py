#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 17:45 2017/11/5 

@author: acer
'''

from basic import Basic
import chardet
import urllib
import json

class User(object):
    def __init__(self):
        pass
    province=''
    city=''
    subscribe_time=''
    headimgurl=''
    language=''
    openid=''
    country=''
    tagid_list=[]
    remark=''
    sex=''
    subscribe=''
    nickname=''

    def __str__(self):
        return "用户的标识:"+self.openid.encode('utf-8')+'\n'+"用户昵称:"+self.nickname.encode('utf-8')+'\n'+\
            "用户所在城市:"+self.city.encode('utf-8')
    def getUser(self,accessToken):
        getUrl="https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s"%accessToken
        urlResp = urllib.urlopen(url=getUrl)
        return urlResp

    def getUserInfo(self,accessToken,openid):
        getUrl = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s"%accessToken+"&openid=%s"%openid+"&lang=zh_CN "
        # print getUrl
        urlResp = urllib.urlopen(url=getUrl)
        return urlResp

if __name__ == '__main__':
    user = User()
    accessToken = Basic().get_access_token()
    #获取用户列表
    user_json=user.getUser(accessToken)
    use_dic_json = json.load(user_json)
    print type(use_dic_json)
    print use_dic_json['data']['openid']
    user_list = use_dic_json['data']['openid']
    #获取用户信息
    for use_obj in user_list:
        userinfo_json=user.getUserInfo(accessToken,use_obj)
        userinfo_dic = json.load(userinfo_json)
        print userinfo_dic
        # print userinfo_dic['province']
        # print userinfo_dic['province'].encode('utf-8')
        # print json.load(useinfo_json)['country']
        # useinfo_dict = json.load(useinfo_json)
        user.city = userinfo_dic['city']
        user.nickname= userinfo_dic['nickname']
        user.openid= userinfo_dic['openid']
        user.country= userinfo_dic['country']
        user.nickname= userinfo_dic['nickname']
        user.nickname= userinfo_dic['nickname']
        user.nickname= userinfo_dic['nickname']
        user.nickname= userinfo_dic['nickname']
        user.nickname= userinfo_dic['nickname']
        print user


