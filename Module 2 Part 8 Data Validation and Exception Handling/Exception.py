# Exception0.py
#
# @ author: A. N. Other
# date: September 2016

'''
def divide_numbers(number_1, number_2):
    if number_2 == 0:
        return "Cannot divide by zero."
    return number_1 / number_2
 
print(divide_numbers(3,0))
'''

 # Exception1.py
#
# @ author: A. N. Other
# date: September 2016
'''
def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero!"
 
print(divide_numbers(3,0))
'''
# Exception2.py
#
# @ author: A. N. Other
# date: September 2016
 
'''
def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except (ZeroDivisionError, TypeError):
        return "Error, check your parameters!"
 
print(divide_numbers(3,0))
'''

# Exception3.py
#
# @ author: A. N. Other
# date: September 2016
'''
def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero."
    except TypeError as e:
        message = "Error, an operand is the wrong type...\n" \
               "Or as Python would say...\n{0}".format(e)
        return message
 
print(divide_numbers(3,"Four"))
'''
'''
# get an exception's argument
try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as Python would say...\n")
    print(e)
'''

# ExceptionExample3.py
#
# @ author: A. N. Other
# date: September 2016
 
entry_is_valid = False
number_of_goes = 0
while not entry_is_valid:
    try:
        number_entered = int(input("Enter a valid positive integer\n"))
        if number_entered <= 0:
            raise ValueError("Entered value is not a positive integer.")
    except ValueError as e:
        print("The entry is not valid:\n{0}\n"
              "Please try again..."
              .format(e))
    else:
        entry_is_valid = True
        print("Thank you. The acceptable number entered "
              "was {0}.".format(number_entered))
    finally:
        number_of_goes += 1
        print("The number of goes used is...{0}"
              .format(number_of_goes))
