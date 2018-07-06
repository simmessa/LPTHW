# @SM asking stuff...nicely!

print "Your age, please?"
age = raw_input()

# raw_input gets a string.
# input tries conversion, but it's insecure!

print "Your height, please?"
height = raw_input()

print "Your weight, may I ask...?"
weight = raw_input()

print "So, quite obviously you're %r old, %r high and %r heavy!" % (age, height, weight)