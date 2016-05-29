import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_269381.json '

#address = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None
if 'status' not in js:
    print '==== Failure To Retrieve ===='
    #print data

mysum=0
for i in js['comments']:
    mysum+=i['count']
print mysum