# @SM list and loops...

count = [1, 2, 3, 4, 5, 6, 7]
fruits = ['apples', 'bananas', 'vulvas', 'penises']
change = [1, 'death', 2, 'destruction', 3, 'plasma']

for number in count:
    print "count: %s" % number

for fruit in fruits:
    print "fruit: %s" % fruit

for i in change:
    print "change: %r" % i

# building lists
elements = []

for i in range(0, 6):
    print "Adding %d to elements list" % i
    elements.append(i)

for i in elements:
    print "grabbed some from elements, i got %d" % i