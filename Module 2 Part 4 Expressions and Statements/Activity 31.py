# challenge 1
# m2a31q3c1.py
# @ author: lucia
# date: 27.11.2022

home_distance_4km = True
age_18y = True
imigration_right = True

# Test enrolling right should be true
print("The student can be enrolled", home_distance_4km
      and age_18y
      and imigration_right)

# Test enrolling right when no right to stay in NZ but willing to pay, should be true
imigration_right = False
pay_fees = True
print ("The student can be enrolled", home_distance_4km
       and age_18y
       and imigration_right
       or pay_fees)


# challenge 2
# m2a31q3c2.py
# @ author: lucia
# date: 27.11.2022

registered_user = True
cart_not_empty = True

# Test when registered using paying shopping cart, it should be True
print("You can pay your shopping cart", registered_user
      and cart_not_empty)

registered_user = False
guest_login = True
cart_not_empty = False
gift_card = True

# Test when shopping with guest login and/or for gift card, it should be True
print("You can pay your shopping cart", registered_user
      or guest_login
      and cart_not_empty
      or gift_card)

