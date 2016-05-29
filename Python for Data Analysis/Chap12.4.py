import urllib
fhand = urllib.urlopen("http://www.py4inf.com/code/romeo-full.txt")
for line in fhand:
    words = line.split()
    print line.strip()


import urllib
import re
url = raw_input("Enter - ")
html = urllib.urlopen(url).read()
links = re.findall("href='(http://.*?)'",html)
for link in links:
    print link

