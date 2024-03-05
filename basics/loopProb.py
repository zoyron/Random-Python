# given a list of numbers, count how many are positive
numbers = [int(x) for x in input("enter numbers separated by a space: ").split()]
positive_number_count = 0

for num in numbers:
    if num >= 0:
        positive_number_count+=1
print(positive_number_count)
