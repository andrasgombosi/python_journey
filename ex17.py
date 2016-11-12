from sys import argv

from os.path import exists

script , from_file, to_file = argv

print "copy from %s to %s" % (from_file, to_file)

#opens and reads file
indata = open(from_file).read()
# prints length
print "The input file is %d byte long" % len(indata)
print "Does the output exitst? %r" % exists(to_file)

print "Here we go, hit ENTER to proceed, CTRL+C to abort"
raw_input()

target_file = open(to_file, 'w')
target_file.write(indata)
target_file.flush
target_file.close
