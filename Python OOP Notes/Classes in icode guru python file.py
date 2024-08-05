#!/usr/bin/env python
# coding: utf-8

# #                OOP
# # There are four pillars of OOp
# # 1: Inheritance
# # 2: Encapsulation
# # 3: Abtraction/abstract
# # 4: Polymorphism
# 
# 
# 
# 
# # Classes/ Objects
# Python is an Object oriented programming language which means that everything in it is an object with its properties and methods.
# In python, each data type is an object that has been instantiated/instance earlier by some class.
# If we want to create a data type of our own, we'll make a class for it, and will define its attributes. 
# 'self' is a convention in which we pass object as parameter
# # self keyword
# self keyword is used for object references. when we create an create an object then self keyword is use to hold the object reference that shows which object it is.
# 
# 
# # Instance=Object
# # Attribute = properties
# # Methods = Function in class

# In[3]:


class person:  #a class named 'person' is created.
    name="Ali"  #class 'person' has property 'name'.
    
p1=person() #an object 'p1' of class is created.
print(p1.name)


# In[18]:


class sum:
    
    def add(self,num1,num2):
        result=num1+num2
        print("The sum is:",result)
    def mul(self,num1,num2):
        print(f"Multiplication is {num1*num2}")
    def sub(self,num1,num2):
        print(f"The subtraction will be {num1-num2}")
obj=sum()
obj.sub(34,22)
obj1=sum()
obj2=sum()
obj1.add(4,5)
obj2.mul(4,9)


# In[16]:


class area:
    def calc_area(self,x,y):
        print("The area of this rectangle is:",x*y)
    
rectangle1=area()
rectangle1.width=5
rectangle1.length=8
    
rectangle2=area()
rectangle2.width=6
rectangle2.length=7
rectangle1.calc_area(rectangle1.width,rectangle1.length)
rectangle2.calc_area(rectangle2.width, rectangle2.length)


# # Constructor
# __init__ method is used as a constructor in python. it is always executed when the class is being initiated.
# Use th init() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
# # Deffination/
# constructor basically used in which things that are not in user control. It works automatically without user permission or any button click.
# # Example
# when we create an mobile application which use internet so we create construcotr in it which checks that internet connection is enable or disable without user permission. if internet is not run then app is not run.
# so we write check internet connection check functionality by using constructor.

# # constructor calling without method/function
# if we not use super() function and self.name then this will not inderited because its necessary to inherit any class

# In[47]:


# simple constructor calling example
class animal:
    def __init__(self,name,sound,age):
        #self.name=name
        #self.sound=sound
        #self.age=age
        print(f"The Name of the animal is {name} and the sound of the animal is {sound}")
class cat(animal):
    def __init__(self,name,sound,age):
        #super().__init__(name,sound,age)
        print(f"the name of the animal is {name} and the sound of the animal is {sound} and the Age is {age} ")
Cat=cat("Cat","meow",15)               


# In[19]:


class sum:
    def __init__(self):
        print("I'm executed!")
obj1 = sum()


# In[20]:


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("John",36)
print(p1.name)
print(p1.age)


# In[1]:


class area:
    def __init__(self,x,y):
        print("The area of this rectangle is:",x*y)

rectangle2=area(5,6)


# In[28]:


class Area:
    def __init__(self):
        x=10
        y=20
        print("The area of this rectangle is :",x*y)
rectangle1=Area()


# In[35]:


class person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"The Name is: {name} and the salary is: {salary}")
person1=person("Ali",50000)
person2=person("Hassan",340000)

print(person1.name)
print(person2.salary)

        
#self.name is used in this class to access the name of the object created.


# # Destructor
# In python, a destrutor is a special method that is clean-up tasks such as releasing resources that were allocated by the object.
# The self parameter in the destructor refers to the object that is being destroyed
# 

# In[9]:


class myclass:
    def __init__(self):
        print("Hello")
    def __del__(self):
        print("myclass.__del__()")
obj=myclass()
print("obj:",obj)
del obj
print("After del obj")
#print("obj:",obj)


# # Access Specifiers
# In python, access specifiers are used to control the visibility and accessibility of class attributes and methods.
# # public: 
# By default, all attributes and methods in a class are public, meaning they can be accessed from anywhere.
# # Private: 
# Python uses a naming convention to idicate private attributes and methods. Attributes and methods that start with a double underscore(_) are considered private and should not be accessed directly from outside the class.
# # Protected:
# Python uses a single underscore(_) at the beginning of an attribute or method name to suggest that it's intended for internal use with in the class and its subclasses.
# 
# 

# In[1]:


class myclass:
    def private_method(self):
        return"this is a private method"
obj=myclass()
# Accessing private method will raise an AttributeError
print(obj.private_method())


# In[1]:


# destructor
class area:
    def rectangle(self,x,y):
        print("Area of Rectangle is = ",x*y)
    def __init__(self): #constructor
            print("constructor is called")
    def __del__(self): #destructor
            print("obj is deleted")
# creating object by calling methods
obj=area()
obj.width=2
obj.height=12
obj.rectangle(obj.width,obj.height)
del obj
#obj.rectangle(obj.width,obj.height) # now obj is deleted so it will not run


# # 1...... Inheritance
# Inheritance is a fundamental conpcept in object-oriented programming (OOP) that allows you to create a new class based on an existing class.
# Inheritance enables code reuse, promotes a hierarichical struture of classes, and allows you to create specialiaed classes from more general ones.
# # parent class/Base Class/ superclass: 
# the class that you're inheriting form. It defines a set of attributes and methods that cab be shared by its subclasses.
# # child class/ derived class/ subclass:
# the new class you're creating . It inherits attributes and methods from the base class and can also have its own attributes and methods.

# In[25]:


class vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def info(self):
        
        print(f"Vehicle Brand is {self.brand} and Model no is {self.model}")
class Car(vehicle):
    def honk(self):
        print("Honk honk!")
#creating instances
car=Car("TOYOTA","Camry")
car.info()
car.honk()
        


# In[56]:


# Example 2
class shape:
    def __init__(self, name):
        self.name=name
    def area(self):
        pass
    
class circle(shape):
    def __init__(self,name,radius):
        super().__init__(name) #Call parent class constructor
        self.radius = radius   # Initialize subclass-specific attribute
    def area(self):            # method overrloading
        return 3.14159 * self.radius**2
class square(shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        
        self.side_length=side_length
    def area(self):
        return self.side_length**2

shapes=[
    circle("circle 1",5),
    square("square 1",6),
    circle("circle 2",7),
    square("square 2",7),
    circle("circle 3",8),
    square("square 3",8)
]

for i in shapes:
    print(f"{i.name} -Area:{i.area()} squar units")
            


# # (i) Single  Inheritance
# 

# In[16]:


class vehicle:
    def display(self):
        print("this is a vehicle.")
class car(vehicle):
    def display_car(self):
        print("this is a car")
car=car()
car.display()
car.display_car()


# # (ii) Multiple Inheritance

# In[26]:


class A:
    def display_A(self):
        print("this is class A.")
class B:
    def display_B(self):
        print("this is class B.")
class C(A,B):
    def display_C(self):
        print("This is Class C.")
c  = C()
c.display_A()
c.display_B()   
c.display_C()


# In[80]:


class transport:
    def __init__(self,nam,model):
        self.nam= nam
        self.model= model
    def display_transport(self):
        print(f"this is our transport {self.nam} class and model {self.model}")
class car(transport):
    def __init__(self,nam,model):
        super().__init__(nam,model)
    def display_car(self):
       print(f"this is our transport {self.nam} class and model {self.model}")
        #print(f"this is our transport {self.name} class and model {self.model}")
#class auto(transport):
    #def display_auto(self):
        #super().__init__(name,model)
        #print(f"This our transport {self.name} and model {self.model}")
Car = car("Toyota", "Camry")
Car.display_transport()
Car.display_car()
#Auto.display_auto()


# # (iii) Heirarichical Inheritance

# In[82]:


class Animal:
    def sound(self):
        pass
class Dog (Animal):
    def sound(self):
        print("Dog Barks.")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
dog=Dog()
cat=Cat()

dog.sound()
cat.sound()

        
        


# In[26]:


class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def soud(self):
        print(f"the name of animal is {self.name} and sound is {self.sound}")
class Dog(Animal):
    def __init__(self,name,sound,age):
        self.age=age
        super().__init__(name,sound)
    def soude(self):
        print(f"The name of animal is {self.name} and sound is {self.sound} and the age is {self.age}")
            # create object
dog=Dog("Tommy","Bark",15)
dog.soud()
dog.soude()


# # (iv) Hybrid Inheritance

# In[5]:


#Hybrid Model
# java cannot support this type reason is below
# only python gives this facility
class A:
    def display_A(self):
        print("This is class B.")
class B(A):
    def display_B(self):
        print("This is class B.")
class C(A):
    def display_C(self):
        print("This is class C.")
class D(B,C):
    def display_D(self):
        print("This is class D.")
d=D()
d.display_A()
d.display_B()
d.display_C()
d.display_D()


# In[6]:


class A:
    def display(self):
        print("This is class B.")
class B(A):
    def display(self):
        print("This is class B.")
class C(A):
    def display(self):
        print("This is class C.")
class D(B,C): # Now it calls B every time because first parent is B
    def disp(self):
        print("This is class D.")
d=D()
d.display()
d.display()
d.display()
d.disp()


# In[7]:


class A:
    def display(self):
        print("This is class B.")
class B(A):
    def display(self):
        print("This is class B.")
class C(A):
    def display(self):
        print("This is class C.")
class D(C,B): # Now it calls C every time Because first parent is C
    def disp(self):
        print("This is class D.")
d=D()
d.display()
d.display()
d.display()
d.disp()


# # Statement and Program
# Write a prorgram that named as trandport whose parameter are name, model create a function named as info create another child
# class named as car who derive from Transport has parameter name, model, speed create method named as feature then again and color. Make another class named as bus who inherit form car properties:
# name, model, speed size as a parameter. Guess which type of inheritence is this??

# In[57]:


class transport:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def info(self):
        print(f"The name is {self.name} and the model is {self.model}")
class car(transport):
    def __init__(self,name,model,speed):
        self.speed=speed
        super().__init__(name,model)
    def feature(self):
        print(f"The {self.model} has {self.speed}")
class vehicle(transport):
    def __init__(self,name,model,color):
        self.color=color
        super().__init__(name,model)
class bus(car):
    def __init__(self,name,model,speed,size):
        self.size=size
        super().__init__(name,model,speed)
Bus=bus("sara","bmw",20,"small")
Car=car("Ali","Kia",249)
Bus.info()
Car.feature()
        


# In[15]:


#overriding
class transport:
    def speed(self):
        pass
class car(transport):
    def __init__(self,color):
        self.color=color
    def speed(self):
        return self.color
class bus(transport):
    def __init__(self,feature):
        self.feature=feature
    def speed(self):
        return self.feature
list=[bus("Mirror"),car("Red")]
for i in list:
    print(i.speed())


# #           2......    Encapsulation
#             (Encapsulation mean data Hiding)
#             There are three type of Access specifier in
#             Encapsulation
# # Access Specifiers/Modifiers
# In python, access specifiers are used to control the visibility and accessibility of class attributes and methods.
# # 1.public:
# By default, all attributes and methods in a class are public, meaning they can be accessed from anywhere.
# # 2.private 
# Python uses a naming convention to indicate private attributes and methods. Attributes and methods that start with a double underscor (__) are considered private and should not ve accessed directly from outside the class
# # 3.protected
# Python uses a single underscore(_) at the beginning of an attribure or method name to suggest that it's intended for internal use within the class and its subclasses.

# In[64]:


class myclass:
    def _privateMethod(self):
        return "This is a private method"
obj=myclass()
result=obj._privateMethod()
print(result)


# In[65]:


# Protected
class protectedexample:
    def __init__(self):
        self._protectedVar= "This is a protected variable"
    def display(self):
        print(self._protectedVar)
obj = protectedexample()
obj.display()           #output: this is a protected variable
print(obj._protectedVar)#output: this is a protected variable


# In[68]:


#Private
class privateExample:
    def __init__(self):
        self.__privateVar = "This is a private variable"
    def display(self):
        print(self.__privateVar)
obj = privateExample()
obj.display() #Output: This is a private variable
# Access the private variable using name managing
print(obj._privateExample__privateVar)# Output: This is private variable


# #   2.1    Encapsulation
# (getter,setter) We use getters & setter to add validation logic around getting and setting a value. To avoid direct access of a class field i.e.
# private variable cannot be accessed directly or modified by external user.
# 
# Using normal function to achieve get and set method

# In[74]:


#Getter/Setter
class Base:
    def __init__(self, age=0):
        self._age=age
    # getter method
    def get_age(self):
        return self._age
    # setter method
    def set_age(self,x):
        self._age=x
ali=Base()
# setting the age using setter
ali.set_age(23)
#retrieving age using getter 
print(ali.get_age())
print(ali._age)


# # Properties:
# properties provide a way to define special methods fo rgetting, setting, and deleting attributes. They are accessed just like normal attrubutes, but beind the scenes, the methods you've defined arecalled. This makes it possible to control attribute access without changing the way you access attributes in your code.
# In python, properties are created using the property() built-in fucntion or the @property decorato. The property() function takes getter, setter and deleter methods as arguments, while the decorator allows you to define the getter method directly above the attribute definatin.

# In[80]:


#property() function
class Base:
    def __init__(self):
        self._age=0
    def get_age(self):
        print("getter method called")
        return self._age
    def set_age(self, a):
        print("setter method called")
        self._age=a 
    def del_age(self):
        print("deleter method called")
        del self._age
    age=property(get_age, set_age,del_age)# a property named "age" is defined which is encapsulating 3 method
mark= Base()

mark.age=10
#del mark.age # After calling this method aga will not print 
print(mark.age) 


# In[5]:


# '@property' decorator
'''Python @property is one of the built-in decorators. the main purpose of any 
decorator is to change your class methods or attrubutes in such a way so that 
the user of your class no need to make any change in their code.'''
class Base:
    __color="pink"
    def __init__(self):
        self._age=0
    #using property decorator
    # a getter fuciton
    @property
    def age(self):
        print("getter method called")
        print("color is:",self.__color)
        return self._age
    
    #a setter fucntion
    @age.setter
    def age(self,a):
        if(a<18):
            raise Exception("Sorry your age is below eligibility criteria")
        print("setter method is called")
        self._age=a
mark = Base()
mark.age=20 # if we use age less than 18 then exception will execute

print(mark.age)
        


# #  3...... Abstraction
# Abstraction is simplifying complex reality by focusing on the essential aspects and ignoring unnecessary details.
# For example, when using a smartphone, you intract with the user interface and fucntionalities it provides, without needing to understand the intricate technical details of how it works internally. Abstraction allows you to use the smartphone as a tool without needing to now erverything about its internal components and processes.

# # Abstraction Class and Methods
# An abstract class is a class that cannot be instantiated directly and is meant to serve as a blueprint for other classes. It may contain both regualr methods with implementations and abstract methods without implementations.
# Abstract methods are declared in the abstract class but lack any concrete code. Abstract methods act as placeholders and must be implemented by concrete (non-abstract) subclasses.

# In[9]:


# Note: we can't make an object of abstract classes
from abc import ABC, abstractmethod
class shape(ABC):
    # defining an abstract method
    @abstractmethod
    def area(self):
        pass
    #defining a concrete method
    def name(self, name):
        self.name=name
        print(f"The shape is {name}")
#subclass "circle" inherits form 'shape'
class circle(shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14159*self.radius**2
#subclass 'Rectangle' inherits from 'Shape'
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
# Attempting to create an instance of the abstract class 'shape'
#This will result in a TypeError since abstract class cannot be instantiated
#shape = shape()  # Uncommenting this line will raise an error beacause we can't make an object of abstract classes
# creating instances of concrete subclasses
Circle=circle(5)
Rectangle=rectangle(4,6)
# using the 'area' method of the subclasses
print("Circle Area:",Circle.area())
print("Rectangle Area",Rectangle.area())
Rectangle.name("rectangle")# this is concrete method


# #     Difference Between Abstraction And Encapsulation
# 
# 
# # Data Abstraction
# # 1
# OOP Concept that hides the implementation details and shows only the fuctionality to the user
# # 2
# Hides the implementation details to reduce the code complexity
# # 3
# OOp languages use abstract classes and interfaces to achieve Data Abstraction
# 
# # Data Encapsulation
# # 1
# OOP concept that vinds or wraps the data and methods together into a single unit
# # 2
# Hides data for the purpose of data protection
# # 3
# OOP languages can achieve Encapsulation by making the data members private and accessing them through public method

# # 4..... Polymorphism
# The word 'polymorphism' means "many forms", and in programming it refers to methods/fuctions/operators with the same name that can be executed on many objects or classes.
# 
# Polymorphism in pyhton, as in many other object-oriented programming languages, refes to the ability of differect objects to respond to the same method or function call in a way that is specific to their individual types or classes. It allows of different classes to be treated as instances of a common base class, providing a unified interface for interacting with objects of diverse types.

# In[12]:


# Function polymorphism
# Python len() function that can be used on different objects
x="Hello World" # string
y={1,3,4,5,6,9,3,7} # Tupple
z={"a":5,
    "b":6,
     "C":8} # Dict
print(len(x))
print(len(y))
print(len(z))
# above shows that len() function works with string,integer and dict etc
# this the example of polymophism 


# In[16]:


#Class polymorphism
# Polymorphism is often used in class method , where we can have multiple classes with the same method name
# {Polymorphic behavior with Duck Typing}
#same method different classes
class dog:
    def speak(self):
        return "Woof!"
class cat:
    def speak(self):
        return "Meow!"
class duck:
    def speak(self):
        return "Quack!"
# A function that demonstrates polymorphism behavior
def animal_sound(self):
    return self.speak()
animals=[dog(),cat(),duck()]
for i in animals:
    print("sound",animal_sound(i))


# In[21]:


# Method Over-riding with Inheritance (Run-time polymorphism)
# same method,classes inherit with parent
class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14159*self.radius**2
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height

#using run-time polymorphism
shapes=[circle(5),rectangle(4,5)]
for shape in shapes:
    print("Area:",shape.area())


# In[22]:


# Dynamic binding of Methods/ overriding
#method same relation parent child
class parent:
    def show(self):
        print("this is the parent class.")
class child(parent):
    def show(self):
        print("this is the child class")
# using dynamic binding to achieve run-time polymorphism
obj1=parent()
obj2=child()
obj1.show()
obj2.show()


# # Exception
# # Try , Exception, Finally

# # Raise an Exception
# As a python you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword

# In[35]:


age= int(input("Enter your age."))
if age<18:
    raise Exception("Sorry minors can't apply fo this")
else:
    print(age)


# In[39]:


#Raising a built -in exception
def divide(a,b):
    if b==0:
        raise ValueError("can't divide by zero")
    return a/b
result=divide(10,0) # Attenpt to divide by zero --> arithmatic exception


# # Custom Exception
# Custom Exception: you can create your own custom by defining new classes that inherit from the exception class or its subclasses. This allows yout to define exceptions that are specific to your applications needs.

# In[4]:


# Define a custom exception class
class mycustomerror(Exception):
    def __init__(self,message):
        super().__init__(message)
    # Function that raise the custom exception
    def validate_age(age):
        if age<0:
            raise mycustomerror("Age can't be Negative")
    user_age = int(input("Enter your age: "))
    validate_age(user_age)
    print(f"Your age is : {user_age}")


# # Exception Handling
# Exception handling in python is a mechanism that allow you to gracefully handle errors or execptional situations that may occur during the execution of a program. Instead of letting these exceptions crash the program, python provides a way to catch and handle them, allowing the program to continue its execution or take appropriate action.
# key concepts and components of exception handling in python include:
# # Try
# The 'try' block lets you test a block of code for errors.(it checks the error in code)
# # Exception
# The 'except' block lets you handle the error. (it handle that error which try generate)
# # Else
# The 'esle' block lets you execute code when there is no error. (If error not occur in try then else part execute the code)
# # Finally
# The 'finally' block lets you execute code, regardless of the result of the try-and except blocks. ( This is execute in every condition)

# In[5]:


try:
    print(abc)
except:
    print("An exception occured.")


# In[10]:


# Exception type
try:
    x=int(input("enter a number:"))
    result=10/x
    name = input("enter your name:")
    print("Hello,"+ name)
except ValueError: # for user wrong input. input character excpet integer 
    # Handle ValueError (e.g., if the user doesn't enter a valid integer)
    print("Invalid input for number")
except ZeroDivisionError:
    #Handle ZeroError (e.g. if the user entes 0)
    print("can't divide by zero")
except Exception as e:
    # Handle any ther exception not caught by previous blocks
    print(f"An error occured :{e}")


# In[12]:


# else
try:
    abc=5
    print(abc)
except:
    print("An error occured.")
else:
    print("Code executed without any error!")


# In[16]:


# finally block without error
try:
    ab=5
    print(ab)
except:
    print("An error occurd.")
else:
    print("Code executed without any error!")
finally:
    print("program ended.")


# In[17]:


# finally block with Error
try:
    ab=5
    if a<5:
        print(ab)
except:
    print("An error occurd.")
else:
    print("Code executed without any error!")
finally:
    print("program ended.")


# In[23]:


# Exception Handling with Custon exception
# Define a custom excetion class
class MyCustomError(Exception):
    def __init__(self,message):
        super().__init__(message)
# function that raises the custom exception
def validate_age(age):
    if age<0:
        raise MyCustomError("Age can't be negative")

    # Example usage of the custom exception
try:
    user_age=int(input("Enter your age: "))
    validate_age(user_age)
    print(f"Your age is: {user_age}")
except MyCustomError as e:
    print(f"Error: {e}")
except ValueError:
    print("Invalid input. Please enter a valid age.")


# # File Handling
# File handling in python is a crucial aspect of programming, as it allows you to read and write data to and from files on your computer. This can be useful for tasks like reading configuration files, processing data, or storing information.
# #        File Opening Modes/python file modes
# # 'r'
# Opens a file for reading.
# # 'w'
# Open a file for writting.
# if file does not exist, it creates a new file.
# if file exists it truncates the file.
# # 'a'
# Open a file in append mode.
# If file does not exist, it  creates a new file.
# # '+'
# Open a file for reading and writing (updating)
# 
# 

# # Opening and Closing Files:
# Python provide built-in fuctions to open and close files . You can use the **open()** function to open a file and the **close()** method to close it when you're done.

# In[ ]:


# Opening a file in read mode
file=open("/example.txt",'r')

# Reading file content
content = file.read()
print(content)

# Closing the file
file.close()


# In[ ]:


# Reading a file line by line
with open ("example.txt","r") as file: # in this we can't have to write file.close at the end it automatically close the file
    for lin in file:
        print(line)
#Reading the entire file content
with open("example.txt","r") as file:
    content = file.read()
    print(content)


# # Writing to Files:
# To write data to a file, open it in write mode **('w')** . you can use **write()** or **writelines()** methods to write data.

# In[ ]:


# writing to a file
with open("output.txt","w") as file:
    file.write("Hello, word!\n")
# writing multiple lines at once
lines=['Line1 \n', "Line2 \n"]
with open ("output.txt", "w") as file:
    file.writelines(lines)


# # Appending to Files:

# In[ ]:


# Appending to a file
with open("output.txt", "a") as file:
    file.write("This is a appended text \n")
    print(file)


# # Working with CSV Files:
# We can use the csv module to read and write CSV file.

# In[ ]:


import csv
# Reading CSV file
with open("data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
# writing to csv fiel
with open("output.csv","w",newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerrow(["Name","Age"])
    csvwriter.writerrow(["Alice",25])

