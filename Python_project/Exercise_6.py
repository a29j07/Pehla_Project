x = "There are %s types of people." % "many"
iOS = "iOS"
do_not = "don't"
y = "Those who know %s and those who %s." % (iOS, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e