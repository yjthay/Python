
fpath = "C:/Users/thayyee/Desktop/regex_sum_269375.txt"
fhand = open(fpath)

import re
#mysum=0
#for line in fhand:
#    for num in re.findall('[0-9]+',line):
#        mysum+=int(num)
#print mysum
print sum([int(num) for num in re.findall('[0-9]+',fhand.read())])