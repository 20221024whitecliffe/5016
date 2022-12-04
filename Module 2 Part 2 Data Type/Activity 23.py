# challenge 1
# TimeDate.py
# @ Author: Lucia
# Date: 25.11.2022

from datetime import datetime
from datetime import timedelta

date_input = input("Please enter a date in the format of DD Mmm YYYY: ")

date_object = datetime.strptime(date_input, "%d %b %Y")

date_past = date_object - timedelta(days=125)

print("125 days ago, it was ", date_past)

""" input = 20 Sep 1983
output = 
Please enter a date in the format of DD Mmm YYYY: 20 Sep 1983
125 days ago, it was  1983-05-18 00:00:00
"""

# challenge 2
# 2week_date.py
# @ author: Lucia
# Date: 26.11.2022

from datetime import datetime
from datetime import timedelta 

date_input = input("Please input a date in format of DD Mmm YYYY: \n")
date_object = datetime.strptime(date_input, '%d %b %Y')
two_week_date = date_object + timedelta(days=14)

print("In 2 weeks timde, the date will be ", two_week_date)

# challenge 3
# dof_diff_calc.py
# @ author: Lucia
# Date: 26.11.2022

from datetime import datetime

dob1 = input("Please imput first date of birth in fomrat of DD Mmm YYYY: \n")
dob2 = input("Please imput second date of birth in fomrat of DD Mmm YYYY: \n")

date_dob1 = datetime.strptime(dob1, '%d %b %Y')
date_dob2 = datetime.strptime(dob2, '%d %b %Y')
dob_diff = date_dob1 - date_dob2

print("The age difference is ", dob_diff)

# challenge 4
# yearcalc.py
# @ Author: Lucia
# Date: 26.11.2022

from datetime import datetime
from datetime import timedelta

print("Welcome to use date calculator")
date_input = input("Please enter a date in format of DD Mmm YYYY: \n")
year_plus = int(input("Plese enter a number of years you would like to add on: \n"))

date_object = datetime.strptime(date_input, '%d %b %Y')
date_after_plus = date_object + timedelta(days = year_plus*365)

print("The date after", year_plus, "years is", date_after_plus)

# challenge 5
# yeardiffcal.py
# @ author: Lucia
# Date: 26.11.2022

from datetime import datetime
from datetime import timedelta

date1 = input("Please enter the first date in format of DD Mmm YYYY: \n")
date2 = input("Please enter the second date in format of DD Mmm YYYY: \n")

date1_object = datetime.strptime(date1, '%d %b %Y')
date2_object = datetime.strptime(date2, '%d %b %Y')
date_diff = date1_object - date2_object

print("The difference between the two dates in years is", int(date_diff.days/365))