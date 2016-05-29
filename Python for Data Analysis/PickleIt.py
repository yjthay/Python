import cPickle, shelve

print "Pickling lists."
#dictionary = {"variety" : ["Sweet", "Hot", "Dill"]}
#dictionary = {"shape" : ["Whole", "Spear","Chip"]}
#dictionary = {"brand" : ["Claussen","Hienz","Vlassic"]}
#pickle_file = open("pickles.dat","w")
#picklelist = ("variety","shape","brand")
#for key in dictionary:
#    cPickle.dump(key, pickle_file)
#    print key
#cPickle.dump(variety, pickle_file)

pickle_file = open("pickles.dat","w")
variety = ["Sweet", "Hot", "Dill"]
shape = ["Whole", "Spear","Chip"]
brand = ["Claussen","Hienz","Vlassic"]

cPickle.dump(variety, pickle_file)
cPickle.dump(shape, pickle_file)
cPickle.dump(brand, pickle_file)
pickle_file.close

print"\n Unpickling"
pickle_file = open("pickles.dat","r")
variety = cPickle.load(pickle_file)
shape = cPickle.load(pickle_file)
brand = cPickle.load(pickle_file)

print variety
print shape
print brand

pickle_file.close
