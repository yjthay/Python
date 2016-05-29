fname = raw_input("Please enter the file name")
fname = fname + ".txt"
try:
    fhand = open(fname)
except:
    print "File not found"
    fname = "mbox-short.txt"
    print "Instead opening ", fname
    fhand = open(fname)

import re

counts = dict()

for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        m = re.search('\S+@\S+',word)
        if m is not None:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word]+=1

print counts
        
        
