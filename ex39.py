# create a mapping of state to abbreviation

states ={
'Oregon': 'OR',
'Florida':'FL',
'California':'CA',
'New York': 'NY',
'Michigan':'MI'
}

# basic set of cities
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

# add more cities
cities['NY']= 'New York'
cities['OR']= 'Portland'

#print cities

print '-'*10
print "NY state has ", cities['NY']

# print some states

print '-'*10
print "Michigan's abbrevation is", states["Michigan"]

# traversing states and cities
print '-'*10
print "Michigan has ", cities[states["Michigan"]]

# all the state abbrevation
print '-'*10

for state,abbrev in states.items():
    print "State %s has the  abbreviation %s" % (state,abbrev)

# go down to city level
for state,abbrev in states.items():
    print "State %s which is abbreviated as %s " % (state,abbrev),
    print "has the city %s in it" %  cities[abbrev]

state = states.get('Texas')

if not state:
    print "No texas"

    #get city with default value
city = cities.get('TX','Does not exist')
print "The city for state 'TX' is %s" % city
