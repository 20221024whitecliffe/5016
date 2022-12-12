# UserEntry.py
#
# author: A. N. Other
# date: September 2016
 
print ("Welcome to your first data entry program\n")
user_name = input("Please enter your name...\n")
user_yob = int(input("Please enter your year of birth...\n"))
 
print("Thank you for your input\n")
print("The name that you entered is ", user_name)

# 2022 can be replaced by datetime.year? 
# article https://favtutor.com/blogs/get-current-year-python
# see entended\GetCurrentYear.py
"""
import datetime

today = datetime.datetime.today()
year = today.year
"""

print("Your age in years is ", 2022 - user_yob) # replay 2022 to 'year' to work out get current year

""" input = lucia, 1983
output = 
Welcome to your first data entry program

Please enter your name...
lucia
Please enter your year of birth...
1983
Thank you for your input

The name that you entered is  lucia
Your age in years is  39
"""