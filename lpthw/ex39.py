# create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

print cities.items()
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print cities.items()

# print out some cities
print '-' * 10
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']

# print some states
print '-' * 10
print "Michigan abbreviation is: ", states['Michigan']
print "Florida abbreviation is: ", states['Florida']

# do it by using the state then cities dict
# first we get the states and then with the value we get cities...
print '-' * 10
print "Michigan has : ", cities[states['Michigan']]
print "Florida has : ", cities[states['Florida']]    

# 1 print every state abbreviation
# just getting State name and its abbreviation
print '-' * 10
# looping in key-value [state-abbrev] [Oregon-OR]
for state, abbrev in states.items():
    print "%s is abbreviated as %s" % (state, abbrev)

# 2 same as above
#print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do the both 1 && 2 at same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry!"
else:
    print "Its there!"    

# get a city with dafault value
city = cities.get('MIX', 'Does Not Exist.')
print "The city for the state mentioned : %s " % city            
