# activity46.py
# author: lucia
# date: 2.12.2022

# challenge 1
'''
def add_numbers(x, y):
    """Add two integer numbers."""
    print(x, y)

print("Welcome to use this function:")

add_numbers(3, 5)
'''
# challenge 2
'''
def display_xy(x = int, y = str):
    """Display y text for x times"""
    print(y * x)

x = int(input("Please enter an integer: "))
y = input("Please enter a string: ")

display_xy(x, y)
'''

# challenge 3

import random

def choose_number():
    """Choose number when r is typed."""
    print(random.randint(0, 100))

y = input("Please enter a letter:")

if y == "r":
    choose_number()
else:
    exit



