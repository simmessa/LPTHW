# @SM some typing on Anne 2 Pro is always good to get hands in shape...

from sys import exit
import random

def gold_room():
    print "A room full of gold, how much will you rob?"

    next = raw_input("> ")

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        print "Numbers are easy, once you learn to type'em..."
    
    if how_much < 50:
        print "You're not a greedy man, therefore...You Win!"
    else:
        dead("Carrying all that gold kills you.")

def monster_room():

    print ("So, you're facing the baddest monster from your (dirty) nigthmares...")
    print ("How would you fight it?")
    print ("You remember something about killing monsters with farts, or maybe you should just beg for mercy...!")

    next = raw_input("> ")

    if "fart" in next:
        print "strange but true, the monster dies, congrats!"
        gold_room()
    if "beg" in next:
        print "you bet the monster for your life..."
        dead("it yawns, then devores you!")
    else:
        dead("you just die!")

def dead(why):
    print why, "Good job, sucker!"
    exit (0)

def start(where):
    if where % 2 == 0:
        gold_room()
    else:
        monster_room()

start( random.randint(0, 1) )