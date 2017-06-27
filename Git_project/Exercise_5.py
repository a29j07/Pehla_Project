my_name = "Abhishek Jindal"
my_age = 20 # not a lie
my_height = 176 # cm
my_weight = 78 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

print "Hello, this is %s." % my_name
print "I'm %d cm tall." % my_height
print "I'm %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "I got %s eyes and %s hair." % (my_eyes, my_hair)
print "My teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
