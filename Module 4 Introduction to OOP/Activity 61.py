# activity61.py
# author: tutor
# 4.12. 2022

class Person:
  def __init__(self,name, age,gender,edu):
    self.name=name
    self.age = age
    self.gender=gender
    self.edu=edu
  def myIntro(self):
    print("Hello my name is "+self.name)
    print('My age is', self.age)
    print("I am " +self.gender)
    print("I have done " +self.edu)
  
person1 = Person("harry",34,"male",'Masters') 
person2= Person("Jhon",43,"male",'Masters') 
person1.myIntro()
person2.myIntro()
"""
Hello my name is harry
My age is 34
I am male
I have done Masters
Hello my name is Jhon
My age is 43
I am male
I have done Masters
"""