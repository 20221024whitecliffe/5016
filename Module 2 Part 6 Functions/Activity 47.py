# activity47.py
# author: lucia
# date: 3.12. 2022
"""
# challenge 1
# I don't understand why this is not working. 
def answer_evaluator(answer):
    ctr = 0
    if answer == True:
        ctr += 1
        print("Your answer is correct. You have {0} score.".format(ctr))
    else:
        print("Sorry it is wrong")

quiz_1 = input("What is the capital of New Zealand?")
if quiz_1.lower == "wellington":
    answer_evaluator(answer = True)
else:
    answer_evaluator(answer = False)
    
quiz_2 = input("What is the biggest city in New Zealand?")
if quiz_2.lower == "auckland":
    answer_evaluator(answer = True)
else:
    answer_evaluator(answer = False)


score = 0
print('\nTwo-item Quiz Example')
def get_score(question, answer, score):
    print('\n'+ question)
    user_response = input('Answer: ')
    if user_response == answer:
        score += 1
        print('Well done')
    else:
        print('Sorry, you got it wrong')
    return score    
score = get_score('What do you call the scope of a variable that can be accessed anywhere in the code?', 'global', 0)
score = get_score('What Python statement allows for throwing back of a value used in the function to the calling statement?', 'return', score)
print('\nYour score: {0}'.format(score))

'''
# assertion
inputs: global, hello
Two-item Quiz Example
What do you call the scope of a variable that can be accessed anywhere in the code?
Answer: global
Well done
What Python statement allows for throwing back of a value used in the function to the 
calling statement?
Answer: hello
Sorry, you got it wrong
Your score: 1
'''      

# challenge 2

print("\nSumming two numbers.")

def calc_sum(n1, n2):
    sum_num = n1 + n2
    return sum_num

n1 = int(input("\nEnter the first number:"))
n2 = int(input("\nEnter the second number:"))
print("The sum of number {0} and number {1} is {2}".format(n1, n2, calc_sum(n1, n2)))

'''
# assertion
input 4 and 3
output:
Summing Two Numbers
Enter the first number: 4
Enter the second number: 3
The sum of 4 and 3 is 7
'''

# challenge 3 (answer not good)

print('\nParking Cost Calculator')
print('\nThis program calculates the cost of parking based on the following formula:'
          '\n  $4 for the first 2 hours, then $3 for every hour thereafter.') 
def get_parking_cost(hours):
   cost = (hours - 2) * 3 + 4
   return cost
hours = int(input('\nEnter the number of parking hours (integer only): '))
print('\nThe cost of parking for {0} hours is {1}'.format(hours, 
get_parking_cost(hours)))    

'''
# assertion
input 4
output: 10
Parking Cost Calculator
This program calculates the cost of parking based on the following formula:
  $4 for the first 2 hours, then $3 for every hour thereafter.
Enter the number of parking hours (integer only): 4
The cost of parking for 4 hours is 10
# assertion 2
input 1
output: 4
Parking Cost Calculator
This program calculates the cost of parking based on the following formula:
  $4 for the first 2 hours, then $3 for every hour thereafter.
Enter the number of parking hours (integer only): 4
The cost of parking for 4 hours is 10
'''

# challenge 4

print('\nColour Lists\n')
list_a = ["brown", "grey", "amber"]
list_b = ["red", "green"]
list_c = ["purple"]
col_list = [list_a, list_b, list_c]
def get_colour(colour_list):
   ctr = len(colour_list)
   while ctr < 3:
      colour = input('Please enter another colour to complete the list {0}: '.format(colour_list))
      ctr += 1
      colour_list.append(colour)
   return colour_list
for clist in col_list:    
  get_colour(clist)
print('\nThe 3-colour lists are:')
for clist in col_list:    
  print(clist)

'''
# assertion
input: yellow
input: green, blue
output:
Colour Lists
Please enter another colour to complete the list ['red', 'green']: yellow
Please enter another colour to complete the list ['purple']: green
Please enter another colour to complete the list ['purple', 'green']: blue
The 3-colour lists are:
['brown', 'grey', 'amber']
['red', 'green', 'yellow']
['purple', 'green', 'blue']
'''
# challenge 5

from time import sleep

print("Welcome to Count Down Timer\n")

counter = 0

def count_down(second):
    for counter in range(second):
        print(second)
        second -= 1
        sleep(1)
        counter += 1
    print("Time Up!!!")

second = int(input("Please enter the seconds to count down...\n"))
print("Starting...\n")
count_down(second)

print("Process finished with exit code 0")


from time import sleep
print('\nWelcome to Count Down Timer\n')
def get_timer():
  seconds = int(input('Please enter the number of seconds to count down...\n'))
  return seconds
def get_countdown_exit_code(seconds):
  start_time = seconds
  print('Starting...')
  for ctr in range(seconds):
    current_time = start_time - ctr
    print(current_time)
    sleep(1)
  print('Time Up!!!!')
  return 0
     
print('\nProcess finished with exit code {0}'.format(get_countdown_exit_code(get_timer())))

'''
#assertions
Input: 5
Output:
Welcome to Count Down Timer
Please enter the number of seconds to count down...
5
Starting...
5
4
3
2
1
Time Up!!!!
Process finished with exit code 0
'''

# challenge 6
''' Wrong, misunderstood the requirement of the challenge
print("Find the max 3 of the stored numbers\n")

def max_3(stored_list):
    stored_list.set
    print("The max three numbers of the list is {0}, {1}, {2}".format(stored_list.index(-1), stored_list.index(-2), stored_list.index(-3)))
    
stored_list = [22, 56, 33, 2, 9, 11, 8]
max_3(stored_list)
'''
''' Wrong too
print('\nFinding max of three numbers\n')
numlist = []

def get_number_list(numlist):
   ctr = len(numlist)
   while ctr < 3:
      num = float(input('Please enter a number: '))
      if num.is_integer():
          num = int(num)
      numlist.append(num)
      ctr += 1
   return numlist

def get_max(numlist):
   max = numlist[0]
   ctr = 1
   while ctr < len(numlist):
      if numlist[ctr] > max:
         max = numlist[ctr]
         ctr += 1
      else:
         ctr += 1
      return max

numlist = get_number_list([])
print('\n{0} is the largest of the three numbers: {1}'.format(get_max(numlist), numlist))
'''
'''
#assumptions
Input, 56, 34, 78
Output:
Finding max of three numbers
Please enter a number:  56
Please enter a number: 34
Please enter a number: 78
78 is the largest of the three numbers: [56, 34, 78]
'''

# challenge 7
# Python code to demonstrate naive method
# to compute factorial

n = int(input("Please enter an non-negative integer"))
fact = 1

for i in range(1,n+1):
	fact = fact * i
	
print ("The factorial of {0} is : ".format(n),end="")
print (fact)


print('\nFinding the factorial of a number')

def get_factorial(num):
   ctr, fact = 1, 1
   while ctr <= num:
     fact *= ctr 
     ctr += 1
   return fact
num = 0
while not int(num) > 0:
  num = input('\nPlease enter a positive integer: ')
  
print('\nThe factorial of {0} is {1}'.format(num, get_factorial(int(num))))

'''
#assertions
Input: 5
Output:
Finding the factorial of a number
Please enter a positive integer: 5
The factorial of 5 is 120
'''
# challenge 8
""""""
def val_numbers(num1, num2, num3):
    if num1 in range(num2, num3):
        validity = True
    else:
        validity = False
    return validity
validity = False

num1 = int(input("please enter number 1: "))
num2 = int(input("please enter number 2: "))
num3 = int(input("please enter number 3: "))
val_numbers(num1, num2, num3)
print("The first number {0} is within the range of second number {1} and third number{2} is {3}".format(val_numbers(num1, num2, num3), validity))
"""
"""
Traceback (most recent call last):
  File "/workspaces/5016/Module 2 Part 6 Functions/Activity 47.py", line 300, in <module>
    print("The first number {0} is within the range of second number {1} and third number{2} is {3}".format(val_numbers(num1, num2, num3), validity))
NameError: name 'validity' is not defined
"""


print('\nFinding if first number is between the second and third numbers\n')
numlist = []
def get_number_list(numlist):
   ctr = len(numlist)
   while ctr < 3:
      num = float(input('Please enter a number: '))
      if num.is_integer():
          num = int(num)
      numlist.append(num)
      ctr += 1
   return numlist
def get_within_range_truth_value(numlist):
   if numlist[2] > numlist[1]:
       if (numlist[0] >= numlist[1] and
          numlist[0] <= numlist[2]):
            return True
       else:
            return False
   else:         
       if (numlist[0] >= numlist[2] and
          numlist[0] <= numlist[1]):
            return True
       else:
            return False
numlist = get_number_list([])
print('\nIt is {0} that {1} is within the range of {2} and {3}.'
         .format(str(get_within_range_truth_value(numlist)).lower(),
          numlist[0], numlist[1],numlist[2]))

'''
#assertions
Input: 45, 10, 67
Output:
Finding if first number is between the second and third numbers
Please enter a number: 45
Please enter a number: 10
Please enter a number: 67
It is true that 45 is within the range of 10 and 67.
#assertion 2
Input: 10, 34, 100
Output:
Finding if first number is between the second and third numbers
Please enter a number: 10
Please enter a number: 34
Please enter a number: 100
It is false that 10 is within the range of 34 and 100.
'''

# challenge 9
# Wrong
'''
list_1 = [1, 3, 5, 7, 9, 11]

user_integer = int(input("Please enter an integer number: "))

def get_closest_number(user_integer, list_1):
    ctr = 1
    distance = abs(user_integer - list_1[0])
    closest_number = list_1[0]
    while ctr < len(list_1):
        if distance >= abs(user_integer - list_1[ctr]):
            distance = abs(user_integer - list_1[ctr])
            closest_number = list_1[ctr]
        ctr += 1
    return closest_number

print("The closest number in the list to {0} is {1} ".format(user_integer, get_closest_number(user_integer, list_1)))
'''


print('\nFinding the Closest Number')
numlist = [8, 28, 50]
num = float(input('\nPlease enter a number: '))
if num.is_integer():
    num = int(num)
def get_closest_number(num, numlist):
   ctr = 1;
   closest = numlist[0]               
   diff = abs(numlist[0] - num)
   while ctr < len(numlist):
      nDiff = abs(numlist[ctr] - num)
      if (nDiff < diff):
         diff = nDiff
         closest = numlist[ctr]         
      ctr += 1
   return closest
                  
print('\nList of numbers to compare with: {0}'.format(numlist))
print('\n{0} is closest to {1}.'.format(num, get_closest_number(num, 
numlist)))

'''
#assertions
Input: 56
Output:
Finding the Closest Number
Please enter a number: 56
List of numbers to compare with: [8, 28, 50]
56 is closest to 50.
#Assertion 2
Input: 27
Output:
Finding the Closest Number
Please enter a number: 27
List of numbers to compare with: [8, 28, 50]
27 is closest to 28.
'''

# Challenge 10

print('\nCounting Characters\n')
word = input("Please enter a string: ")
def get_character_count(word):
  uCtr, lCtr, oCtr = 0, 0, 0
  for key, value in enumerate(word):
    if value.isupper(): 
      uCtr += 1
    elif value.islower():
      lCtr += 1
    else:
      oCtr += 1
  return {'Upper case letters':uCtr, 'Lower case letters':lCtr, 'Other characters':oCtr}    
print('\nCharacter Counts:\n')
counter_dict = get_character_count(word)
for key,value in counter_dict.items():
   print('{0}: {1}'.format(key, value))

'''
#assertions
Input: IlikeTIGERS
Output:
Counting Characters
Please enter a string: IlikeTIGERS
Character Counts:
Lower case letters: 4
Upper case letters: 7
Other characters: 0
#assertion 2
Input: I love cats
Output:
Please enter a string: I love cats
Character Counts:
Other characters: 2
Upper case letters: 1
Lower case letters: 8
'''

# Challenge 11

print('\nDisplaying values less than the average in a list\n')
numlist = [23, 45, 62, 33, 76, 13, 24, 66]
def get_average(numlist):
  summation = 0
  for num in numlist:
    summation += num
  return summation / len(numlist)
def get_lower_nums(average, numlist):
  lower_nums = []
  for num in numlist:
    if num < average:
       lower_nums.append(num)
  return lower_nums
average = get_average(numlist)
lower_nums = get_lower_nums(average, numlist)
print('Average: {0}\nValues less than the average: {1} '.format(average, lower_nums))

'''
#assertions
Displaying values less than the average in a list
Average: 42.75
Values less than the average: [23, 33, 13, 24]
'''

# challenge 12

print('\nOnline Store Application\n')

store = {'Greenstone Koru carving': 265, 'Rimu Tiki necklace': 42, 'Manaia bone earrings': 311}

print('Enter the quantity of each item you wish to purchase: \n')

item_quantity = {}

def get_purchase_total(store):
  subtotal = 0  
  for key,value in store.items():
    quantity = input(('{0} @ ${1}, quantity needed?\n'.format(key, value)))
    subtotal += int(quantity) * value
  return subtotal  
     
subtotal = get_purchase_total(store)
print('\nSubtotal is: ${0}'
         '\nGST @15% is: ${1}'
         '\nGrand Total is: ${2:0.2f}'.format(subtotal, .15*subtotal, 1.15*subtotal))

'''
#assertions
Input: 0,1,3
Output:
Online Store Application
Enter the quantity of each item you wish to purchase:
Rimu Tiki necklace @ $42, quantity needed?
0
Greenstone Koru carving @ $265, quantity needed?
1
Manaia bone earrings @ $311, quantity needed?
3
Subtotal is: $1198
GST @15% is: $179.7
Grand Total is: $1377.70
#assertion 2
Input: 1,0,2
Output:
Online Store Application
Enter the quantity of each item you wish to purchase:
Manaia bone earrings @ $311, quantity needed?
1
Greenstone Koru carving @ $265, quantity needed?
0
Rimu Tiki necklace @ $42, quantity needed?
2
Subtotal is: $395
GST @15% is: $59.25
Grand Total is: $454.25
'''

# challenge 13

print('\nWelcome to my Calculator Program!')
print('\nWhen asked for the operation, please enter add, subtract, multiply, divide, or exit.')
print('\nWhen you enter exit, the program will terminate.')
print('\nWhen you enter any of the valid operations, you be prompted for 2 numbers.')
# create an operations dictionary
operations = {'add':'+', 'subtract':'-', 'multiply':'*', 'divide':'/', 'exit':'X'}
def input_number(nth):
  while True:
    n1 = input('\nPlease enter the ' + nth + ' number: ')
    if n1.isnumeric() == True:
      return int(n1)
    elif n1.lower() == 'exit':
      return n1
    else:
      print('You need to enter an integer, try again')
def compute(op, n1 ,n2):
  if op == 'add':
     result = n1 + n2
  elif op == 'subtract':
     result = n1 - n2
  elif op == 'multiply':
     result = n1 * n2
  elif op == 'divide':
     result = n1 / n2
  else:
      return "Error: Compute operation was not found."
  return result
while True: 
  op = input('\nPlease enter the operation: ').lower()
  if op in operations.keys(): 
    if op != 'exit':
       n1 = input_number('first')
       if n1 == 'exit':
           break
       n2 = input_number('second')
       if n2 == 'exit':
           break
       result = compute(op, n1, n2)
       print('\n', n1, operations[op], n2, '=', result)
    else:
        print("Thanks for using the calculator")
        break
  else:
     print('You need to enter one of these: add, subtract, multiply, divide, or exit')
'''
# test case assertion 1
print("\n\nTest case assertion 1 \n\n")
print("3 + 5 = 8")
'''