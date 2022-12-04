# Useless Trivia
#
# Gets personal information from the user and then
# prints true but useless information about him or her

name = input("Hi.  What's your name? ")

age = input("How old are you? ")
age = int(age)

weight = int(input("Okay, last question.  How many pounds do you weigh? "))

print("\nIf poet ee cummings were to email you, he'd address you as",
      name.lower())
print("But if ee were mad, he'd call you", name.upper())

called = name * 5
print("\nIf a small child were trying to get your attention",)
print("your name would become:")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nYou're over", seconds, "seconds old.")

moon_weight = weight / 6
print("\nDid you know that on the moon you would weigh only",
      moon_weight, "pounds?")

sun_weight = weight * 27.1
print("On the sun, you'd weigh", sun_weight, "(but, ah... not for long).")

input("\n\nPress the enter key to exit.")
""" input = lucia, 39, 4
output =
Hi.  What's your name? lucia
How old are you? 39
Okay, last question.  How many pounds do you weigh? 4

If poet ee cummings were to email you, he'd address you as lucia
But if ee were mad, he'd call you LUCIA

If a small child were trying to get your attention
your name would become:
lucialucialucialucialucia

You're over 1229904000 seconds old.

Did you know that on the moon you would weigh only 0.6666666666666666 pounds?
On the sun, you'd weigh 108.4 (but, ah... not for long).


Press the enter key to exit.
"""