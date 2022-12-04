# for.py
# author: lucia
# date: 30.11.2022
'''
for counter in range(5):
      print("hello world")
'''

# ForLoop.py
#
# @ author: A. N. Other
# date: September 2016
'''
user_input = int(input("Please enter the number of times "
                       "that you wish to see the message."))
 
for i in range(user_input):
    print("hello world....", i)
'''
 
# ForLoopNested.py
#
# @ author: A. N. Other
# date: September 2016
 
user_input = int(input("Please enter a number for the size"
                       "of the shape you wish to create."))
 
for i in range(user_input):
    for j in range(i):
        print('* ', end="")
    print('')
 
for i in range(user_input, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')
