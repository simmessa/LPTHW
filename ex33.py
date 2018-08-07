#while loops, love em, but don't abuse em

i = 0
numbers = []

while i < 6:
    print "Suga babe top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "Suga babe bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num