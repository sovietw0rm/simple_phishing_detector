# coding: utf-8

import idna
import unicodedata
import sys

domain_file = sys.argv[1].strip()

'''
THRESHOLD = 0.3
def compare(domain1, domain2):
    if len(domain1) != len(domain2):
        return False
    count = 0
    for i in range(len(domain1)):
        if domain1[i] != domain2[i]:
            count += 1
    if count < THRESHOLD * len(domain1):
        return True
    return False
'''
#ascii flooding
def unicode_to_ascii(data):
    return unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')

def compare(domain1, domain2):
    if len(domain1) != len(domain2):
        return False
    if unicode_to_ascii(domain1) == unicode_to_ascii(domain2):
        return True
    return False

domains = open(domain_file, "r").readlines()

checks = [u"google.com", u"apple.com", u"ebay.com", u"amazon.com", u"icloud.com", u"paypal.com", u"microsoft.com", u"gmail.com", u"yahoo.com", u"facebook.com", u"twitter.com", u"instagram.com", u"youtube.com"]

for domain in domains:
    #only check unicode domains
    if not domain.find('xn--') == 0:
        continue
    try:
        for check in checks:
            if compare(idna.decode(domain.strip()), check):
                print idna.decode(domain.strip()), domain.strip()
    except:
        continue
