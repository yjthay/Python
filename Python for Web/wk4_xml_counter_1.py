import urllib
import xml.etree.ElementTree as ET

url='http://python-data.dr-chuck.net/comments_269377.xml'

page = urllib.urlopen(url)
data = page.read()
tree = ET.fromstring(data)
mysum=0
for i in tree.findall('.//count'):
    mysum+=int(i.text)