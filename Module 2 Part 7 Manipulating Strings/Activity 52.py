# activity52.py
# author: lucia
# date: 3.12.2022

# challenge 1
'''
numbers = input("Please enter three numbers with ',' in between: \n")

number_list = numbers.split(",")

average_numbers =  (int(number_list[0]) + int(number_list[1]) + int(number_list[2]))/len(number_list)

print(average_numbers)
'''
'''
user_numbers = input("Please enter 3 integers separated by commas.\n\n")
split_input = user_numbers.split(",")
#turn the list of strings into a list of int
int_list = [int(i) for i in split_input]
#calculate average of items in a list
calc_average = sum(int_list)/len(int_list)
print(calc_average)
'''
'''
#asertions
Input: 3,4,5
Output: 4.0
'''

# challenge 2
'''
user_numbers = input("Please enter any integers separated by commas.\n\n")
split_input = user_numbers.split(",")
int_list = [int(i) for i in split_input]
calc_sum = sum(int_list)
print(calc_sum)
'''
'''
#assertions
Input: 4,6,7,8,2,3,1
Output: 31
'''

# challenge 3
'''
from random import shuffle

sentence = "whatever they say, let it be"

split_sentence =  sentence.split(" ")

shuffle(split_sentence)

print(split_sentence)
'''
'''
#assertions
Input: sentence = "this is a sentence that needs to be shuffled."
Output: ['a', 'shuffled.', 'sentence', 'to', 'this', 'is', 'be', 'needs', 'that']
'''

# challenge 4
'''
sentence = "whatever they say, let it be"

split_sentence = sentence.split(" ")

if len(split_sentence) <= 2:
    print("The string returned is  .")
else:
    new_string = [split_sentence[0], split_sentence[1], split_sentence[-2], split_sentence[-1]]
    print(new_string)
'''
'''
sentence = "This is a sentence from which to make another sentence."
def get_new_sentence(sentence):
    split_sentence = sentence.split()
    if len(split_sentence) < 2:
        return []
    else:
        list_2 = []
        list_2.append(split_sentence[0])
        list_2.append(split_sentence[1])
        list_2.append(split_sentence[-2])
        list_2.append(split_sentence[-1])
        return list_2
print(get_new_sentence(sentence))
'''
'''
#assertion
Input: sentence = "This is a sentence from which to make another sentence."
Output: ['This', 'is', 'another', 'sentence.']
'''

# challenge 5
'''
sentence = "This is a sentence containing words of various length"

sentence_split =  sentence.split()

def get_longest_word(sentence_split):
    longest_word = ""
    for count in range (0, len(sentence_split)):
        if len(sentence_split[count]) > len(longest_word):
            longest_word = sentence_split[count]
    return longest_word
print(get_longest_word(sentence_split))
'''
'''
#assertion
Input: sentence = "This is a sentence containing words of various length."
Output: containing
'''

# challenge 6
'''
sentence = "This is a sentence containing words of various length."
sentence_split = sentence.split()
print("Please enter a number to remove between 1 and ", len(sentence_split), 
"\n\n")
index = int(input())
sentence_split.pop(index - 1)
print(sentence_split)
'''
'''
#assertion
Input: sentence = "This is a sentence containing words of various length."
4
Output: ['This', 'is', 'a', 'containing', 'words', 'of', 'various', 'length.']
'''

# challenge 7
'''
list_of_words = "red,orange,yellow,green,blue,indigo,violet,red,green"
list_split = list_of_words.split(",")
unique_list = set(list_split)
print(unique_list)
'''
'''
#assertions
Input: list_of_words = "red,orange,yellow,green,blue,indigo,violet,red,green"
Output: {'green', 'indigo', 'violet', 'red', 'orange', 'yellow', 'blue'}
'''

# challenge 8
'''
sentence = "This is a string"

def get_reversed_string(sentence):
    if len(sentence) % 4 == 0:
        sentence_reversed = "".join(reversed(sentence))
        return sentence_reversed
    else:
        return sentence

print(get_reversed_string(sentence))
'''
'''
#assertions
Input: sentence = "This is a string."
Output: This is a string.
Input: sentence = "This is a string"
Output: gnirts a si sihT
'''

# challenge 9
'''
eng_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z']
user_input = input("Please enter the text that you wish to encrypt or decrypt,"
                                  "followed by a comma and the integer key.\n\n")
split_user_input = user_input.split(",")
sentence = split_user_input[0]
offset = int(split_user_input[1])
def get_cipher(sentence, offset):
    result = ""
    for count in range(0, len(sentence)):
        num = ord(sentence[count])
        num += offset
        if num > ord('z'):
            num -= 26
        elif num < ord('a'):
            num += 26
        letter = chr(num)
        result += letter
    return result
print(get_cipher(sentence, offset))
'''
'''
#assertion
Input: helloworld,6
Output: nkrrucuxrj
'''

# challenge 10
'''
bunzle = 32
prudential = 22
unilever = 60

def get_trade(company, transaction, share_num):
    if transaction == "sell":
        company -= share_num
        return company
    else:
        company += share_num
        return company
transaction = input("Please enter trade type then a space followed by the share "
                                  "name a commas and the number.\n\n")
input_split = transaction.split(" ")
second_split = input_split[1].split(",")
transaction = input_split[0]
co = second_split[0]
share_num = int(second_split[1])
if co.lower() == "bunzle":
    bunzle = get_trade(bunzle, transaction, share_num)
    print("done! Bunzle shares remaining: ", bunzle)
elif co.lower() == "prudential":
    prudential = get_trade(prudential, transaction, share_num)
    print("done! Prudential shares remaining: ", prudential)
else:
    unilever = get_trade(unilever, transaction, share_num)
    print("done! Unilever shares remaining: ", unilever)
'''
'''
#assertion
Input: 32 sell 10
Output: done! Bunzle shares remaining:  22
Input: buy prudential,47
Output: done! Prudential shares remaining: 69
'''

# challenge 11
import math
def get_perimeter_square(side):
    perimeter = side * 4
    return perimeter
def get_perimeter_triangle(side):
    perimeter = side * 3
    return perimeter
def get_perimeter_circle(radius):
    perimeter = 2 * math.pi * radius
    return perimeter
def get_area_square(side):
    area = side ** 2
    return area
def get_area_triangle(side):
    area = (side / 2) * side
    return area
def get_area_circle(radius):
    area = math.pi * (radius ** 2)
    return area
def get_volume_cube(side):
    volume = side ** 3
    return volume
def get_volume_tetrahedron(side):
    volume = (side ** 3) / 6 * math.sqrt(2)
    return volume
def get_volume_sphere(radius):
    volume = 4 / 3 * math.pi * (radius ** 3)
    return volume
user_input = input("please input square, triangle or circle followed by a comma, then "
                                "volume, perimeter or area followed by a comma and then either the length of the "
                                "side or the radius.\n\n")
split_input = user_input.split(",")
if split_input[0] == "square":
    if split_input[1] == "perimeter":
        print(get_perimeter_square(int(split_input[2])))
    elif split_input[1] == "area":
        print(get_area_square(int(split_input[2])))
    else:
        print(get_volume_cube(int(split_input[2])))
elif split_input[0] == "triangle":
    if split_input[1] == "perimeter":
        print(get_perimeter_triangle(int(split_input[2])))
    elif split_input[1] == "area":
        print(get_area_triangle(int(split_input[2])))
    else:
        print(get_volume_tetrahedron(int(split_input[2])))
else:
    if split_input[1] == "perimeter":
        print(get_perimeter_circle(int(split_input[2])))
    elif split_input[1] == "area":
        print(get_area_circle(int(split_input[2])))
    else:
        print(get_volume_sphere(int(split_input[2])))
'''
#assertions
Input: circle,volume,4
Output: 268.082573106329
Input: triangle,perimeter,6
Output: 18
'''
