# @SM Copying files, intriguing.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying %s to %s..." % (from_file, to_file)

indata = open(from_file).read()

print "Lenght of input file is %d" % len(indata)
print "output %r, does it exist?" % exists(to_file)
print "ready, let's go on with RETURN"
raw_input("#")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Done."

out_file.close()