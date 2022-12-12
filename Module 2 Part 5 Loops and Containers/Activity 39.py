# For_Exe1.py
# @author: Lucia
# Date: 1.12.2022

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# For_Exe3.py
# @author: Lucia
# Date: 1.12.2022

import random
target_nub, guess_num = random.randint(1,10), 0
while target_nub != guess_num:
    guess_num =  int(input("Guess a number between 1 and 10 until you get it right"))
print("Well guessed!")

'''
stored_number = 5
guessed_number = int(input("Please guess a number between 1 to 9:\n"))

for guessed_number in range (1, 10):
    if guessed_number == stored_number:
        print("Well guessed!")
        guessed_number = 10
    else:
        print("Try again...")
        guessed_number =  int(input("Please guess a number between 1 to 9:\n"))
'''

# For_Exe8.py
# @author: Lucia
# Date: 1.12.2022

for i in range (0, 6):
    if (i == 3 or i ==6):
        continue  # jump over
    print(i, end=" ")
print("\n\n")

# For_Exe10.py
# @author: Lucia
# Date: 1.12.2022

for i in range(1,51):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    print(i)

# For_Exe21.py
# @author: Lucia
# Date: 1.12.2022


for i in range(1, 7):
    print("*")

print("*" * (i-1))


result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

# For_Exe22.py
# @author: Lucia
# Date: 1.12.2022

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or(row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            result_str=result_str+"* "    
        else:      
            result_str=result_str+"   "    
    result_str=result_str+"\n"    
print(result_str);

# For_Exe27.py
# @author: Lucia
# Date: 1.12.2022

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 4 or (row == 0 and column > 0 and column < 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

# For_Exe31.py
# @author: Lucia
# Date: 1.12.2022

dog_age = int(input("Please type the dog's age in human years: \n"))

if dog_age < 0:
              print("Age must be positive number.")
              exit()
elif dog_age <= 2:
    dog_year = 10.5 * dog_age
else:
    dog_year = 10.5 * 2 + 4 * (dog_age - 2)

print("The dog's age in dog years is ", dog_year, "\n")

h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
	print("Age must be positive number.")
	exit()
elif h_age <= 2:
	d_age = h_age * 10.5
else:
	d_age = 21 + (h_age - 2)*4

print("The dog's age in dog's years is", d_age)

# For_Exe22.py
# @author: Lucia
# Date: 1.12.2022

result_str=""    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row + column == 7):  
            result_str=result_str+"* "    
        else:      
            result_str=result_str+"  "    
    result_str=result_str+"\n"    
print(result_str)

# For_Exe42.py
# @author: Lucia
# Date: 1.12.2022

'''
n =  int(input("Please enter a finish integer number :\n"))

sum_n = n * (n - 1) / 2
average_n = sum_n / n

print("The sum of all integers are ", sum_n, "\n"
          "The average of all integers are ", average_n, "\n")
'''

print("Input some integers to calculate their sum and average. Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1

if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)

# For_Exe43.py
# @author: Lucia
# Date: 1.12.2022

'''
number = int(input("Please enter a integer number between 1 to 10 for multiplication table: \n "))

for number in range(1, 11):
    print("\n", number, "x", "1 = ", number*1, "\n")
    print("\n", number, "x", "2 = ", number*2, "\n")
    print("\n", number, "x", "3 = ", number*3, "\n")
    print("\n", number, "x", "4 = ", number*4, "\n")
    print("\n", number, "x", "5 = ", number*5, "\n")
    print("\n", number, "x", "6 = ", number*6, "\n")
    print("\n", number, "x", "7 = ", number*7, "\n")
    print("\n", number, "x", "8 = ", number*8, "\n")
    print("\n", number, "x", "9 = ", number*9, "\n")
    print("\n", number, "x", "10 = ", number*10, "\n")
'''

number = int(input("Please enter a integer number between 1 to 10 for multiplication table: \n "))

for i in range(1,11):
    print(number, "x", i, "=", number * i)