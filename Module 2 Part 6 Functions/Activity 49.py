# activity49.py
# author: lucia
# date: 3.12.2022

# challenge 1

rate = float(input("Please enter the conversion rate between NZD and GBP\n\n"))
type = input("Please enter 'to' or 'from'\n\n")
amount = float(input("Please enter the amount you wish to convert\n\n"))
def get_convert(rate, type, amount):
    result = float
    if type == "to":
        result = amount * rate
    else:
        result = amount * (1 / rate)
    return result
exchange_rate = get_convert(rate, type, amount)
print("The amount of currency when converted {1} NZD is: {0} ".format(exchange_rate, type))

'''
#assertions
Input: 0.44, to, 100
Output:
Please enter the conversion rate between NZD and GBP
0.44
Please enter 'to' or 'from'
to
Please enter the amount you wish to convert
100
The amount of currency when converted to NZD is: 44.0
#assertion2
Input: 0.44, from, 200
Output:
Please enter the conversion rate between NZD and GBP
0.44
Please enter 'to' or 'from'
from
Please enter the amount you wish to convert
200
The amount of currency when converted from NZD is: 
$454.54545454545456
'''

# challenge 2

list_1 = [5, 10, 15, 20, 25]

def get_first_last(list_1):
    list_2 = [list_1[0], list_1[-1]]
    return list_2
new_list = get_first_last(list_1)
print("The first and last items from the list are: ", new_list)

'''
#assertions
Input: list_1 = [5, 10, 15, 20, 25]
Output: The first and last items from the list are:  [5, 25]
'''

# challenge 3

dashes = "---"
slashes = "|  "

def make_dashes(dashes):
    print(dashes, end=" ")
def make_slashes(slashes):
    print(slashes, end=" ")
def board_line():
    for count in range (0, 3):
        make_dashes(dashes)
    print("")
    for count in range (0, 4):
        make_slashes(slashes)
    print("")

for count in range (0,3):
    board_line()

'''
#assertion
Output:
--- --- ---
|   |   |   |
--- --- ---
|   |   |   |
--- --- ---
|   |   |   |
'''

# challenge 4

list_integer = [4, 9, 7]

def histogram(list_integer):
    ctr = 0
    while ctr < len(list_integer):
        print("*" * int(list_integer[ctr]), "")
        ctr +=1

histogram(list_integer)

'''
list_1 = [4, 9, 7]

def histogram(list_1):
    for count in range (0,len(list_1)):
        for item_count in range (0, list_1[count]):
            print("*", end= "")
        print("")
histogram(list_1)
'''
'''
#assertion
Output:
* * * *
* * * * * * * * *
* * * * * * *
'''

# challenge 5

list_words = ["tiger", "leopard", "ocelot", "cheetah", "lion"]
list_lengths = []

def word_length(list_words):
    for count in range (0,len(list_words)):
        num = len(list_words[count])
        list_lengths.append(num)

word_length(list_words)
print(list_lengths)

'''
#assertions
list_words = ["tiger", "leopard", "ocelot", "cheetah", "lion"]
list_lengths = [5, 7, 6, 7, 4]
'''

# challenge 6

def nintynine_bottles_of_beer(counter):
    counter = 99
    for counter in range(99, 0, -1):
        print("{0} bottles of beer on the wall, {0} bottles of beer. Take one down, pass it around, {1} bottles of beer on the wall."
                  . format(counter, counter-1))
    counter -= 1

counter = nintynine_bottles_of_beer(99)

start = 99
lyric_1 = " bottles of beer on the wall, "
lyric_2 = " bottles of beer. Take one down, pass it around, "
lyric_3 = " bottles of beer on the wall."
def get_full_lyric(start):
    print(start, lyric_1, start, lyric_2, start-1, lyric_3)
    start -= 1
    return start
for count in range (0, start):
    start = get_full_lyric(start)
'''
#assertion
Output: Increasingly less numbers of bottles of beer
'''