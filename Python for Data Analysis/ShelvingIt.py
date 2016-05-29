import cPickle, shelve
print"\n Shelving lists"
pickles = shelve.open("pickles.dat","r")

pickles["variety"]
