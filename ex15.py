# @SM files, gotta catch'em all

from sys import argv

script, filename = argv

txt = open(filename)

print "Your file is: %r" % filename
print "content is:\n"
print txt.read()

print "Why don't you type the filename again?"
filename = raw_input("> ")

txt_again = open(filename)

print "Your file is: %r" % filename
print "content is:\n"

print txt_again.read()