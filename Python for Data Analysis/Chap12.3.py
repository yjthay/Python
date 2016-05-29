import socket
import time

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("www.py4inf.com",80))
mysock.send("GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n")

count = 0
picture = ""
while True:
    data = mysock.recv(5120)
    if (len(data)<1):
        break
    time.sleep(0.02)
    count =count+len(data)
    print len(data),count
    picture = picture+data
    
mysock.close()

pos = picture.find("\r\n\r\n")
print "Header length",pos
print picture[:pos]

picture = picture[pos+4]
fhand = open("stuff.jpg","w")
fhand.write(picture);
fhand.close
