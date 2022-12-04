# Function1.py
#
# @ author: A. N. Other
# date: September 2016
 
def show_hello():
    print("Hello there, this is my very first function!!!\n\n")
 
print("Testing my first user defined function...\n\n")
 
# invoking the function
show_hello()
 
# invoking the function again
show_hello()

# Function2.py
#
# @ author: A. N. Other
# date: September 2016
 
def show_hello(param):
    print("Hello there, the number of times this "
          "function is called is {0}!!!\n\n".format(param))
 
 
# creating and setting a counter
counter = 0
print("Testing my second user defined function...\n\n")
 
counter += 1
# invoking the function
show_hello(counter)
 
counter += 1
# invoking the function again
show_hello(counter)

# Function3.py
#
# @ author: A. N. Other
# date: September 2016
 
first_number = 13
second_number = 2
 
def show_difference(number_1, number_2):
    print("The first number is {0}.\n"
          "The second number is {1}.\n"
          "The difference between them is {2}!!!\n"
          .format(number_1, number_2, number_1 - number_2))
 
print("Welcome to my difference calculator...\n\n")
 
# invoking the function
show_difference(first_number, second_number)
 
# test case assertion
'''
print("Test case assertion: if first number is 13 and second number is 2 "
    "then the difference should be 11!!")
 
show_difference(13, 2)
'''

# Function4.py
#
# @ author: A. N. Other
# date: September 2016
 
score = 4
 
def show_new_score():
    score += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(score))
# some run code
x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point. "
          .format(score))
# invoking the function
show_new_score()
# test case assertion
'''
print("Test case assertion: the inital score is 4 "
    "and it should become 5!!")
 
show_new_score()
#
'''
'''
Your score is 4 points...

Hit any key to get another point.  
Traceback (most recent call last):
  File "/Users/lucia/Desktop/IT/Whitecliffe/Software/function4.py", line 18, in <module>
    show_new_score()
  File "/Users/lucia/Desktop/IT/Whitecliffe/Software/function4.py", line 9, in show_new_score
    score += 1
UnboundLocalError: local variable 'score' referenced before assignment
'''
