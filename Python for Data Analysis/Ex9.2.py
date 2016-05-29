fname = raw_input("Please enter the file name ")
try:
    fhand = open(fname)
except:
    fname = "mbox-short.txt"
    print "Opening ", fname, " instead"
    #exit()
    fhand = open(fname)

import string
daysofweek = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")
# daysofweek = ("mon", "tues", "wed", "thurs", "fri", "sat", "sun")
DOW = dict()

for line in fhand:
    #line = line.translate(None, string.punctuation)
    #line = line.lower()
    line = line.split()
    for word in line:
        if word not in daysofweek:
            None
        else:
            if word not in DOW:
                DOW[word] = 1
            else:
                DOW[word] +=1

print DOW

        
