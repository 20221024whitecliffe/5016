# activity43.py
# author: lucia
# date: 2.12.2022

# challenge 1
'''
dict_1 = {"add": "+", "minus": "-", "multiple":"*"}

dict_1["divide"] = "/"

print(dict_1)
'''

# challenge 2
'''
dict_1 = {"add": "+", "minus": "-", "multiple":"*"}
dict_2 = {"divide":"/", "percent":"%", "square":"^"}

dict_1.update(dict_2)

print(dict_1)
'''

# challenge 3
'''
dict_1 = {"add": "+", "minus": "-", "multiple":"*"}
print(dict_1)
'''

# challenge 4
'''
dict_1 = {"number1:":1, "number2:":2, "number3:":3, "number4":4}

sum_value = 0

for item in dict_1.values():
    sum_value += item

print(sum_value)
'''
'''
print('\nSumming dictionary values')
#initialise dictionary 1 
city_dict1 = {'AKL':1495, 'CHC':389.7, 'DUD':118.5, 'WLG':405}
print('\nCity Dictionary 1:',city_dict1)
#sum values in the dictionary
sum = 0
for popn in city_dict1.values():
    sum += popn
print('\nTotal population in the major cities (in thousands):')
print(sum)
'''
'''
# assertion output should be:
Total population in the major cities (in thousands):
2408.2
'''

# challenge 5
'''
print('\nDeleting entry from a dictionary')
#initialise dictionary 1 and 2
city_dict1 = {'AKL':'Auckland', 'CHC':'Christchurch', 'DUD':'Dunedin', 'WLG':'Wellington'}
print('\nCity Dictionary 1:',city_dict1)
#remove the dictionary entry for Dunedin
del(city_dict1['DUD'])
print('\nUpdated city Dictionary (Dunedin deleted):')
print(city_dict1)
'''
'''
# assertion output should be missing the Dunedin entry
'''

# challenge 6
#initialise dictionary 1
city_dict1 = {'AKL':'Auckland', 'CC':'Christchurch', 'DUD':'Dunedin', 'WLG':'Wellington', 
'AUK':'Auckland'}
print('\nCity Dictionary 1:',city_dict1)
indexes_to_delete = []
print('\nDeleting entries from dictionary where key length is 2')
for val in city_dict1.keys():
    if len(val)==2:
        indexes_to_delete.append(val)
for items in indexes_to_delete:
    del(city_dict1[items])
print('\nCity Dictionary 1:', city_dict1)
'''
# assertion: output should be missing the Christchurch entry
'''
