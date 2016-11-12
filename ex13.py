from sys import argv

#takes arguments from the command line runtime. Unpacks argv into variables
# Script is the zero argument, which contains the name of hte file
script, first, second, third,multi1 = argv


print "Argv: %r" % argv

print "this script is called:", script
print "first vaariable is :",first
print "second variable is :" , second
print "third variable is :" , third

multi2 = raw_input("second multiplier")

print int(multi2) * int(multi1)
