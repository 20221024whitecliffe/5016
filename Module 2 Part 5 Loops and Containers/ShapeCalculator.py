# ShapeCalculator.py
# @author: Lucia
# Date: 28.11.2022

'''
print("Welcome to use the Shape Calculator\n"
          "You can use this calculator to calculate the area or the volume of the shape.\n"
          "You can terminate the calculator by typing 'exit'")

Exit = False

while Exit != True:
    option = input("Please enter your option: area or volume or exit\n")
    if option == "exit":
        Exit = True
        print("The calculator is terminated.\n")
    elif option == "area":
        x = int(input("Please enter an integer number between 0 to 10\n"))
        if x < 0 or x > 10:
            x = int(input("Please enter a valid number between 0 to 10\n"))
        elif 0 <= x <= 10:
            y = int(input("Pease enter an integer number smaller than 8\n"))
            if y < 0 or y > 8:
                y = int(input("Please enter a valid number between 0 to 8\n"))
            else:
                area = (10*8 + 3*8 + 10*3) *2 + y*3*2
                print("The calculated area is: ", area, "\n\n")
    elif option == "volume":
        x = int(input("Please enter an integer number smaller than 10\n"))
        if x < 0 or x > 10:
            x = int(input("Please enter a valid number between 0 to 10\n"))
        elif 0 <= x <= 10:
            y = int(input("Pease enter an integer number smaller than 8\n"))
            if y < 0 or y > 8:
                y = int(input("Please enter a valid number between 0 to 8\n"))
            else:
                volume = 10*3*8 - x*y*3
                print("The calculated area is: ", volume, "\n\n")
'''

chosen_option_valid = False
chosen_option = str
exit_option = str
exit_option_valid = False
side_x = int
side_x_valid = False
side_y = int
side_y_valid = False

print("\nWelcome\n")

'''
while exit_option_valid == False:
    exit_option == input("You may type exit to terminate the program\n")
    if exit_option.lower == "exit":
        exit_option_valid = True
        print("The program is terminated\n\n")
        exit
'''

# use while to get first input
while chosen_option_valid == False:
    choice = input("Enter either Surface or Volume to choose "
                              "whether to calculate surface are or volume,"
                              "\n\n")
    if choice.lower() == "surface":
        chosen_option = "surface"
        chosen_option_valid = True
    elif choice.lower() == "volume":
        chosen_option = "volume"
        chosen_option_valid = True
    else:
        print("Incorrect choice, please try again.....\n\n")

# use while to get x value
while side_x_valid == False:
    side_x = int(input("Enter x as an integer\n\n"))
    if side_x >= 10 and side_x > 0:
        print("\nInvalid side length\n\n")
    else:
        side_x_valid = True

# use while to get y value
while side_y_valid == False:
    side_y = int(input("Enter y as an integer\n\n"))
    if side_y >= 8 and side_y > 0:
        print("\nInvalid side length\n\n")
    else:
        side_y_valid = True

# do area calculation
if chosen_option == "surface":
    surface = (10 * 8 - side_x * side_y) * 2 + (3 *10 * 2) + (3 * 8 * 2) + (side_y * 3) * 2
    print("\nThe surface area of the shape is: ", surface, "\n\n")

# do volume calculation
if chosen_option == "volume":
    volume = (10 * 3 * (8 - side_y))  + (side_y * 3 *(10 - side_x))
    print("\n The volume of the shape is: ", volume, "\n\n")

# Test
'''
print("My assertions are: "
          "nsurface, side_x = 5, side_y = 4, output = 252"
          "\nvolume, side_x = 7, side_y = 3, output =177")
'''
# the sample answer has a few problems:
# it doesn't have option of exit
# one variable was not good, have corrected it