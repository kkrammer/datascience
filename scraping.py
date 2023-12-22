# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 11:06:39 2023

@author: krame
"""
from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)
#page.text 

soup = BeautifulSoup(page.text, 'lxml')
#print (soup)

#tags
tag = soup.header.p.string
#print(tag)

#attributes
tag = soup.header.a
tag['attribute_new'] = 'this is new'
tag.attrs
print(tag.attrs)
#print(tag['data-toggle'])







