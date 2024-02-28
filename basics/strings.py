# strings module

name = 'Johhny arora'
print(name.upper())
print(name.replace("Johhny", "John"))

name = "Karan, Arjun, Hitesh, Sagar"

# the split method splits and returns the output list wherever it encounters a space by default, for eg, the output of the following would include ',' in each element of the list since it's before the space so it would be included in the element string
print(name.split())

#to avoid the above stuff from happening we give an input to the split method that this is what we want to use for splitting the output list for eg, writing split(", ") would use the comma and space combined as the splittor for the list that would be returned

print(name.split(", "))

# the find method returns the index of the first character of the target substring in the string
# for eg, find("kulcha") in "butter kulcha" would return 7 since from 7th index the substring "kulcha" starts

x = "butter kulcha"
print(x.find("kulcha"))
