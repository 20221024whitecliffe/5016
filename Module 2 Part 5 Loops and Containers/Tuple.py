# Tuple.py
#
# @ author: A. N. Other
# date: September 2016
 
bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne", 21025, "45 Green Lane"),
                 ("Anihera", -75))
''' 
print("The number of bank accounts is ", len(bank_accounts))
'''
 
# showing names and balances
'''
for i in bank_accounts:
    print("\nThe name is ", i[0], " and the balance is $", i[1])
'''
 
# showing only names with addresses
'''
for i in bank_accounts:
    if len(i)>2:
        print("\nThe name is ", i[0], " and the address is ", i[2])
'''

# activity 42-2-1
'''
for i in bank_accounts:
    if i[1] < 100:
        print("\n The names of people with less than $100 are ", i[0])
'''
'''
low_balance = 100
for i in bank_accounts:
    if i[1] < low_balance:
        print("\nA customer with less than ${0} is {1}".format(
              low_balance,
              i[0]))
'''

# 42-2-2
'''
for i in bank_accounts:
    if len(i) <= 2:
        print("\nThe customers with either no address or phone numbers are ", i[0])
'''

# 42-2-3 4
'''
balances_list = []
for i in bank_accounts:
    balances_list.append(i[1])
print("\nThe highest balance is ${0}.".format(max(balances_list)))
print("\nThe lowest balance is ${0}.".format(min(balances_list)))
print("\nThe sum of all balances is ${0}.".format(sum(balances_list)))
'''

# 42-2-5
'''
for i in bank_accounts:
    print("\n")
    for customer_detail in i:
        print(customer_detail, end="")
'''

# 42-2-6
'''
for i in bank_accounts:
    if i[1] > 5000 or i[1] <0:
        print("\n")
        for customer_detail in i:
            print(customer_detail, end="")
'''
