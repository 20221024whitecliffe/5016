# challenge 1
# 1ton.py
# author: lucia
# date: 28.11.2022

n = int(input("Please enter a number"))
counter = 1

while counter <= n:
    print("["+str(counter)+"]\n")
    counter += 1

# Test
'''
print("My assertions are"
      "n = 1, output = [1]"
      "n = 2, output = [1][2]"
      "n = 3, output = [1][2][3]")
'''

# challenge 2
# sumint.py
# @ author: Lucia
# Date: 28.11.2022
counter = 1
sum_n = 0

n = int(input("Please input an integer number:"))

while counter <= n:
    sum_n = sum_n + counter
    counter += 1

print("The sum of 1 to", n, "is", sum_n)

# Test
'''
print("My assertions are:"
          "\nn = 5, output = 15"
          "\nn = 19, output = 190")
'''

# challenge 3
# multiplebetweenpq.py
# author: lucia
# date: 28.11.2022

# this is not working as supposed to be.


p = int(input("Please enter a integer number smaller than 10"))
q = 1

while q < 10:
    q = int(input("Please enter an ending number greater than 10\n\n"))
    counter = 1
    starting_number = p
    if p <= 10:
        while starting_number <= 10:
            starting_number = p * counter
            counter += 1
        while counter < q:
            print(starting_number, end=",")
            starting_number = starting_number + p
            counter += p

# Test
'''
print("My assertions are:"
          "\np = 4, q = 25 output = 12,16,20,24"
          "\np = 3, q = 17 output = 12,15")
'''

# challenge 4
# password.py
# author: lucia
# date: 28.11.2022

password = input("Please enter a password\n")
counter = 1

while password.lower != "exit" and counter < 3:
    counter += 1
    password = input("Please enter a password\n")

print("The program is terminated")

# Test
'''
print("My assertions are:"
         "password = abc, output = please enter a password"
         "password = exit, output = The program is terminated")
'''

# challenge 5
# guessgame.py
# author: lucia
# date: 28.11.2022

secret_number = 12
guess = int(input("Please guess the secret number\n"))
counter = 0
last_guess = int
found = False

while found != True:
    if guess < secret_number:
        print("The number you guessed is smaller than the secret number\n")
        if last_guess != guess:
              counter += 1
        last_guess = guess
        guess = int(input("Guess another number"))
    elif guess > secret_number:
        print("The number you guessed is bigger than the secret number\n")
        if last_guess != guess:
           counter += 1
        last_guess = guess
        guess = int(input("Guess another number"))
    else:
        counter += 1
        print("Your answer is right\n")
        found = True

print("Your have guessed", counter, "times\n")

# Test
'''
print("My assertions are:"
         "guess = 12 output = your answer is right"
         "guess = 1,3,12 output = smaller counter = 3("Your answer is right\n")"
         "guess = 13, 13,13, 12 output = bigger counter=2")
'''