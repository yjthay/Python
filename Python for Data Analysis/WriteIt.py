text_file = open("writeit.txt","w")
text_file.write("Writing lesson one \n")
for i in range(100):
    i = str(i)
    text_file.write(i+" \n")
text_file.close

text_file = open("writeit.txt","r")
for line in text_file:
    print line
text_file.close

raw_input("\n Press enter to finish part 1")


text_file = open("writeit.txt","w")
lines = ["this is line 1 \n", "and line 2 \n", "lastly line 3"]
text_file.writelines(lines)

text_file = open("writeit.txt","r")
for line in text_file:
    print line
text_file.close
