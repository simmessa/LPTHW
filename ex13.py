# @SM parameters, thx god.

# 1st time we use modules! 
from sys import argv

# this is how we define cmd line arguments! We ask just what we need...
script, first, second, third = argv

# this syntax in python is called unpacking, very powerful stuff
# argv is taken and assigned (unpacked) to the specified vars in that order

print "The script is called: ", script
print "1st param is called: ", first
print "2nd param is called: ", second
print "3rd param is called: ", third

