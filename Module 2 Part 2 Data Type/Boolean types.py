# Baby.py
#
# author: A. N. Other
# date: September 2016

import random

male = False # what is the point of writing this line? what if straight using the following line? tried, still worked
male = bool(random.randint(0, 1)) # 0, 1 both included. bool(0) = False, bool(1) = True

if (male):
    print ("We will use name Rangi")
else:
    print ("We will use name Anihera")

""" output = 
We will use name Rangi (random)
"""

# BoolTests.py
#
# author: A. N. Other
# date: September 2016
 
print ("Test 1 ", bool(True))
print ("Test 2 ", bool(False))
print ("Test 3 ", bool("text"))
print ("Test 4 ", bool(""))
print ("Test 5 ", bool(" "))
print ("Test 6 ", bool(0))
print ("Test 7 ", bool())
print ("Test 8 ", bool(3))
print ("Test 9 ", bool(None))

""" output = 
Test 1  True
Test 2  False
Test 3  True
Test 4  False
Test 5  True
Test 6  False
Test 7  False
Test 8  True
Test 9  False
"""