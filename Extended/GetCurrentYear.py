# https://favtutor.com/blogs/get-current-year-python
# GetCurrentYera.py
# Date: 10.12.2022

# 1) By Using today() method
import datetime

today = datetime.date.today()

print(today)

# a) Accessing the year attribute
import datetime

today = datetime.date.today()

year = today.year

print(year)

# b) With srtftime() function 
import datetime

today = datetime.date.today()

year = today.strftime("%Y")

print(year)

# 2) By Using now() method
import datetime

today = datetime.datetime.now()

#accessing the year attribute
year1 = today.year
print(year1)

#using the strftime() method
year2 = today.strftime("%Y")
print(year2)
