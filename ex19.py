# @SM functions, and vars, back with a Vengeance!

def mac_and_cheese(mac_count, boxes_of_cheese):
    print "You've got %r macs!" % mac_count
    print "You've also got %r boxes of cheese!" % boxes_of_cheese
    print "Enough for a Farty!\n" #Do I have to explain this, don't make me.

print "Call directly:"
mac_and_cheese(10,20)

print "Call with vars:"
macs = 10
boxes_of_cheese = 20
mac_and_cheese(macs, boxes_of_cheese)

print "Funny maths:"
mac_and_cheese(10*2**34, 998*997)

print "Funny math combos:"
mac_and_cheese(macs**macs, boxes_of_cheese*macs-77)

# @SM keep in mind exp in python isn't ^ (bitwise and!) but **

# @SM python passes values to functions by value NOT by reference!