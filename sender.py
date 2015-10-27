import urllib
import urllib2
import cookielib

data_file = open('data_zhuanyeke', 'r')
url = ''
step = 0
begin = 0
while True:
    step += 1
    data = data_file.readline()
    data_arr = data.split(',')
    if step < begin or len(data_arr) < 11 or not data_arr[7] or not data_arr[8]:
        continue
    if not data:
        break
    postdata = urllib.urlencode({'info': data})
    req = urllib2.Request(url=url, data=postdata)
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    status = result.read()
    print '%s   %d' % (status, step)
