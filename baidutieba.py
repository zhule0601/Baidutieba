# -*- coding:utf-8 -*-
import time
import re
from bs4 import BeautifulSoup

import requests

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

time1 = time.clock()
def Spider (url):
    html = requests.get(url)
    selector = BeautifulSoup(html.text,'lxml')
    content_field = selector.find('div',class_='p_postlist').find_all('img',{'src':re.compile(r'http://imgsrc.+?sign.+?\.jpg')})

    for each in content_field:
        reply_info = each['src']

        print reply_info


if __name__=='__main__':

    for i in range(1,12):
        p = 'http://tieba.baidu.com/p/4940514362?pn='+str(i)
        print 'di',i
        Spider(url = p)

time4 = time.clock()
print time4-time1