# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:01:49 2015

@author: gridxkl
"""

import requests
from bs4 import BeautifulSoup

def downloadUrl(url):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Not OKAY status code: {}".format(r.status_code))
    return r.text
def parseText(html):
    bs = BeautifulSoup(html)
    return bs.select('div.article')[0].text
    