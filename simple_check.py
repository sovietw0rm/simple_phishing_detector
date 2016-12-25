# coding: utf-8
import requests
from lxml import html
import sys
domain_file = sys.argv[1].strip()

def check(domain):
    try:
        content = requests.get('http://%s' % domain, timeout=30).text
    except:
        return False
    if content.find("HTTrack") >= 0:
        return True
    if content.find("giaidau.vn") >= 0:
        return True
    check1 = (content.find("zaloapp") >=0) or (content.find("garena") >=0 or (content.find("VIP CF") >= 0))
    try:
        tree = html.fromstring(content)
        actions = tree.xpath("//form/@action")
        if len(actions) > 0:
            for action in actions:
                if action.find(".php") > 0:
                    return (True and check1)
        return False
    except:
        print  "Fail", domain
        return False

if __name__ == '__main__':
    domains = open(domain_file, "r").readlines()
    for domain in domains:
        if check(domain.strip()):
            print domain.strip()
