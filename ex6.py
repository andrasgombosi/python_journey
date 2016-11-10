#variable string with a decimal variable supplied in in
x = "There are %d type of people" % 10
#string var
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary,do_not)

print x
print y

# quotes around both ways
print " I said : %r" % x
print "I also said : '%s' " % y
#boolean operator
hil = False

joke = "Funny %r"
# variable itself containst placeholder for some string
print joke % hil

#concat
print binary + do_not
