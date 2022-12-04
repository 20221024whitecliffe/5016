# splitstring.py
# author: youtube
# date: 3.12.2022

problems = "broke, pale, short, nerdy"
print(problems)

L = problems.split(",")
'''
L = problems.split("short")
'''
print(L)

joined = "".join(L)

print(joined)
