import urllib
url = 'http://python-data.dr-chuck.net/comments_42.xml'

import lxml.etree as etree

page = urllib.urlopen(url)
data = page.read()
tree = etree.fromstring(data)

print etree.tostring(tree, pretty_print = True)

mysum=0
count=0
for child in tree:
    for subchild in child:
        for i in subchild:
            if i.tag=='count':
                mysum+=int( i.text)
                count+=1