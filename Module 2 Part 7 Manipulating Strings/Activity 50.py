# activity50.py
# author: lucia
# date: 3.12.2022

# challenge 1

stored_string = "The first rule of fight club is: do not talk about fight club."

print("The numbers of space in the strings are {0}".format(stored_string.count(" ")))

'''
#assertions
String: fight_club = "The first rule of fight club is: do not talk about fight 
club."
Output: The number of times that a space appears is 12
'''

# challenge 2

print("The numbers of punctuations are {0}".format(stored_string.count(",") + stored_string.count(".") + stored_string.count("")))

'''
#assertions
String: fight_club = "The first rule of fight club is: do not talk about 
fight club."
Output: The number of times that a space appears is 2
'''

# challenge 3

guess = input("Please type your word: ")

if stored_string.startswith(guess) ==  True:
    print("Correct!")
else:
    print("Wrong!")

'''
#Assertions
Input: the
Output: Does this string start with the given text?....False
#assertion 2
Input: The
Output: Does this string start with the given text?....True
'''

# challenge 4

guess = input("Please type your word: ")

if stored_string.startswith(guess) ==  True:
    print("It starts with", guess)
elif stored_string.endswith(guess) == True:
    print("It ends with", guess)
else:
    print("Wrong!")

'''
fight_club = "The first rule of fight club is: do not talk about fight club."
user_text = input("Please enter some case sensitive text.\n\n")
print("Does this string start with the given text?....{0}\n"
      .format(fight_club.startswith(user_text)))
print("Does this string end with the given text?....{0}\n"
      .format(fight_club.endswith(user_text)))
'''
'''
#Assertions
Input: The f
Output:
Does this string start with the given text?....True
Does this string end with the given text?....False
#assertion 2
Input: club.
Output:
Does this string start with the given text?....False
Does this string end with the given text?....True
'''

# challenge 5

fight_index = stored_string.find("fight")
print("The end index position of 'fight' is {0}".format(fight_index))

'''
Input: fight_club = "The first rule of fight club is: do not talk about fight 
club."
Output:
The index position of fight is 18
'''

# challenge 6

fight_index_colon_index = stored_string.find(":")
fight_position = stored_string.find("fight", fight_index_colon_index , len(stored_string))

print("Looking for the word fight anytime after :...\n\n"
         "The word fight appears at index position..{0}"
         .format(fight_position))

'''
#assertion
Input: fight_club = "The first rule of fight club is: do not talk about fight 
club."
Output:
Looking for the word fight, anytime after :...
The word fight appears at index position..51
'''

# challenge 7

email_address = "robert.paulson@hotmail.com"

dot_index = email_address.find(".")

at_index = email_address.find("@")

username_surname = email_address[dot_index+1:at_index]

username = email_address[0] + username_surname

print(username)

'''
#assertion
Input: email_address = "robert.paulson@hotmail.com"
Output: paulsonr
'''

# challenge 8

pin = "789n70"

if pin.isdigit() == True:
    print("The {0} only contains number.".format(pin))
else:
    print("The {0} does not only contain number.".format(pin))

'''
#assertions
Input: pin = "25.0"
Output: This pin contains characters other than digits
Input: pin = "25r0"
Output: This pin contains characters other than digits
Input: pin = "2580"
Output: This pin is made up only of digits
'''

# challenge 9

password = input("Please enter a password:\n")

if len(password) < 8:
    print("The password must contain no less than 8 digits.")
if any(c.isalpha() for c in password) == False:
    print("The password must contain at least 1 alphabet.")
if any(c.isdigit() for c in password)  == False:
    print("The password must contain at least 1 number.")
if any(c.isupper() for c in password) == False:
    print("The password must contain at least 1 upper case.")

'''
#assertions
Input: hello
Output:
The password needs to contain at least 8 characters
The password needs to contain at least one digit
The password needs to contain at least one uppercase character
Input: hellohello
Output:
The password needs to contain at least one digit
The password needs to contain at least one uppercase character
Input: hello123
Output:
The password needs to contain at least one uppercase character
'''

# challenge 10
list_1 = ["tyler.durden@gmail.com", "marla.singer@yahoo.co.nz"]
list_2 = []
for count in range (0, len(list_1)):
    dot_index = list_1[count].find(".")
    at_index = list_1[count].find("@")
    first_name = list_1[count][0:dot_index]
    last_name = list_1[count][dot_index + 1:at_index]
    title_first_name = first_name.title()
    title_last_name = last_name.title()
    list_3 = []
    list_3.append(title_first_name)
    list_3.append(title_last_name)
    list_2.append(list_3)
print(list_2)
'''
#assertion
Input:
list_1 = ["tyler.durden@gmail.com", "marla.singer@yahoo.co.nz"] 
should produce
Output:
list_2 = [['Tyler', 'Durden'], ['Marla','Singer']]
'''