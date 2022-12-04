# activity46.py
# author: lucia
# date: 3.12.2022

# challenge 1
'''
name = input("Please type your name")
phone = input("Please type your phone number")

def introduction(name, phone):
    print("Hello there, my name is {0} and my number is {1}.".format(name, phone))

introduction(name, phone)
'''
'''
name = input("\nPlease enter your name: ")
phone_number = input("Please enter your phone number: ")
def display(name, phone_number):
  print("\nHello there, my name is {0} and my number is {1}."
        .format(name,phone_number.rstrip()))
display(name, phone_number)
'''
'''
# test case assertion 1
print("\n\nTest case assertion 1 - input and output shown below.\n\n")
print("Please enter your name: jeff williams\n",
      "Please enter your phone number: 0226921065\n\n",
      "Hello there, my name is jeff williams and my number is  0226921065.")
'''

# challenge 2
'''
base = int(input("\nPlease enter a number: "))
def display_multiples(base):
  ctr = 1
  num = base
  while ctr <= 4:
    num += base
    ctr += 1
    print(num)
    
display_multiples(base)
'''
'''
# test case assertion 1
print("\n\nTest case assertion 1 - input and output shown below.\n\n")
print("Please enter a number: 3\n",
      "6\n",
      "9\n",
      "12\n",
      "15")
'''

# Challenge 3
'''
base = int(input("\nPlease enter a number (x): "))
terms = int(input("\nPlease the number of multiples to generate (y): "))
def display_multiples(base, terms):
    ctr = 1
    num = base
    while ctr <= terms:
        num += base
        ctr += 1
        print(num)

display_multiples(base, terms)
'''
'''
# test case assertion 1
print("\n\nTest case assertion 1 - input and output shown below.\n\n")
print("Please enter a number (x): 2\n",
      "Please the number of multiples to generate (y): 4\n",
      "4\n",
      "6\n",
      "8\n",
      "10")
#'''

# Challenge 4
'''
print('\nSumming list values')

#initialise list
list = [5, 7, 21, 32, 10]
print('\nList Entries:', list)
#sum values in the list
def sum_items(list):
  sum = 0
  for value in list:
      sum += value
  return sum    
print('\nSum of values in the list: {0}'
      .format(sum_items(list)))
'''
'''
# test case assertion 1
print("\n\nTest case assertion 1 - output shown below.\n\n")
print("Summing list values\n\n",
      "List Entries: [5, 7, 21, 32, 10]\n\n",
      "Sum of values in the list: 75\n")
'''

# challenge 5
'''
print('\nCounting Characters')
word = input("Please enter a string: ")
def count_characters(word):
  upper_case, lower_case, other_characters = 0, 0, 0
  for key, value in enumerate(word):
    if value.isupper(): 
      upper_case += 1
    elif value.islower():
      lower_case += 1
    else:
      other_characters += 1    
  print('\nCharacter Counts:'
        '\nUpper case letters: {0}'
        '\nLower case letters: {1}'
        '\nOther characters: {2}'
        .format(upper_case, lower_case, other_characters))
count_characters(word)
'''
'''
# test case assertion 1
print("\n\nTest case assertion 1 - output shown below.\n\n")
print("Counting Characters:\n",
      "Please enter a string: Jeff Williams\n\n",
      "Character Counts:\n\n",
      "Upper case letters: 2\n",
      "Lower case letters: 10\n",
      "Other characters: 1")
'''

# challenge 6
print('\nCounting Even Numbers from this list:')
numlist = [3,5,6,2,13,24,42]
print(numlist)
def count_even_numbers(list):
  counter = 0
  for index, item in enumerate(list):
    if (isinstance(list[index], int)
        and (list[index] % 2) == 0):
      counter += 1
  print('\nThe count of even numbers is: {0}'
        .format(counter))
count_even_numbers(numlist)
'''
# test case assertion 1
print("\n\nTest case assertion 1 - output shown below.\n\n")
print("Counting Even Numbers from this list:\n",
      "[3, 5, 6, 2, 13, 24, 42]\n\n",
      "The count of even numbers is:  4")
'''
