# @SM A Zork game, me likes!

from sys import argv

script, user_name = argv

prompt = "> "

print "Hi sexy %s, I'm the script %s" % (user_name, script)
print "Time for askies!"

print "Do you like me %s babe?" % user_name
likes = raw_input(prompt)

print "Wassyournumbah?"
number = raw_input(prompt)

print "Mind sexting me your seXXX?"
sexting = raw_input(prompt)

print """

Ok babe %s, we're set, I've got your number:
%s
you said %s and when asked about sexting you said: %s!
""" % (user_name, number, likes, sexting)
