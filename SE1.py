# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:01:49 2015

@author: kylefields00
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
    
class Crawler(object): 
    def __init__(self, start_url):
        self.start_url = start_url
        
    @staticmethod
    def _make_absolute_url(url):
        return 'http://reddit.com' + url
        
    def crawl(self):
        current_page_url = self.start_url
        while True:
            
        current_page = downloadUrl(current_page_url)
        bs = BeautifulSoup(current_page)
        all_posts_links = bs.findAll('a',attrs={'class':'title'});  
        post_links = [Crawler._make_absolute_url(link['href']) for link in all_posts_links]
        
