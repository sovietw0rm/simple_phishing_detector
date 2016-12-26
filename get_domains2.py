import requests
from lxml import html
import os

while True:
    keywords = open("vn_keywords.txt", "r").readlines()
    content = requests.get('http://domains-by-day.com').text
    tree = html.fromstring(content)
    latest = tree.xpath('//table/tr/td/a/@href')[0].split('/')[1]
    if os.path.exists("output/domains%s.txt" % latest.replace('-', '')):
        sleep(60 * 60)
        continue
    for i in range(6000):
        content = requests.get('http://domains-by-day.com/%s/domains-%d.html' % (latest, i)).text
        tree = html.fromstring(content)
        domains = tree.xpath('//tr')
        if len(domains) < 10:
            break
        for domain in domains:
            temp = domain.xpath('td/a')
            if len(temp) < 1:
                continue
            b = temp[0].xpath('text()')
            open("output/domains%s.txt" % latest.replace('-', ''), "a").write(b[0].lower() + "\n")
            c = b[0].lower()
            for k in keywords:
                if c.find(k.strip()) > -1:
                    open("check/domains%s.txt" % latest.replace('-', ''), 'a').write(c  + "\n")
                    break
    sleep(60 * 60)
