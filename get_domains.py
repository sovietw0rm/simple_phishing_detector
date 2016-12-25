# coding: utf-8
from lxml import html
import requests
import datetime
import os.path
from time import sleep
while True:
    today = datetime.datetime.now()
    month = today.month
    year = today.year
    day = today.day
    print year
    print month
    print day
    if os.path.exists("output/domains%d%d%d.txt" % (year, month, day - 1)):
        sleep(2 * 60 * 60)
        continue
    keywords = open("vn_keywords.txt", "r").readlines()
    for i in range(1,6000,1):
        content = requests.get('http://wschg.com/new/%d/%d/%d/page-%d.html' % (year, month, day - 1, i)).text
        print i
        tree = html.fromstring(content)
        domains = tree.xpath('//tr/td/a/text()')
        if len(domains) < 1:
            break
        for d in domains:
            open("output/domains%d%d%d.txt" % (year, month, day - 1), "a").write(d.lower())
            c = d.lower()
            for k in keywords:
                if c.find(k.strip()) > -1:
                    open("check/domains%d%d%d.txt" % (year, month, day - 1), "a").write(c)
                    break
    sleep(60 * 60)
