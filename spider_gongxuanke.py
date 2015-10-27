# -*- coding: utf-8 -*-
import urllib2
import bs4

import spider_base

opener = spider_base.base()

base_url = 'http://210.42.121.132/stu/choose_PubLsn_list.jsp?pageNum='
raw_file = open('data_gongxuanke', 'w')

for i in range(1, 23):
    lsn_url = base_url + str(i)
    # print lsn_url
    req = urllib2.Request(url=lsn_url)
    page = opener.open(req).read().replace('\n', '').replace('\t', '').replace('\r', '')
    soup = bs4.BeautifulSoup(''.join(page))
    tr = soup.table.findAll('tr')
    for j in range(1, len(tr)):
        info = ''
        td = tr[j].findAll('td')
        info += td[0].string.encode('utf-8').replace(' ', '') + ','
        info += td[1].string.encode('utf-8').replace(' ', '') + ','
        info += td[3].string.encode('utf-8').replace(' ', '') + ','
        tip = td[9].div.string.encode('utf-8').replace(' ', '').replace(':', ',').replace(';', ',')
        tip = tip.replace(u'星期', '').replace(u'每', '').replace(u'节', '').replace(u'周', '').replace(u'区', '')
        tip = tip.replace(u'一', '1').replace(u'二', '2').replace(u'三', '3').replace(u'四', '4')
        tip = tip.replace(u'五', '5').replace(u'六', '6').replace(u'日', '0')
        tip = tip.replace('4,01', '4,1-').replace('4,02', '4,2-').replace('4,03', '4,3-').replace('4,04', '4,4-')
        tip = tip.replace('4,05', '4,5-').replace('4,06', '4,6-').replace('4,07', '4,7-')
        tip = tip.replace(u',老外', u',老外-')
        while len(tip.split(',')) < 7:
            tip += ','
        info += tip
        info += td[10].div.string.encode('utf-8').replace(' ', '') + ','
        info += td[11].input['id'].encode('utf-8').replace(' ', '') + '\n'
        raw_file.write(info)
    print str(i)
raw_file.close()
