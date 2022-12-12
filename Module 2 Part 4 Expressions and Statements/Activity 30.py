# Q1 Challenge 1
# getting user inputs
"""
j = int(input("Please enter height of triagle j\n"))
k = int(input("Please enter bottom of triangle k\n"))

# working out the size
area = j*k/2

print("The area of the triange is", area, "\n")

# Testing

'''
print("My assertions are:"
      "\nj = 5, k = 6 output = 15"
      "\nj = 3, k = 7 output = 10.5")
'''

# Q1 Challenge 2 
# get user input
g = int(input("Please enter height of the rectangle g\n"))
s = int(input("Please enter width of the rectangle s\n"))
q = int(input("Please enter width of the deducted rectangle q\n"))
w = int(input("Please enter height of the deducted rectangle w\n"))

# work out size
shape_area = g*s - q*w

print("The size of the area is", shape_area)

# Test
'''
print("My assertions are:"
      "\ng = 5, s = 6, q = 3, w = 2 output = 24"
      "\ng = 4, s = 8, q = 2, w = 1 output = 30")
'''

# Q1 Challenge 3 
# get user input
m = int(input("Please enter length of the arrow m\n"))
u = int(input("Please enter height of the arrow u\n"))
n = int(input("Please enter edge of the arrow n\n"))

# work out size
arrow_area = m*u + n*n/2

print("The size of the area is", arrow_area)

# Test
'''
print("My assertions are:"
      "\nm = 5, u = 6, n = 3 output = 34.5"
      "\nm = 4, u = 3, n = 5 output = 24.5")
'''

# Q2 Challenge 1
# get user input
x = int(input("Please enter height of the square x\n"))
y = int(input("Please enter width of the square y\n"))

# work out size
moved_area = x*y - 3.14*x*x/2 + 3.14*x*x/2 # 3.14 * x ** 2 / 2 is this expression correct too? yes as below

print("The size of the area is", moved_area)
# print(3.14*x**2/2, 3.14 * x * x /2) tested same

# Test
'''
print("My assertions are:"
      "\nx = 5, y = 6 output = 30"
      "\nm = 4, u = 3 output = 12")
'''

# Q2 Challenge 2 
# get user input
radius = int(input("Please enter radius of the circle c\n"))

# work out size
threequartercircle = 3/4*3.14*radius*radius # radius ** 2

print("The size of the area is", threequartercircle)

# Test
'''
print("My assertions are:"
      "\nc = 5 output = 58.875"
      "\nc = 4 output = 37.68")
'''

# Q2 Challenge 3

import math

# get user input
f = int(input("Please enter width of the triangle f\n"))
g = int(input("Please enter height of the triangle g\n"))
e = int(input("Please enter width of the rectangle e\n"))

# work out size
area = g*e + math.pi*(g/2)**2/2 + g*f/2

print("The size of the area is", area)

# Test
'''
print("My assertions are:"
      "\nf = 6, g = 6, e = 6 output = 68.14"
      "\nf = 9, g = 7, e = 2 output = 64.74")
'''

# Q3 Challenge 1 

import math

# get user input
e = int(input("Please enter longest side of the triangle e\n"))
d = int(input("Please enter bottom side of the triangle d\n"))

# work out size
area = d / 2 * math.sqrt(e**2 - d**2)

print("The size of the area is", area)

# Test
'''
print("My assertions are:"
      "\ne = 5, d = 4 output = 6"
      "\ne = 25, d = 24 output = 84")
'''
"""

# Q3 Challenge 2 
import math

# get user input
f = int(input("Please enter bottom length of the triagle f\n"))

# work out size
"""size = f / 2 * math.tan(40) * f """
# mistake is found in math.tan(40), here I understood 40 as a degree, but it should be radians
degree = math.radians(40)
size = f/2 * math.tan(degree) * f

print("The size of the triangle is", size)

# Test
'''
print("My assertions are:"
      "\nf = 3 output = "
      "\nf = 5 output = ")
'''

# Q3 Challenge 3

import math

# get user input
g = int(input("Please enter height of the triagle g\n"))
e = int(input("Please enter width of the rectangle e\n"))

# work out size
size = g / math.tan(math.radians(38)) * e/2 + g * e + math.pi * (g/2) ** 2 /2

print("The size of the shape is", size)

# Test
'''
print("My assertions are:"
      "\ng = 3, e=2, output = "
      "\ng = 5, e=1  output = ")
'''