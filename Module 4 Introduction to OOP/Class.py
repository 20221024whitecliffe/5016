# class.py
# author: lucia
# date: 4.12.2022
'''
class Person:
#Class code containing data and behaviour will come here
    age = 10
    gender='male'
    # create a new object of Person class

harry = Person()
sarrah=Person()

# Output: 10

print(harry.age)

print(sarrah.age)
'''
'''
class Person:
  def __init__(self, age, gender):
    self.age = age
    self.gender = gender

herry = Person(36,"male")

sarrah = Person(34, "female")

print(herry.age)
print(sarrah.age)
'''

class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
    def myIntro(self):
        print("Hello my gender is " +self.gender)
        print('Hello my age is', self.age) # , is used when we need to show int or float values.

harry = Person(36,"male")

sarrah = Person(34,"female")

harry.myIntro()

sarrah.myIntro()

# You should pass values in object in same order as mentioned in _init() method.

#In the above example, first age will come, then gender.
