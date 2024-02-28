coffee_varities = ['black', 'cold', 'filter', 'espresso']
print(coffee_varities)
print(coffee_varities[1:3])
print(coffee_varities[:2])
print(coffee_varities[2:])

# lists are mutable
# it doesn't create a new list when modifying an index, it changes that one only
for coffee in coffee_varities:
    print(coffee)

for coffee in coffee_varities:
    print(coffee, end=" ")
