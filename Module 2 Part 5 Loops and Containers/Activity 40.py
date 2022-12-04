# listAct40.py
# author: Lucia
# Date: 1.12.2022

list_1 = [23, 66, 23, 12]
list_2 = [1,19, 4, 8]
list_3 = ["land of ", "the ", "the long white cloud"]

# challenge 1
'''
print("List 1 = ", list_1, "\n")
print("List 2 = ", list_2, "\n")

list_combined = list_1 + list_2
print("the combined list is ", list_combined, "\n")

choice = input("Please choose if you want to see average or sum of the combined list by typing ave or sum:")

sum_list = sum(list_combined)
if choice == "sum":
    print("The sum of the combined list is ", sum_list, "\n")
elif choice == "ave":
    average_list = float(sum_list) / len(list_combined)
    print("The average of the combined list is ", average_list, "\n")
'''

# Test
'''
print("My assertions are:"
          "\nchoice = sum, output = 156"
          "\nchoice = ave, output = 19.5")
'''

# challenge 2
'''
if len(list_2) > len(list_3):
    print("The list with more elements is ", list_2, "\n")
elif len(list_2) < len(list_3):
    print("The list with more elements is ", list_3, "\n")
else:
    print("The two lists have same amount of elements")
'''
'''
temp_list = [list_2, list_3]
list_to_print = []

for item in temp_list:
    if len(item) > len(list_to_print):
        list_to_print =  item

print("\nThe longest list contains {0} elements."
      .format(len(list_to_print)))
print("\nThe list is {0}"
      .format(list_to_print))
'''

# Test
'''
print("My assertion is:"
          "\nThe longest list contains 4 element."
          "\nThe list is [1, 19, 4, 8]")
'''
# challenge 3
'''
temp_list = []
list_to_print = []
for item in list_1:
    if item in temp_list:
        list_to_print.append(item)
    else:
        temp_list.append(item)
print(list_to_print)
'''

# Test
'''
assertion case 1
[23]
'''

# challenge 4
'''
list_2.sort()
print(list_2[0])
'''
# Test
'''
assertion
output = 1
'''

# challenge 5
'''
temp_list = []
list_to_print = []
for item in list_1:
    if item % 2 == 0:
        temp_list.append(item)
    elif item % 2 != 0:
        list_to_print.append(item)
print(list_to_print)
'''
'''
for counter in range(1, len(list_1), 2):
    print(list_1[counter])
'''
# Test
'''
assertion
output = 66, 12
'''
# challenge 6
'''
print(list_1[2], " ", list_1[3])
print(list_2[2], " ", list_2[3])
'''

# Test
'''
assertion
output = 23 12
output = 4 8
'''
# challenge 7
'''
import random

print(random.choice(list_2))
print(random.choice(list_2))
'''
# Test
'''
asserions are any two elements in list_2
'''

# challenge 8
'''
import random

item_1 = random.choice(list_2)
item_2 = random.choice(list_2)

while item_1 == item_2:
    item_2 = random.choice(list_2)
    
print(item_1, item_2)
'''

# Test
'''
asserions are any two elements in list_2
'''

# challenge 9
'''
joined_list = " ".join(sorted(list_3, key=len))
print(joined_list)
'''
