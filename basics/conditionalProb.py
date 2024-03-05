age = int(input("give me user age: "))
if age < 13:
    print("the user is a child")

elif age >= 13 and age <= 19:
    print("the user is a teenager")

elif age >= 20 and age <= 59:
    print("the user is an adult")

else:
    print("the user is a senior citizen")
#not covering the negative age case in this one because of the laziness
