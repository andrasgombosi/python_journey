from sys import argv

script , filename = argv

print "We are going to erase %r" % filename

print "if you do not want that, hit CTRL-C (^C)."
print "if yo want that, hit RETURN (or ENTER...)"

raw_input("?")

print "opening the file..."

target = open(filename,'w')

print "Truncatig the file"
target.truncate()

print "Now I am going to ask you three lines"

line1 = raw_input("1:")
line2 = raw_input("2:")
line3 = raw_input("3:")

print "Write them to the file"

newline = '\n'

target.write(line1 + newline + line2 + newline + line3 + newline)

target.flush
target.close
