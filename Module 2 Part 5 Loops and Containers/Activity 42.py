# ChallengesTuples.py
#
# @ author: A. N. Other
# date: September 2016
print("Here are challenges 1 and 2...\n")
#tuple with different datatypes (Challenge 1 and Challenge 2)
julia = ("Julia", "Roberts", 1967, "Actress", "Atlanta, Georgia")
print(julia, "\n")
"""
Here are challenges 1 and 2...

('Julia', 'Roberts', 1967, 'Actress', 'Atlanta, Georgia') 

"""
print("Here is challenge 3...\n")
#tuple with five numbers. Print the third (Challenge 3)
lotto_balls = (1,45,23,78,34,24)
print("The third lotto ball was :", lotto_balls[2], "\n")
"""
Here is challenge 3...

The third lotto ball was : 23
"""

print("Here is challenge 4...\n")
# tuple with three strings. (Challenge 4)
animals = ("cat", "dog", "horse")
animal_1 = animals[0]
animal_2 = animals[1]
animal_3 = animals[2]
print(animal_1, " ", animal_2, " ", animal_3, "\n")
"""
Here is challenge 4...

cat   dog   horse
"""
print("Here is challenge 5...\n")
#tuple with six elements. Challenge 5
lotto_balls = (1,45,23,78,34,24)
print("The fourth lotto ball was :", lotto_balls[3], "\n")
print("The fourth from last lotto ball was :", lotto_balls[-4], "\n")
"""
Here is challenge 5...

The fourth lotto ball was : 78 

The fourth from last lotto ball was : 23 
"""
print("Here is challenge 6...\n")
#tuple with duplicates. Challenge 6
items = (1,45,23,78,34,24, 45,24, 24)
repeated_items = []
for counter in range (0,len(items)):
    for number in range(counter+1, len(items)):
        if items[counter] == items[number]:
            repeated_items.append(items[number])
individual_repeats = set(repeated_items)
print(individual_repeats)
"""
Here is challenge 6...

{24, 45}
"""
'''
# test case assertions
Challenges 1 and 2 output = ('Julia', 'Roberts', 1967, 'Actress', 'Atlanta, Georgia')
Challenge 3 output = The third lotto ball was : 23
Challenge 4 output = cat   dog   horse
Challenge 5 output is:
The fourth lotto ball was : 78
The fourth from last lotto ball was : 23
Challenge 6 output = {24, 45}
'''
#tuple with duplicates.
items = (1,45,23,78,34,24, 45,24, 24)
found = 0
number = int(input("Enter the value you wish to search for\n"))
for counter in range (0,len(items)):
    if items[counter] == number:
        found += 1
if found == 0:
    print("The number was not in the tuple")
elif found == 1:
    print("The number was in the tuple once")
else:    
    print("The number was in the tuple more than once")
    
'''
# assertion
input= 3, output = "The number was not in the tuple" 
input= 78, output = "The number was in the tuple" 
input= 24, output = "The number was in the tuple more than once"
'''
