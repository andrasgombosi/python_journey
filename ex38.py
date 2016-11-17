ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, tehre are not 10 things in that list/"


stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Dog", "Crap", "Whatever"]

while len(stuff) <> 10:
    next_one = more_stuff.pop()
    print "adding this one to stuff" ,next_one
    stuff.append(next_one)
    print "Now there are %d items in stuff" % len(stuff)


print "There we go" , stuff

print "LEt's do things with stuff"


print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])


for i in range(0,len(stuff)):
    print stuff[i]
