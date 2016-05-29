import urllib 
import BeautifulSoup as bs
from BeautifulSoup import *
import re

url ='http://python-data.dr-chuck.net/known_by_Cian.html'

def tags(url,tagfilter):
    html = urllib.urlopen(url).read()
    soup = bs.BeautifulSoup(html)
    tags = soup(tagfilter)
    return tags


position=18
reps=7
i=0
while i<reps:
    url=tags(url,"a")[position-1].get('href')
    i+=1
    print url
    

