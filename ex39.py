#ex39
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
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('_' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('_' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print("{} is abbreviated {}".format(state,abbrev))
    print("and has city {}".format(cities[abbrev]))
   
# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print("{} has the city {}".format(abbrev, city))
 
 # now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print("{} state is abbreviated {}".format(state,abbrev))
    print("and has city {}".format(cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: {}".format(city))