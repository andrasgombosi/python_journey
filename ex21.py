
def add (a,b):
    print "Adding %d and %d" % (a,b)
    return a+b

def substract (a,b):
    print "Substracting %d from %d" % (a,b)
    return a-b

def multiply (a,b):
    print "multipliing %d with %d" % (a,b)
    return a*b

def divide(a,b):
    print "dividing %d with %d" % (a,b)
    return a/b

age = add(30,6)
height = substract(200,12)
weight = multiply(8.6,10)
iq = divide(100,2)

print "Age: %d, height %d . weight %d iq: %d" % (age,height, weight,iq)

print "Puzzle"

what = add(age, substract(height, multiply(weight, divide(iq,2))))

print "that becomes:" , what , ", cool, he?"
