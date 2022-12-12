# QuizNZ.py
# @ author: lucia
# date: 27.11.2022

import time

print("Welcome to test your knowledge about New Zealand\n")

start_time = time.time()
ticker = 0

# quiz 1
sheep_per_person = int(input("Do you know how many sheep per New Zealander has?"))
if sheep_per_person == 5:
    ticker += 1
    print("Well done!", "It makes New Zealand the highest ratio in the world!!!\n")
else:
    print("Ooops!", "Every New Zealander has 5 sheeps making the highest ratio in the world!!!\n")

# quiz 2
location_bungee = input("Do you know where is the first bungee jump in the world located?\n"
                        "A: Dunedin\n"
                        "B: Queenstwon\n"
                        "C: Christchurch\n")

location_bungee = location_bungee.lower()
if location_bungee.lower == "b":
    ticker += 1
    print("Well done!", "The first bungee jump in the world is in Queenstwon\n")
else:
    print("No worries,", "I would have not known if I haven't gone to Queenstown to jump!\n")

# quiz 3
land_mammal = input("Do you know the only native land mammal living in New Zealand?\n"
                    "A: Bat\n"
                    "B: Dog\n"
                    "C: Possum\n")

land_mammal = land_mammal.lower()
if land_mammal.lower == "a":
    ticker +=1
    print("Whoa!", "You do know New Zealand quite well!\n")
else:
    print("I know, it's a tricky question.", "And the answer is BAT!\n")

# quiz 4
coastline_world = int(input("New Zealand has a coastline of 15,134km."
                            "Do you know what is the rank of New Zealand in the world?\n"))
if coastline_world == 9:
    ticker += 1
    print("Bingo!", "You answered correctly!\n")
else:
    print("It is the 9th longest!\n")

# quiz 5
official_language = input("Do you know which of the following is not a New Zealand official language?\n"
                          "A: Sign language\n"
                          "B: Maori\n"
                          "C: English\n")

official_language = official_language.lower
if official_language.lower == "c":
    ticker += 1
    print("Bravo!","Your answer is correct!!\n")
else:
    print("It is shockingly to know that English is actually not an official language!!\n")

finish_time = time.time()
print("Congratulations! You have answered", ticker, "questions correctly!\n")
print("The time you have spent on the quizes is", finish_time - start_time, "seconds.\n\n"
      "Thank you for playing the game!\n")
      