import requests
from requests_html import HTMLSession
s = HTMLSession()

query = 'london'
url = f'https://www.google.com/search?q=weather+{query}'


r = s.get(url, headers={'User- Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' })

temp = r.html.find('span#wob_tm',first=True).text



      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
