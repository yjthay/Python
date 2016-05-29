# coding: utf-8
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host="www.pythonlearn.com"
port=80
s.connect((host,port))
s.send('GET http://www.pythonlearn.com/code/intro-short.txt http/1.0 \n\n')
while True:
    data=s.recv(512)
    if len(data)<1:
        break
    print data
    
import urllib
s = urllib.urlopen('http://www.pythonlearn.com/code/intro-short.txt')