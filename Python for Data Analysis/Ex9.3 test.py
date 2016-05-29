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
import string

counts = dict()

for line in fhand:
    line = line.lower()
    #words = line.split()
    #for word in line:
    m = re.search('from: \S+@\S+',line)
    if m is not None:
        words = line.split()
        for word in words:
            if word <> "from:":
                word = word.translate(None,"'")
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word]+=1

print counts
        
        
