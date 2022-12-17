########################   Example1  #########################

#Operations.py

def add(num1,num2):
    print(num1+num2)

def mul(num1,num2):
    print(num1 * num2)
	
	
#client.py

#Approach1
import operations
operations.add(10,20)
operations.mul(10,20)

#Appraoach2
from operations import add,mul
add(10,20)
add(10,20)

#Appraoach3
from operations import *
add(10,20)
add(10,20)



########################   Example2: Same functions in 2 modules  #########################

#animal.py
def fly():
    print("Animal Cant fly")

def color():
    print("Animal is Black")
	
#bird.py
def fly():
    print("Bird Can Fly")

def color():
    print("Bird is Green")
	
#main.py

#Approach1
import animal
import bird

animal.fly()
animal.color()

bird.fly()
animal.color()

#Approach2
from animal import *
fly()
color()
from bird import *
fly()
color()

fly()


########################   Example3: Classes in 2 modules  #########################

#a.py
class Animal():
    def display(self):
        print("I like Cow")

#b.py
class Bird():
    def display(self):
        print("I like Parrot")

		
#main.py

#Approach1
import a
import b

obj1=a.Animal()
obj1.display()

obj2=b.Bird()
obj2.display()

#Approach2
from a import Animal
from b import Bird

obj3=Animal()
obj3.display()

obj4=Bird()
obj4.display()

###############  Example4: Finding How many Classes present in a Module #########################
    ##### Note: Cannot Find How many methods but we can find how many functions in a Module #####
#m.py
class A:
    pass

class B:
    def m1(self):
        print("this is m1 method")
    def m2(self):
        print("this is m2 method")

#main.py
import m
print(dir(m))

###############  Example5: Finding How many Functions present in a Module #########################

#m.py
def m1():
    print("this is m1 method")
def m2():
    print("this is m2 method")

#main.py
import m
print(dir(m))
	



	
	
	
	



