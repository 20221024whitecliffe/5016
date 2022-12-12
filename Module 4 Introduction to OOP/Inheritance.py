# inheritance.py
# author: lucia
# date: 4.12.2022
'''
class ParentClass:

    {Body}

class ChildClass(ParentClass):

    {Body}
'''
 
'''
class Employee:  #Parent Class
    def intro(self): 
      print("Employee introduction") 

#child class Emp1 inherits the base class Employee
class Emp1(Employee):  #Child Class
    def rank(self): 
      print("I am Director ") 

p1 = Emp1() 
p1.rank() 
p1.intro() 
'''
'''
from abc import ABC 

class ClassName(ABC):

# abc import ABC, abstractmethod

class abs_class(ABC):

    #normal method

    def method(self):

        #method definition

    @abstractmethod

    def Abs_method(self):

        #Abs_method definition
'''
'''
from abc import ABC 

class Person(ABC):  
    # abstract method  
    def occupation(self):
        pass 

class Student(Person):
     def occupation(self):
         print("I am student")  

class Teacher(Person):
     def occupation(self):
         print("I am Teacher")  

class Manager(Person):
    def occupation(self):
        print("I am manager")  

 # Driver code  

s = Student()  

s.occupation()  

t = Teacher()  

t.occupation()  

m = Manager()  

m.occupation()
'''
'''
class Student:

    # constructor

    def __init__(self, name, section,address):  

        # public data member (accessable every where )

        self.name = name

        # protected data memebr (accessable within the class and sub class)

        self._section = section

        #private data memeber (accessable only within the class)

        self.__address=address
'''
'''
class Student:
    def __init__(self, name,section,age):
        self.name = name
        self._section=section #Protected
        self.__age = age   # private member

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

    # getter method
    def get_section(self):
        return self._section

    # setter method
    def set_section(self, section):
        self._section = section

stud = Student('Rose','Pink', 21)

# retrieving age and section using getter
print('Name:', stud.name, stud.get_section(), stud.get_age())

# changing age using setter
stud.set_age(26)
stud.set_section('Blue')

# retrieving age and section using getter
print('Name:', stud.name, stud.get_section(),stud.get_age())
'''
