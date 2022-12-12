# tupleyoutube.py
# author: lucia
# date: 1.12.2022

prime_number = [2, 3, 5, 7, 11, 13, 17]
perfect_square = (1, 4, 9, 16, 25, 36)

# display lengths
print("# Primes = ", len(prime_number))
print("# Squares = ", len(perfect_square))
"""
# Primes =  7
# Squares =  6
"""
# iterate over both sequences
for p in prime_number:
    print("Prime: ", p)
for q in perfect_square:
    print("Square: ", q)
'''
Prime:  2
Prime:  3
Prime:  5
Prime:  7
Prime:  11
Prime:  13
Prime:  17
Square:  1
Square:  4
Square:  9
Square:  16
Square:  25
Square:  36
'''
import sys
list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("list size = ", sys.getsizeof(list_eg))
print("tuple size = ", sys.getsizeof(tuple_eg))
"""
list size =  120
tuple size =  104
"""

# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("knows python?", knows_python)
"""
Age =  27
Country =  Vietnam
knows python? True
"""