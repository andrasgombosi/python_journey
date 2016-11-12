#import command line argument handling
from sys import argv

#unpack argument array
script,filename = argv

#open file based or argument
txt = open(filename)

# show what the argument was.
print "Here is your file %r" % filename
#apply read on the file object. Read puts it onto the stdo
print txt.read()

print "Type a filename again"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

print txt_again.encoding
