# DateTest.py
#
# author: A. N. Other
# date: September 2016
 
from datetime import datetime
from datetime import timedelta
 
date_input = input("Please enter you DOB in the format DD Mmm YYYY: \n")
 
# cast to a datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')
 
# output some confirmation
print ("The year entered is ", date_object.year, "\n")
 
# do a calculation
my_age = datetime.today() - date_object
 
# show the result in different formats
print ("My exact age is ", my_age, "\n")
print ("My exact age just in days is ", my_age.days, "days\n")
print ("My exact age just in years is ", int(my_age.days/365), "years\n")
 
# add 10 days to my current age
print("In 10 days time my age will be ", datetime.today() + timedelta(days=10), ".\n")
 
# add my current age to today's date
print("I will be double my age in ", datetime.today()+ my_age, ".")

print(type(my_age)) # my_age is a datetime.timedelta type

""" input = 20 Sep 1983
output = 
Please enter you DOB in the format DD Mmm YYYY: 
20 Sep 1983
The year entered is  1983 

My exact age is  14320 days, 1:52:34.437948 

My exact age just in days is  14320 days

My exact age just in years is  39 years

In 10 days time my age will be  2022-12-14 01:52:34.438010 .

I will be double my age in  2062-02-17 03:45:08.875980 .
"""
