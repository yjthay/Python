fname = raw_input('Enter the file name: ')
if fname is "":
    fname = "romeo.txt"
    print "Using ",fname," instead" 

try:
    fhand = open(fname)
except:
    print "File cannot be opened:", fname
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

print counts

counts = {"chuck":1,"annie":42, "jan":100}
for key in counts:
    print key, counts[key]

lst = counts.keys()
lst.sort()
print lst

for key in lst:
    print key, counts[key]

import string
string.punctuation
#from string import maketrans # Required to call maketrans function.

vowels = "aeiou"
numbers = "12345"
transtable = string.maketrans(vowels,numbers)

counts1 = dict()

fhand = open(fname)
for line in fhand:
    line = line.translate(transtable,"f")
    #line = line.translate(None,string.punctuation)
    print line
    line= line.lower()
    print line
    words = line.split()
    for word in words:
        if word not in counts1:
            counts1[word] = 1
        else:
            counts1[word] +=1

print "counts1 ",counts1
