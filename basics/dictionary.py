# dictionary in python
# dictionaries are also mutable
coffee_types = {"brew":"cold", "espresso":"hot", "filter":"love"}

for coffee in coffee_types:
    print(coffee)
#this would print all the keys

for coffee in coffee_types:
    print(coffee, coffee_types[coffee])
#this code would print the key value pairs
