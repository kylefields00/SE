# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:26:18 2015

@author: kylefields00
"""

import requests
from bs4 import BeautifulSoup


def downloadUrl(url):
    headers = { 'User-Agent': 'PythonCrawler to Go v. 1.0'}
    r = requests.get(url, headers=headers)
    if r.status_code != 200: 
                   # status code 200 means there is a valid response.
        raise Exception("Not OKAY status code: {}".format(r.status_code))
    return r.text
    
    
def parseText(html):
    bs = BeautifulSoup(html)
    return bs.select('div.usertext-body')[1].text  #<-- must find correct 
                                                   #   element block
                                                   # for parsing to work
    
class Crawler(object):
    def __init__(self, start_url):
        self.start_url = start_url
     
    def crawl(self):
        current_page_url = self.start_url
        while True:
            current_page = downloadUrl(current_page_url)
            bs = BeautifulSoup(current_page)
            all_posts_links = bs.findAll('a',attrs={'class':'title'});  
            post_links = [Crawler._make_absolute_url(link['href']) for link in all_posts_links]
            
            
         
         ##static method not implemented yet.
        