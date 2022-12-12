# challenge 1
# ChessBoard.py
# @ author: lucia
# date: 27.11.2022

column = input("Please enter a column letter from a to h:\n")

if column == "a" or "c" or "e" or "g":
    print("The column starts with black square\n")
else:
    print("The column starts with white square\n")

row = input("Please enter a row number from 1 to 8:\n")

if (row == ("1" or "3" or "5" or "7")) and (column == ("a" or "c" or "e" or "g")):
        print("The square is black\n")
elif (row == ("1" or "3" or "5" or "7")) and (column == ("b" or "d" or "f" or "h")):
        print("The square is white\n")
elif (row == ("2" or "4" or "6" or "8")) and (column == ("a" or "c" or "e" or "g")):
        print("The square is white\n")
elif (row == ("2" or "4" or "6" or "8")) and (column == ("b" or "d" or "f" or "h")):
         print("The square is black\n")

# Test
'''
input row = 1, column = c, output = black, black
input row = 2, column = b, output = white, black
input row = 5, column = d, output = white, white
input row = 6, column = g, output = black, white
'''

# challenge 2
# trianglename.py
# @ author: lucia
# date: 27.11.2022

side_1 = int(input("Please enter one side length of the triangle:\n"))
side_2 = int(input("Please enter 2nd side length of the triangle:\n"))
side_3 = int(input("Please enter 3rd side length of the triangle:\n"))

if (side_1 == side_2) and (side_2 == side_3):
    print("The triangle is an equilateral triangle.\n")
elif (side_1 != side_2) and (side_2 != side_3):
    print("The triangle is scalene.\n")
else:
    print("The triangle is an isosceles triangle.\n")

# Test
'''
side_1 = 6, side_2 = 6, side_3 = 6, output = equilateral
side_1 = 6, side_2 = 5, side_3 = 4, output = scalene
side_1 = 6, side_2 = 4, side_3 = 4, output = isosceles
'''

# challenge 3
# phonebill.py
# @ author: lucia
# date: 27.11.2022

plan = round(float(15),2) # its not possible to show two digits as integer or simply float it. https://bobbyhadz.com/blog/python-add-zeros-after-decimal
air_time = int(input("Please enter how many minutes air time you used this month\n"))
text_message = int(input("Please enter how many text messages you used this month\n"))

additional_air_time = 0.25
additional_text_message = 0.15
flat_charge = 0.44
sales_tax = 0.05
 
print("Base charge is $", plan, "\n")

if air_time > 50:
    additional_minute_charge = round(float((air_time - 50)*additional_air_time), 2)
    print("Additional minutes charge is $", additional_minute_charge , "\n")
else:
    additional_minute_charge = 0

if text_message > 50:
    additional_text_charge = round(float((text_message -50)*additional_text_message), 2)
    print("Additional text message charge is $", additional_text_charge, "\n")
else:
    additional_text_charge = 0

print("The 111 fee is $", flat_charge, "\n")

before_tax = plan + additional_minute_charge + additional_text_charge + flat_charge
total_tax = round(float(sales_tax * before_tax),2)
total_bill = round(float(before_tax + total_tax), 2)
print("The tax is $", total_tax, "\n" )
print("The total bill is $", total_bill, "\n" )

# Test
'''
air_time = 30, text_message = 30, base charge = $15.00, 111 fee = $0.44, tax = $0.77, total bill = $16.21
air_time = 40, text_message = 60, base charge = $15.00, additional text charge = $1.50, 111 fee = $0.44, tax = $0.85 , total bill = $17.79
air_time = 60, text_message = 60, base charge = $15.00, additional minute charge = $2.5, additional text charge = $1.50, 111 fee = $0.44, tax = $, total bill = $
'''

# challenge 4
# cuboid.py
# @ author: lucia
# date: 28.11.2022

decision = input("Please choose if you want to calculate the surface area or the volume of the cuboid\n"
                 "a: area\n"
                 "b: volume\n")
width = int(input("Please type in the width of the cuboid:"))
height = int(input("Please type in the height of the cuboid:"))
length = int(input("Please type in the length of the cuboid:"))

area = 2 * (width * height + width * length + height * length)
volume = width * height * length

if decision == "a":
    print("The area of the cuboid is", area, "\n")
elif decision == "b":
    print("The volume of the cuboid is", volume, "\n")
else:
    print("Your choice doesn't exist.")

# Test
'''
print("My assertion is"
     "decision = a"
     "width = 5"
     "height = 6"
     "length = 3",
     "output = The area of the cuboies is 126")
print("My assertion is"
     "decision = b"
     "width = 3"
     "height = 5"
     "length = 2",
     "output = The volume of the cuboies is 30")
'''