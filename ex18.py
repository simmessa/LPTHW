# @SM functions!

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_2(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "Nuuuuthing sir"


print_two("anal", "beads")
print_two_2("anal", "phalluses")
print_one("Wurstel")
print_none() #WTF