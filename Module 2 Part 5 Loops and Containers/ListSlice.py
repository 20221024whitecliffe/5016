# ListsSlice.py
#
# @ author: A. N. Other
# date: September 2016
# empty list
 
my_list = ['k','e','t','e','m','a','r','a','e']
# elements 3rd to 5th
print(my_list[2:5])
 
# elements beginning to 4th
print(my_list[:4])
 
# elements 6th to end
print(my_list[5:])
 
# elements beginning to end
print(my_list[:]) # : cant omit, will comes back invalid syntax error

"""Output = 
['t', 'e', 'm']
['k', 'e', 't', 'e']
['a', 'r', 'a', 'e']
['k', 'e', 't', 'e', 'm', 'a', 'r', 'a', 'e']
"""