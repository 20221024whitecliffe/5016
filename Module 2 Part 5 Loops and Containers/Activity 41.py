# activity41.py
# author: lucia
# date: 1.12.2022

# challenge 1
'''
list_1 = [ 34, 123, 5, 77, 59, 2, 4 ]

print(list_1[2: 5])
'''
'''
my assertion
[5, 77, 59]
'''

# challenge 2
'''
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
length = len(list_1)
half = int(length/2)

print(list_1[0:half])
'''
'''
assertion
output = [1, 2, 3, 4]
'''

# challenge 3
'''
list_1= []
length = len(list_1)

if length % 4 == 0:
    quarter = int(length / 4)
    print(list_1[quarter * 3:length])
'''

# challenge 2-1
'''
item = int
counter = 0
list_1 = [2, 4, 6, 8, 9, 11, 13, 15]

while counter < 3:
    item = int(input("Enter an integer to the list"))
    list_1.append(item)
    counter += 1

print(list_1)
'''
'''
list_1 = []
for counter in range(0,3):
    item = int(input("\nInput an integer\n"))
    list_1.append(item)
print(list_1)
'''
'''
# assertion 
intput 3 integers, 13, 15, 14, output = [13, 15, 14]
'''

# challenge 2-2
'''
proverb_part_list = [ "As a man disappears ", " the ", "land remains." ]
add = input("Please enter an element to the list:\n")
proverb_part_list.append(add)

proverb = " ".join(proverb_part_list)

print(proverb)
'''
'''
proverb_part_list = [ "As a man disappears", "the", "land remains." ]
print("A well known Maori proverb states:...\n")
print("As a man disappears from sight the land remains\n")
print("The stored version of this proverb states:...\n")
for item in proverb_part_list:
    print(item, end=" ")
item = input("\n\nInput the first missing section of the proverb\n")
proverb_part_list.insert(1, item)
joined_list = " ".join(proverb_part_list)
print(joined_list)
'''
'''
# assertion 
intput = "from sight", output = As a man disappears from sight the land remains.
'''

# challenge 3
'''
import random

list_1 = []

for item in range(5):
    list_1.append(random.randint(1,10))

print(list_1)
'''

'''
# assertion - list elements are randomised
output = [1, 3, 7, 2, 6]
output = [5, 5, 8, 4, 7]
'''

# challenge 4
'''
shopping_cart = ["iPhone 7", "MacBook Air", "Surface Tablet"]

item = int(input("Choose the item index you want to remove from the cart: "))
shopping_cart.pop(item)

print(shopping_cart)
'''
'''
# assertion
intput = 0, output = ['MacBook Air', 'Surface Tablet'] 
intput = 2, output = ['iphone 7', 'MacBook Air'] 
'''

# challenge 5
'''
word = input("\nInput a word\n")
list_to_reverse = list(word)
list_to_reverse.reverse()
print(" ".join(list_to_reverse))
'''
'''
# assertion
input = hello, output = olleh
input = hello world, output = dlrow olleh
'''

# challenge 6
'''
list_1 = [ 34, 123, 5, 77, 59, 34, 2, 4 , 123]
print("Initial stored list is...\n")
print(list_1, "\n\n")
print("Removing the duplicates, the stored list is now...\n")
list_1 = set(list_1)
print(list_1, "\n\n")
'''
'''
# assertion
[ 34, 123, 5, 77, 59, 34, 2, 4 , 123], output = [2, 34, 4, 5, 123, 77, 59] 
'''

# challenge 7
'''
list_1=[]

if len(list_1) >= 1:
    print("The list is not emply\n")
else:
    print("The list is emply\n")
'''
'''
list_1 = [ 34, 123, 5, 77, 59, 34, 2, 4 , 123]
length = len(list_1)
if length < 1:
    print("The list is empty")
else:
    print("The list has", len(list_1), "items it in.\n")
'''
'''
# assertion
input = [ 34, 123, 5, 77, 59, 34, 2, 4 , 123], output = The list has 9 items it in.
'''
    
# challenge 8
'''
list_1 = ["I","Love", "You"]

n = int(input("Write a number you want the words from"))

if n <= len(list_1):
    print(list_1[0:n])
'''
'''
length = int(input("\nInput a word length\n"))
list_1 = ["Cat", "Horse", "Tiger", "Baboon", "Squirrell", "Elephant"]
for counter in range (len(list_1)):
    if len(list_1[counter]) > length:
        print(list_1[counter])
'''
'''
# assertion
input = 5, output = Baboon elephant Squirrell.
'''

# challenge 9
'''
list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
list2 = [3, 6, 9, 12, 15, 18]

result = False
for x in list1:
    for y in list2:
        if x == y:
            result = True
print(result)
'''
'''
# assertion
list_1 = [1,56,123,87], list_2 = [34, 84, 76, 93], output = False
list_1 = [1,56,123,87], list_2 = [34, 84, 56, 93], output = True
'''

# challenge 10
'''
import random
list_1 = [1,56,123,87]
print(list_1)
random.shuffle(list_1)   
print(list_1)
'''
'''
# assertion
list_1 = [1,56,123,87], output = [123, 87, 1, 56]
'''

# challenge 11
'''
list_1 = [1, "a", True, 5.2]
list_2 = ["stupid", "mix"]

list_1.append(list_2)
print(list_1)
list_1.extend(list_2)
print(list_1)
'''
'''
# test case assertion 1
[1, 56, 123, 87, [34, 75, 13, 89]]
# test case assertion 2
[1, 56, 123, 87, [34, 75, 13, 89], 34, 75, 13, 89]
'''

# challenge 12
'''
import random
from datetime import datetime, timedelta

duration = 6

period = timedelta(seconds=1)

next_time = datetime.now()+ period

counter = 0

list_1 = []

while counter < duration:
    if next_time <= datetime.now():
        list_1.append(random.randrange(1, 10, 1))
        next_time += period
        counter += 1

print(list_1)
'''
'''
# assertion
output = [71, 81, 68, 46, 58, 92]
'''

# challenge 13
'''
from random import randint

lotto_balls = list(range(1, 50))
selected_balls = []
counter = 0
balls_left = 49

for counter in range(1, 7):
    ball_index = randint(1, balls_left) -1
    ball = lotto_balls[ball_index]
    if (ball) not in selected_balls:
        selected_balls.append(ball)
        lotto_balls.pop(ball_index)
    balls_left -= 1
    counter += 1

print("Selected balls are ", selected_balls, "\n")
print("Remaining balls are ", lotto_balls, "\n")
'''
'''
# test case assertion:
since the outputs are randomised, I assert that they show:
A list of balls from 1 to 49 is created
6 balls are selected
The ball numbers are not repeated
The the balls are removed from the initial list
'''
