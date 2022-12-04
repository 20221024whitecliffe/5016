# Challenge 1
# author: A. N. Other
# date: September 2016
magnitude = float(input("Please enter magnitude of the earthquake\n\n"))
if magnitude >= 10:
    print("\nThe earthquake is Meteoric""\n\n")
elif (magnitude >= 8 and magnitude <10):
    print("\nThe earthquake is Great""\n\n")
elif (magnitude >= 7 and magnitude <8):
    print("\nThe earthquake is Major""\n\n")          
elif (magnitude >= 6 and magnitude <7):
    print("\nThe earthquake is Strong""\n\n")    
elif (magnitude >= 5 and magnitude <6):
    print("\nThe earthquake is Moderate""\n\n")   
elif (magnitude >= 4 and magnitude <5):
    print("\nThe earthquake is Light""\n\n")   
elif (magnitude >= 3 and magnitude <4):
    print("\nThe earthquake is Minor""\n\n") 
elif (magnitude >= 2 and magnitude <3):
    print("\nThe earthquake is Very minor""\n\n")
else:          
    print("\nThe earthquake is Micro""\n\n")
# Testing
'''
print("My assertions are:"
      "\nmagnitude = 5.7, output = Moderate"
      "\nmagnitude = 0.0, output = Micro"
      "\nmagnitude = 11, output = Meteoric")
'''

# challenge 2
 author: A. N. Other
# date: September 2016
noise_level = float(input("Please enter noise level\n\n"))
if noise_level > 130:
    print("\nThe sound level is greater than that of a jackhammer""\n\n")
elif noise_level == 130:
    print("\nThe sound level is equivalent to a jackhammer""\n\n")    
elif (noise_level > 106 and noise_level <130):
    print("\nThe sound level is between a jackhammer and a petrol lawnmower""\n\n")
elif (noise_level == 106):
    print("\nThe sound level is equivalent to a petrol lawnmower""\n\n")          
elif (noise_level > 70 and noise_level <106):
    print("\nThe sound level is between an alarm clock and a petrol lawnmower""\n\n")    
elif (noise_level == 70):
    print("\nThe sound level is equivalent to an alarm clock""\n\n")   
elif (noise_level > 40 and noise_level <70):
    print("\nThe sound level is between the noise in a quiet room and an alarm clock""\n\n")   
elif (noise_level == 40):
    print("\nThe sound level is equivalent to the noise in a quiet room""\n\n") 
else:          
    print("\nThe sound level is less than that in a quiet room""\n\n")
# Testing
'''
print("My assertions are:"
      "\nnoise_level = 140, output = The sound level is greater than that of a jackhammer"
      "\nnoise_level = 130, output = The sound level is equivalent to a jackhammer"
      "\nnoise_level = 10, output = The sound level is less than that in a quiet room")
'''

# challenge 3
# author: A. N. Other
# date: September 2016
letter = (input("Please enter a letter of the alphabet\n\n"))
if letter.lower() == ("a" or "e" or "i" or "o" or "u"):
    print("\nThe letter you have entered is a vowel\n\n")
elif letter.lower() == "y":
    print("\nSometimes y is a vowel, and sometimes y is a consonant\n\n")    
else:          
    print("\nThe letter is a consonant\n\n")
# Testing
'''
print("My assertions are:"
      "\nletter = a, output = The letter you have entered is a vowel"
      "\nletter = y, output = Sometimes y is a vowel, and sometimes y is a consonant"
      "\nletter = m, output = The letter is a consonant")
'''

# challenge 4
# author: A. N. Other
# date: September 2016
bonus = 0
bonus_base_rate = 2400
rating = float(input("Please enter a rating or either 0.0, 0.4 or 0.6 or higher\n\n"))
if rating == 0.0:
    print("\nUnacceptable performance. Bonus: $",bonus,"\n\n")
elif rating == 0.4:
    bonus = bonus_base_rate * rating
    print("\nAcceptable perfornace performance. Bonus: $",bonus,"\n\n")
elif rating >= 0.6:
    bonus = bonus_base_rate * rating
    print("\nMeritorious performance. Bonus: $",bonus,"\n\n")    
else:          
    print("\nYou have entered an incorrect rating\n\n")
# Testing
'''
print("My assertions are:"
      "\nrating = 0.1, output = You have entered an incorrect rating"
      "\nrating = 0.4, output = Acceptable perfornace performance. Bonus: $ 960.0 "
      "\nrating = 0.5, output = You have entered an incorrect rating"
      "\nrating = 0.6, output = Meritorious performance. Bonus: $ 1440.0 "
      "\nrating = 0.7, output = Meritorious performance. Bonus: $ 1680.0 ")
'''

# challenge 5
# author: A. N. Other
# date: September 2016
year = int(input("Please enter a year\n"))
if year % 12 == 0:
    print("\n" ,year, " is the Year of the Monkey\n")
elif year % 12 == 1:
    print("\n" ,year, " is the Year of the Rooster\n")
elif year % 12 == 2:
    print("\n" ,year, " is the Year of the Dog\n")
elif year % 12 == 3:
    print("\n" ,year, " is the Year of the Pig\n")
elif year % 12 == 4:
    print("\n" ,year, " is the Year of the Rat\n")
elif year % 12 == 5:
    print("\n" ,year, " is the Year of the Ox\n")
elif year % 12 == 6:
    print("\n" ,year, " is the Year of the Tiger\n")
elif year % 12 == 7:
    print("\n" ,year, " is the Year of the Hare\n")
elif year % 12 == 8:
    print("\n" ,year," is the Year of the Dragon\n")
elif year % 12 == 9:
    print("\n" ,year, " is the Year of the Snake\n")
elif year % 12 == 10:
    print("\n" ,year, " is the Year of the Horse\n")
elif year % 12 == 11:
    print("\n" ,year, " is the Year of the Sheep\n")
else:          
    print("\nYou have entered an incorrect year\n")
# Testing
'''
print("My assertions are:"
      "\nyear = 2000, output = Dragon"
      "\nyear = 1998, output = Tiger")
'''