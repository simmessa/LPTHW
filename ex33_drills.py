#while loops, love em, but don't abuse em



def suga_babe(suga, numbers, increment):

    i = 0
    numbers = []
    while i < suga:
        print "Suga babe top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "Suga babe bottom i is %d" % i

    return numbers

print "The numbers: "

numbah = []

suga_babe(234, numbah, 18)

for num in numbah:
    print num