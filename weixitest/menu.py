#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 15:03 2017/11/4 

@author: acer
'''
import urllib
from basic import Basic


class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            # print postData
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    # 获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
     {
        "button":
        [
            {
                "type": "location_select",
                "name": "我的位置",
                "key":  "rselfmenu_2_0"
            },
            

             {	
                  "type":"view",
                  "name":"我的博客",
                  "url":"http://blog.yuxuefendou.cn:8080/"
              },
            
            {
                "name": "微信博客",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "最近博客",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "日常生活",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "记录",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    }
                ]
            },
          ]
    }
    """
    accessToken = Basic().get_access_token()
    # myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
