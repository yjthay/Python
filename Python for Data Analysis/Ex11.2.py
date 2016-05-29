fname = raw_input("Please enter the file name to open")
try:
    fhand = open(fname)
except:
    print "File does not exist"
    fname = "mbox-short.txt"
    print "Instead will be opening ",fname
    fhand = open(fname)
import re
revisionnumber = 0
count = 0
for line in fhand:
    words=re.findall("New Revision: ([0-9.]+)",line)
    
    if words !=[]:
        #print words[0]
        revisionnumber += int(words[0])
        count +=1

average = revisionnumber/float(count)
print average
    
    
