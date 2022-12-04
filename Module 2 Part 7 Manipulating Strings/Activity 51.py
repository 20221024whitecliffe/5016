# activity51.py
# author: lucia
# date: 3.12.2022

# challenge 1
'''
class_size = int(input("Please enter your class size: "))

list_class = []
for number in range(0, class_size):
    name = input("Please enter student {0} name: ".format(number+1))
    list_class.append(name)

string_students = ", ".join(list_class)
print("Thank you, the names of your students in swapped case are: {0}".format(string_students.swapcase()))
'''
'''
#assertions
Input: 3, Beyonce, Kelly, Michelle
Output: bEYONCE, kELLY, mICHELLE
'''

# challenge 2
'''
sentence = input("Please enter a sentence:\n")

new_sentence = sentence.replace(" ", "|")

print(new_sentence)
'''
'''
sentence = input("Please enter a sentence\n\n")
print("Replacing part of a string...\n{0}".format(sentence.replace(" ", "-
")),"\n")
'''
'''
#assertion
Input: I love tigers
Output:
Replacing part of a string...
I-love-tigers 
'''

# challenge 3
'''
string = "Kiwi North is a great musem!"

reverse_string = "".join(reversed(string))

print(reverse_string)
'''
'''
sentence = "I love tigers"
print("Reversing characters in a string...\n{0}"
      .format(''.join(reversed(sentence))),
      "\n")
'''
'''
#assertions
Input: sentence = "I love tigers"
Output:
Reversing characters in a string...
sregit evol I
'''

# challenge 4
'''
from random import randint 

sentence = "I love tigers"

index = randint(0, len(sentence))
character = sentence[index]

print("The sentence after adding random character is {0}".format(character.join(sentence)))
'''
'''
#assertions
Input: sentence = "I love tigers"
Output:
Inserting a random character into a string...
Ie eleoeveee eteiegeeeres
'''

# challenge 5
'''
bank_account = [["Ben", "Kiwibank", 500], ["Alice", "Nordic Bank", 1000], ["Lucia", "Bank", 1000000001]]

for count in range(0, len(bank_account)):
    list_1 = bank_account[count]
    print("Welcome {0}. Thank you for joining {1}. Your balance is {2}.".format(list_1[0], list_1[1], list_1[2]))
'''
'''
#assertion
Input: list_1 = [["Andrew", "ANZ", 100.00], ["George", "BNZ", 20.30], 
["David", "KiwiBank", 450.21]]
Output:
Welcome Andrew. Thank you for joining ANZ. your balance is $100.0
Welcome George. Thank you for joining BNZ. your balance is $20.3
Welcome David. Thank you for joining KiwiBank. your balance is 
$450.21
'''

# challenge 6
# not working
sentence = "The only thing that scares me is Keyser Soze."

sentence = sentence.replace(" ", "*")
sentence = sentence.lower

new_sentence = ""

for char in range (0, len(sentence)):
    if char % 5 == 0:
        letter = sentence[char]
        letter = letter.upper()
        new_sentence += letter
    else:
        new_sentence += sentence[char]
print(new_sentence)

'''
Traceback (most recent call last):
  File "/Users/lucia/Desktop/IT/Whitecliffe/Software/activity51.py", line 113, in <module>
    for char in range (0, len(sentence)):
TypeError: object of type 'builtin_function_or_method' has no len()
'''














