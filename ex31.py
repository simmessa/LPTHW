# @SM decisions

print "Adventure stuff, choose your destiny, door1 or door2 ?"

door = raw_input("> ")

if door == "1":
    print """There's Giana (one of the sisters) eating a bucket o' chicken fried wings, What's next?
    1. kick Giana
    2. get sum wings"""

    
    giana = raw_input("> ")

    if giana == "1":
        print "Giana kills you. nice."
    elif giana == "2":
        print "Giana kills you, but after getting back her wings. Top"
    else:
        print "Whatever you meant with %s is ok, Giana went away."
    
elif door == "2":
    print """You are in the shadow of my ass. anything more?
        1. kick ass
        2. blow ass
        3. asshole"""

    asswer = raw_input("> ")

    if asswer == "1" or asswer == "2":
        print "You die, once again, great job."
    else:
        print "You die faster, you're somewhat improving."
else:
    print "You still die, not choosing a door wasn't smart."