# activity17.py
# @ author: Lucia
# Date: 24.11.2022

# challenge 1
# creating variable, calculate circle area, know data type
pi = 3.1415926535
r = 6
area = pi*r**2

print(area)
print(type(r))
print(type(area))

""" Output = 
113.097335526
<class 'int'>
<class 'float'>
"""

# challenge 2
# use simple calculations, know data type
x = 4
y = 7
z = 34.7
add =  x + y + z
print(add)
print(type(x))
print(type(y))
print(type(z))
print(type(add))

""" output = 
45.7
<class 'int'>
<class 'int'>
<class 'float'>
<class 'float'>
"""

# challenge 3
# use simmple calculation, get result
x = 3 + 7j
y = 9j

print(x.real)
print(x.imag)
print(y.real)
print(y.imag)

#add one line to see type of x.real
print(type(x.real))

""" output = 
3.0
7.0
0.0
9.0
<class 'float'>
"""