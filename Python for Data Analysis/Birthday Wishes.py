# Birthday wishes
# Demostrates keyword arguments and default parameters values

# positional parameters
def birthday1(name, age):
    print "Happy Birthday, ",name,"!", " I hear that you are ",age, " today.\n"

birthday1("YJ", "25")

def birthday2(name = "Jackson", age = "10"):
    print "Happy Birthday, ",name,"!", " I hear that you are ",age, " today.\n"

birthday2()
birthday2(name = "Tester")
birthday2(age = "100")

