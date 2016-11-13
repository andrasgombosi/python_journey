def print_two(*args):
        arg1,arg2 = args
        print "arg1 is %s and arg2 is %s" % (arg1,arg2)

def print_two_again(arg1,arg2):
        print "arg1 is %s and arg2 is %s" % (arg1,arg2)

def print_one(arg1)        :
    print "arg1 is %s" % arg1

def print_none():
        print "No args here"


print_two("this","that")
print_two_again("this2", "that2")
print_one("sole")
print_none()
