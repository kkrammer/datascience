# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:58:47 2023

@author: krame
"""

from bs4 import BeautifulSoup
import lxml
import requests
import re 

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

#print(page)

soup = BeautifulSoup(page.text, 'lxml')

#print(soup)
#find()
soup.find('div',{'class':'container test-site'})
#print(soup.find('div',{'class':'container test-site'}))
soup.find('h4',{'class':'pull-right price'})
#print(soup.find('h4',{'class':'pull-right price'}))

#print(soup.find('h4', class_ =  'pull-right price'))

price = soup.find_all('h4',{'class':'pull-right price'})[6:]
title = soup.find_all('a',{'class':'title'})
soup.findAll('p', class_ = 'pull-right')


print(price)


#find_all part 2
soup.findAll(['h4','p'])
soup.findAll(id = True)
soup.findAll(string = 'Iphone')
soup.findAll(string=re.compile('Samsung'))
soup.findAll(class_ = re.compile('pull'))
soup.findAll('p', class_ = re.compile('pull'), limit=3)
