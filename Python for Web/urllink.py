import urllib 
import BeautifulSoup as bs
from BeautifulSoup import *

url = raw_input('Please enter URL - ')
#url ='http://www.livescore.com/'

html = urllib.urlopen(url).read()
soup = bs.BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    print tag.get('href',None)
    pause(1)