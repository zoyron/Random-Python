list1 = [1,2,3]
list2 = list1
print("here we have list2 = list1, so \"list1 is list2\" would evaluate to True")
print(list1 is list2)
print(list1)
print(list2)
# in the above example a list with 1,2 and 3 in values is created in the memory then it is reference to the variable list1, after that we referenced list1 to list2, hence giving it the same memory reference as we have in list1, but instead of that had we done list2 = [1,2,3] then although the values in the lists would have been same, but the memory reference would be different. Those 2 lists would have same values but those would be entirely different lists since their memory location would be totally different

#if we change the value in the list(example1), both the variables would be effected since both of them are referencing the same location in the memory
list1[2] = 222
print(list1)
print(list2)

list1 = [1,2,3]
list2 = [1,2,3]
# in this particular example both the lists have same values but we need to remember that these are two different lists at two different locations in the memory, unlike the 1st example where we made just 1 list and pointed 2 different variables  to it
print("here \"list1 == list2\" would equate to True but \"list1 is list2\" would equate to false because '==' checks for the same values whereas 'is' checks for the same memory reference ")
# and these lists might be same in values, but since these are 2 different lists these would occupy different memory locations
print(list1 == list2)
print(list1 is list2)
# but in this example if we change the value of one index in any list the other list won't be effected since they are referencing different locations in the memory
list1[1] = 2222
print(list1)
print(list2)
