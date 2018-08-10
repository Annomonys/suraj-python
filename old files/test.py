# This program prints Hello, world!
from bs4 import BeautifulSoup
import requests
import re

print('Hello, world!')

url= 'https://www.snapdeal.com'
page3= requests.get(url)
soup3= BeautifulSoup(page3.text)
desc= soup3.find(attrs={'name':'Description'})
keys= soup3.find(attrs={'name':'Keywords'})
# img_tags= soup3.find_all('img')
# images= [img['src'] for img in img_tags]
if (desc == None) or (keys == None):
    desc= soup3.find(attrs={'name':'description'})
    keys= soup3.find(attrs={'name':'keywords'})
    
try:
    print(desc['content'])
    print('KeyWords')
    print(keys['content'])
    # for image in images;
    #     filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', image)
    #     with open(filename.group(1), 'wb') as f:
    #         if 'http' not in image:
    #             url= '{}{}'.format(url, image)
    #         response = requests.get(image)
    #         f.write(response.content)
except Exception as e:
    print('%s (%s)' % (e.message, type(e)))