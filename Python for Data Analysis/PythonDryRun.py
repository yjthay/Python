letters = "a/b/c"
delimiter = "/"
jlist = letters.split("/")
#print jlist
#print len(jlist)
del jlist[len(jlist)-1]

#print jlist

jlist.append([4])
#print jlist


orig = jlist[:]
jlist.sort()
#print orig
#print jlist
#mbox-short.txt

emailfile = raw_input("Whats the file name? \n")
fhand = open(emailfile)

count =0
for line in fhand:
    words = line.split()
    #print "Debug: " + str(words)
    #print len(words)
    if len(words) != 0 and words[0] == "From":
        print words[1]
        count = count +1
    continue
    
    #if words[0] != "From" : continue
    #print words[1]
print "There were " + str(count) + " lines in the files with 'From' as the first word"

fhand.close

romeo = open("romeo.txt")

romeolines = []
for line in romeo:
    #print line
    romeolines = romeolines + line.split()
    romeolines.sort()
    print romeolines

userinput = ""
list_of_numbers = []
while userinput != "DONE":
    userinput = raw_input("What is the number in your mind? :")
    if userinput !="DONE":
        userinput = int(userinput)
        list_of_numbers.append(userinput)

print list_of_numbers
print max(list_of_numbers)
print min(list_of_numbers)
 
    
raw_input("Press enter to exit")