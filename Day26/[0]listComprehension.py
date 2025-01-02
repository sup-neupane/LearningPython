#List Comprehension is unique to python and is used to create new list from old Syntax:
# new_list = [new_item for item in list]

#It dosent strictly apply for list we may also do for strings as:
name = "Suparna"
new_list = [letter for letter in name]
print(new_list)

#We can do it for list string range and tuple
new_nums = [ number * 2 for number in range(1,5)]
print(new_nums)


#We can also do it applying some conditions as:
# new_list = [ new_item for item in list if test ]
even_nums_double = [number * 2 for number in range(1, 5) if number % 2 == 0]
print(even_nums_double)



