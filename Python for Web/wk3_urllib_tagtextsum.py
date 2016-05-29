import urllib 
import BeautifulSoup as bs
from BeautifulSoup import *
import re

#url = raw_input('Please enter URL - ')
url ='http://python-data.dr-chuck.net/comments_269380.html'

html = urllib.urlopen(url).read()
soup = bs.BeautifulSoup(html)
mysum=0
tags = soup('span')
for tag in tags:
    mysum+=int(tag.text)

print mysum