# @SM Reading and writing files, good stuff

from sys import argv

script, filename = argv

print "This script will kill %s", filename
print "You can still avoid destruction, hit CTRL+C"
print "Otherwise, hit ENTER and we'll continue the KILLING."

# this is just press enter to continue
raw_input("?")

print "opening ", filename
target = open(filename, 'w')

print "Hail, hail, hail and kill!"
target.truncate()

print "I'm sorry pal, but you asked for it"

print "At least input 3 lines and we'll revive the file for the sake of fuck"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "Better than nothing!"

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# better
target.write(line1+"\n"+line2+"\n"+line3+"\n")

target.close

print "all done, Amen."