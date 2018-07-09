#@SM format strings...

my_name = 'Banana S. Joe'
my_age = 35 # not true
my_height = 1.74 # cm
my_weight = 70 # kg
my_eyes = 'Hazelnut'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %f meters tall." % my_height
print "He's %d Kgs heavy." % my_weight
print "Actually, that's not slim..."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# tricky line
print "If I add %d, %f, and %d I get %r." % (my_age, my_height, my_weight, my_age + my_height + my_weight)