# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import re
import bs4

_id = ''
pwd = ''

def base():
    
        # 获取验证码图片，伪造启动器opener，在其中保存cookie
        img_url = 'http://210.42.121.132/servlet/GenImg'
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        req = urllib2.Request(url=img_url)
        img_code = opener.open(req)
        img_file = open('img.jpg', 'wb+')
        img_file.write(img_code.read())
        img_file.close()
        
        # 模拟登入
        token = raw_input()
        web_url = 'http://210.42.121.132/servlet/Login'
        postdata = urllib.urlencode({'id': _id, 'pwd': pwd, 'xdvfb': token})
        req = urllib2.Request(url=web_url, data=postdata)
        result = opener.open(req)
        if result.geturl() == web_url:
            print 'Failed'
        else:
            print 'Successful'

        return opener
