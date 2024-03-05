#day = input("give me a day: ")
#age = int(input("give me an age: "))
#ticket_price = 0
##if age < 18:
##    ticket_price = 8
##else:
##    ticket_price = 12
## the other way to write the price is as follows
#ticket_price = 12 if age >= 18 else 8
#
#if day == "wednesday":
#    ticket_price -= 2
#
#print(ticket_price)

# weather problem

#weather = input("give me the weather condition:")
#
#if weather == "sunny":
#    print("go for a walk.")
#elif weather == "rainy":
#    print("read a book.")
#elif weather == "snowy":
#    print("build a snowman.")
#else:
#    print("give a valid input ")

year = int(input("give me a valid year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
    print(year, " is a leap year")
else:
    print(year, "is not a leap year")
