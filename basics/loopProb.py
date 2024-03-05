# given a list of numbers, count how many are positive
#numbers = [int(x) for x in input("enter numbers separated by a space: ").split()]
#positive_number_count = 0
#
#for num in numbers:
#    if num >= 0:
#        positive_number_count+=1
#print(positive_number_count)

# sum of even numbers
n = int(input("enter a number: "))
sum_even = 0
for i in range(1, n+1):
    if i%2  == 0:
        sum_even += i
print(sum_even)
