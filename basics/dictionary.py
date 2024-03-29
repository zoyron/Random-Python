# dictionary in python
# dictionaries are also mutable
coffee_types = {"brew":"cold", "espresso":"hot", "filter":"love"}

for coffee in coffee_types:
    print(coffee)
#this would print all the keys

for coffee in coffee_types:
    print(coffee, coffee_types[coffee])
#this code would print the key value pairs


for x,y in coffee_types.items():
    print(x,y)
#this also prints the same thing for dictionary as the above example does


squared = {x:x**2 for x in range(11)}
print(squared)
