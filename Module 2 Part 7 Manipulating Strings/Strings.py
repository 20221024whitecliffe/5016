# String1.py
#
# @ author: A. N. Other
# date: September 2016
 
string_1 = "Whanau!"
 
print("The third letter is {0}\n".format(string_1[2]))
print("The length of the string is {0}".format(len(string_1)))
"""
The third letter is a

The length of the string is 7
"""
# String2.py
#
# @ author: A. N. Other
# date: September 2016
 
string_1 = "here is a translation: Haera mai ki konei means come here!"
 
print("The number of times that k appears is {0}\n"
      .format(string_1.count("k")))
 
konei_endindex = string_1.find("konei") + len("konei")
print("The end index position of konei is {0}\n"
      .format(konei_endindex))
 
here_position = string_1.find("here", konei_endindex, len(string_1))
print("Looking for the string_1 here, anytime after konei...\n\n"
         "The string_1 here appears at index position..{0}"
         .format(here_position))
"""
The number of times that k appears is 2

The end index position of konei is 41
Looking for the string_1 here, anytime after konei...

The string_1 here appears at index position..53
"""


# String3.py
#
# @ author: A. N. Other
# date: September 2016
 
string_1 = "Ka mate kāinga tahi ka ora kāinga rua."
 
print("Does this string start with Ka?....{0}\n".format(string_1.startswith("Ka")))
 
print("Does this string start with Tr?....{0}\n".format(string_1.startswith("Tr")))
 
print("Does this string end with rua?....{0}\n".format(string_1.endswith("rua.")))
"""
Does this string start with Ka?....True

Does this string start with Tr?....False

Does this string end with rua?....True
"""

# String4.py
#
# @ author: A. N. Other
# date: September 2016
'''
string_1 = "Hello World"
 
# replacing part of a string
print("Replacing part of a string...\n{0}"
      .format(string_1.replace("Hello", "Goodbye")),
      "\n")
 
#Changing Upper and Lower Case Strings
string_1 = "hElLo wOrlD"
print("Making a string upper case...\n{0}"
      .format(string_1.upper()),
      "\n")
 
print("Making a string lower case...\n{0}"
      .format(string_1.lower()),
      "\n")
 
print("Making a string title case...\n{0}"
      .format(string_1.title()),
      "\n")
 
print("Making a string capitalised...\n{0}"
      .format(string_1.capitalize()),
      "\n")
 
print("Making a string swap case...\n{0}"
      .format(string_1.swapcase()),
      "\n")
 
print("Reversing and inserting characters to a string...\n{0}"
      .format("*".join(reversed(string_1))),
      "\n")
'''
'''
# Python strings have the strip(), lstrip(), rstrip() methods
# for removing any character from both ends of a string.
# If the characters to be removed are not specified then
# white-space will be removed.
 
string_1 = "Hello World"
# Strip off newline characters from end of string_1
string_1.strip("\n")
 
# strip()     removes from both ends
# lstrip()    removes leading characters (Left-strip)
# rstrip()    removes trailing characters (Right-strip)
 
string_1 = "    xyz    "
 
# showing string strip
print("Original string is.... \n")
print("***",string_1,"***\n")
print("Using strip()...\n")
print("***",string_1.strip(),"***\n")
print("Using lstrip()...\n")
print("***",string_1.lstrip(),"***\n")
'''
'''
# Concatenation
 
# To concatenate strings in Python use the "+" operator.
# "Hello " + "World" = "Hello World"
# "Hello " + "World" + "!" = "Hello World!"
 
string_1 = "Hello World"
 
print("Using the join method to add a : between every char...\n{0}"
      .format(":".join(string_1)),
      "\n")
 
print("Using the join method to add a whitespace between every char...\n{0}"
      .format(" ".join(string_1)),
      "\n")
'''
'''
 # Replacing String  

#replace1.py

#Python has replace() method that replaces each matching occurrence of the old  

#character/text in the string with the new character/text.

#The replace() method can take maximum of 3 parameters:

#old - old substring you want to replace#new - new substring which will replace the old substring

#count (optional) - the number of times you want to replace the old substring with the new substring

 

string_1 = "Hello World"

print ('Replacing Hello with GoodBye')

print (string_1.replace('Hello','GoodBye'))
'''
'''
#The upper() method converts all lowercase characters in a string

#into uppercase characters.

string_1 = "Hello World"

print('Converting to uppercase')

print(string_1.upper())

'''

#Strings can be reversed using slicing.
#To reverse a string, create slice that starts
#with the length of the string, and ends at index 0.

string_1 = "Hello World"
stringlength=len(string_1) # calculate length of the list

slicedString=string_1[stringlength:-1] # slicing

print (slicedString) # print the reversed string

s='*'.join(string_1)

print(s)
"""
H*e*l*l*o* *W*o*r*l*d
"""

# String5.py
#
# @ author: A. N. Other
# date: September 2016
 
string_1 = "It's only after we've lost everything " \
                   "that we're free to do anything"
 
# splitting the string
print("Splitting the string...\n{0}"
         .format(string_1.split()),
         "\n")
 
# splitting the string on the letter e
print("Splitting the string on the letter e...\n{0}"
         .format(string_1.split("e")),
         "\n")
"""
Splitting the string...
["It's", 'only', 'after', "we've", 'lost', 'everything', 'that', "we're", 'free', 'to', 'do', 'anything'] 

Splitting the string on the letter e...
["It's only aft", 'r w', "'v", ' lost ', 'v', 'rything that w', "'r", ' fr', '', ' to do anything'] 
"""