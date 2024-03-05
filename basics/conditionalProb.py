day = input("give me a day: ")
age = int(input("give me an age: "))
ticket_price = 0
#if age < 18:
#    ticket_price = 8
#else:
#    ticket_price = 12
# the other way to write the price is as follows
ticket_price = 12 if age >= 18 else 8

if day == "wednesday":
    ticket_price -= 2

print(ticket_price)
