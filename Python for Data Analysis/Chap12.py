import socket

mysock = socket.socket()#socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("www.py4inf.com",80))
mysock.send("GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n")# HTTP/1.0\n\n


while True:
    data = mysock.recv(512)
    if (len(data)<1) :
        break
    #print data

mysock.close()

import socket
import time

mysock = socket.socket()#socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("www.py4inf.com",80))
mysock.send("GET http://py4inf.com/cover.jpg HTTP/1.0 \n\n")

count = 0
picture = ""
while True:
    data = mysock.recv(5120)
    if (len(data) <1): break
    time.sleep(0.25)
    count = count +len(data)
    #print len(data),count
    picture = picture + data

mysock.close

#Look for the end of the header (2CRLF)
pos = picture.find("\r\n\r\n")
#print "Header length",pos
#print picture[:pos]

#Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg","w")
fhand.write(picture)
fhand.close()


import urllib

counts = dict()
fhand = urllib.urlopen("http://www.py4inf.com/code/romeo.txt")
for line in fhand:
    words =  line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print counts
    
