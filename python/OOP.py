# class NameOfTheClass:
#     '''This is a docstring. I have created a class'''
#     Constructors
#     Variables
#         1. Instance Variables
#         2. Class Variables
#         3. Local Variables
#     Methods
#         1. Instance Methods
#         2. Class Methods
#         3. Static Methods
# every method should have self as a parameter. its is ignored at runtime
# self variables are default variables that refers to a current object of a class.
# self variables can be used to initialize the instance variables of a class.
# self helps us access instance variables and methods
# self is a reference variable which refers to the current object. its contains its address in memory.
# self can also be named as anything but it is advisable to use self.

# # example 1 ---> creating an object
# # name_of_the_object = NameOfTheClass()
# class Employee:
#     def display(for_this_place):
#         print("Hi, I'm Elfo!")

# new_object = Employee()
# new_object.display()

# new_object2 = Employee()
# new_object2.display()

# # constructor is a special method in python. it is used to initialize the instance variables of a class.
# # constructor is executed automatically when we create an object of a class.
# # constructor is also known as special method or magic method.
# # constructor is used to initialize the instance variables of a class.
# # constructor has the name __init__.
# # constructor is not mandatory to create in a class.
# class Employee:
#     # def __init__(for_this_place):
#     #     print("Constructor for this place, dey work!!!")
#     def gang_gang(for_this_place):
#         print("Gang Gang, __init__ still dey baba mi!!!")

# emp = Employee()
# emp.__init__() # calling the constructor explicitly
# print(dir(Employee))

# # Parameterized Constructor
# # elfwood == self
# class Employee:
#     def __init__(elfwood, id, name):
#         elfwood.id = id
#         elfwood.name = name

#     def display(elfwood):
#         print("ID -->", elfwood.id)
#         print("Hi I'm", elfwood.name)

# emp = Employee(1, "Elfo")
# emp.display()
# emp2 = Employee(2, "Luci")
# emp2.display()

# methods are functions defined inside a class  ---- constructor is also a method used to initialize the instance variables of a class.

# # instance variable
# class Student:
#     def __init__(elfwood, name, id):
#         elfwood.name = name
#         elfwood.id = id

# s1 = Student("Elfo", 1) # s1 is an object of the class Student and the instance variables are name and id
# s2 = Student("Luci", 2)
# print("Student 1 info:\n", s1.name, "\n", s1.id, end="\n\n")
# print("Student 2 info:\n", s2.name, "\n", s2.id, end="\n\n")

# # instance variable and data hiding
# # data hiding is a concept of OOP where we can restrict the access of instance variables and methods of a class.
# # we can restrict the access of instance variables and methods of a class by using double underscore(__) 
# # before the name of the instance variable or method.
# class Student:
#     def __init__(elfwood, name, id):
#         elfwood.__name = name
#         elfwood.__id = id

# s1 = Student("Elfo", 1) # s1 is an object of the class Student and the instance variables are name and id
# s2 = Student("Luci", 2)
# print("Student 1 info:\n", s1.__name, "\n", s1.__id, end="\n\n")
# print("Student 2 info:\n", s2.__name, "\n", s2.__id, end="\n\n")

# # declaring instance variables inside the constructor
# # every object has a __dict__ attribute which is used to display the object info as dictionary.
# class Employee:
#     def __init__(worker):
#         worker.emp_number = 1
#         worker.emp_name = "Elfo"
#         worker.emp_salary = "Sweets"
# emp = Employee()
# print("Employee Number:", emp.emp_number)
# print("Employee Name:", emp.emp_name)
# print("Employee Salary:", emp.emp_salary)
# print(emp.__dict__)

# # declaring instance variables inside a method:
# class Student:
#     def m1(caller):
#         caller.a = 11
#         caller.b = 21
#         caller.c = 34
#         print(caller.a)
#         print(caller.b)
#         print(caller.c)
# s = Student()
# s.m1()
# print(s.__dict__)

# # declaring instance variables using the objects
# class Test:
#     def __init__(here):
#         print("Constructor here.")
#     def m1(here):
#         print("Instance method.")
# t = Test()
# t.a = 10
# t.b = 20
# t.c = 55
# print(t.a)
# print(t.b)
# print(t.c)
# print(t.__dict__)

# class Test:
#     pass

# t = Test()

# t.a = 11
# t.b = 22

# print(t.a)
# print(t.b)

# # accessing instance varibales from inside
# class Users:
#     def __init__(here):
#         here.a = 11
#         here.b = 22
#     def display(here):
#         print(here.a)
#         print(here.b)

# u1 = Users()
# u1.display()

# # static varibales in python are variables that are not changing. They are class level variables.
# # here == self
# class Student:
#     # static variable
#     college_name = "ISW Tech Academy"
#     def __init__(here, name, id):
#         here.name = name
#         here.id = id

# s1 = Student("Elfo", 1)
# s2 = Student("Luci", 2)

# # accessing static variables with class
# print("Student 1 info:\n", s1.name, "\n", s1.id, "\n", "College name --> ", Student.college_name, end="\n\n")
# print("Student 2 info:\n", s2.name, "\n", s2.id, "\n", "College name --> ", Student.college_name, end="\n\n")

# # accessing static varibles with object
# print("Student 1 info:\n", s1.name, "\n", s1.id, "\n", "College name --> ", s1.college_name, end="\n\n")
# print("Student 2 info:\n", s2.name, "\n", s2.id, "\n", "College name --> ", s2.college_name, end="\n\n")

# # a static varible can be declared
# # inside a class, outside of the method (as shown above).
# # inside the constructor.
# class Demo:
#     def __init__(self):
#         Demo.b = 20
#         print(Demo.b)
# d = Demo() # object automatically displays static varibale b
# # print(Demo.__dict__) # gives the output of class content

# # a static varible can be declared inside the instance method.
# class Pinkman:
#     def meth(breaking_bad):
#         Pinkman.breaking_bad = 146370
#         print(Pinkman.breaking_bad)
# heisenberg = Pinkman()
# heisenberg.meth()
# print(Pinkman.__dict__)

# # a static varible can be declared inside the static method.
# # A function defined inisde a class is a static method using a decorator called @staticmethod, you don't have
# # to give self
# class Demo():
#     @staticmethod
#     def m3():
#         Demo.z =10
#         return Demo.z
# print(Demo.m3())

# # a static varible can be declared inside the class method.
# # A class method uses a decorator @classmethod when creating a class method.
# # you use cls instead of self
# class Demo:
#   @classmethod
#   def m4(cls):
#     cls.c = 30
#     return cls.c
# print(Demo.m4())

# # A decorator is a function that takes another function and extends 
# # the behavior of the latter function without explicitly modifying it.
# # how it works
# def HelloDecorator(func):
#     def inner1():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
#     return inner1

# def function_to_be_used():
#     print("This is inside the function !!")

# function_used = HelloDecorator(function_to_be_used)
# function_used()

# # decorator function
# # how it should be done
# import time
# import math

# def calculate_time(func):
#     def inner1(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print("Total time taken in:", func.__name__, end - begin)
#     return inner1

# @calculate_time
# def factorial_func(num):
#     time.sleep(2)
#     print(math.factorial(num))
# factorial_func(10)

# # a local variable is a varible that is declared and used inside a method.
# # a local variable cannot be accessed outside the method.
# class Demo:
#     def m1(self):
#         a = 10 # local variable
#         print(a)
# d = Demo()
# d.m1()

# # different methods are instance methods, class methods and static methods.
# # instance methods are methods that are declared inside a class and can be accessed using the objects of the class.
# # you must declare self as a parameter in an instance method.
# class Demo:
#     def __init__(self, a):
#         self.a = a # instance variable
#     def method(self):
#         print(self.a)
# d = Demo("Instance method")
# d.method()

# # setter and getter methods
# # setter methods can be used to set the values of the instance variables of a class.
# # they are also known as mutator methods.
# # def set_variable(self, variable):
# #     self.variable = variable
# class Customer:
#     # setter methods
#     def set_name(self, name):
#         self.name = name
#     def set_id(self, id):
#         self.id = id
# c = Customer()
# c.set_name("Elfo")
# c.set_id(1)
# print(c.name)
# print(c.id)

# # getter methods can be used to get the values of the instance variables of a class.
# # they return the values of the instance variables. they are known as accessor methods.
# class Customer:
#     def set_name(self, name):
#         self.name = name
#     def set_id(self, id):
#         self.id = id
    
#     # getter methods
#     def get_name(self):
#         return self.name
#     def get_id(self):
#         return self.id
# c = Customer()
# c.set_name("Elfo")
# c.set_id(1)
# print(c.get_name())
# print(c.get_id())

# # class methods are methods that are declared inside a class and can be accessed using the class name.
# # they act on class variables rather than instance variables.
# # they must be declared using a decorator called @classmethod.
# # they must be declared with a parameter called cls as the first parameter.
# # they are rarely used in python
# class Pizza:
#     radius = 200 # class variable
#     @classmethod
#     def get_radius(cls):
#         return cls.radius
# print(Pizza.get_radius())

# # static methods are methods that are declared inside a class and can be accessed using the class name.
# # they cannot access the class variables and instance variables.
# # it is a general utility method. No need to use self or cls.
# # we can declare it using the decorator @staticmethod.
# # we can access it by using the class name or the object name.
# class Demo:
#     @staticmethod
#     def sum(x, y):
#         print(x + y)
#     @staticmethod
#     def product(x, y):
#         print(x * y)
# Demo.sum(10, 20)
# Demo.product(10, 20)

# # Nested classes
# # they are classes defined inside another class.
# class Outer:
#     def __init__(self):
#         print('Outer class object creation.')
#     class Inner:
#         def __init__(self):
#             print('Inner class object creation.')
#         def method(self):
#             print("Inner class method.")

# a = Outer() # object of outer class prints the __init__ method of the outer class
# b = Outer().Inner() # object of inner class prints the __init__ method of the outer and inner class
# b.method() # prints the method of the inner class

# inheritance is a concept of OOP where we can inherit the properties of one class into another class.
# the existing class is called the super, base, or parent class
# the new class is called the derived or child class
# the derived class inherits the properties (variables, methods, and constructors) of the base class.
# this allows for code reusability.
# application development time will be reduced.
# code redundancy will also be reduced.
# there are three types of inheritance in python:
# single, multiple, and multilevel inheritance.
# single inheritance is a type of inheritance where a derived class inherits the properties of a single base class.
# multiple inheritance is a type of inheritance where a derived class inherits the properties of 2 or more base classes.
# multilevel inheritance is a type of inheritance where a derived class inherits the 
# properties of a base class and the derived class acts as the base class for another class.

# class One():
#     def meth1(self):
#         print("Base class.")

# # single inheritance
# class Two(One):
#     def meth2(self):
#         print("Child class derived from class One.")

# # c = Two()
# # c.meth1()
# # c.meth2()

# # multilevel inheritance
# class Three(Two):
#     def meth3(self):
#         print("Grandchild class derived from class Two.")

# # c = Three()
# # c.meth1()
# # c.meth2()
# # c.meth3()

# # multiple inheritance
# class A:
#     def a(self):
#         print("A class ---> Parent 1.")

# class B:
#     def b(self):
#         print("B class ---> Parent 2.")

# class Four(A, B): # if the method names are the same in both parent classes, 
#     # the method in the first parent class that is called in the child class is executed.
#     def meth4(self):
#         print("Child class derived from class A and B")

# c = Four()
# c.a()
# c.b()
# c.meth4()

# # it is not required to define a default constructor for the derived class if the base class has a default consructor ONLY.
# # if we have argumented constructors in the base class, then it is the responsibility to pass the respective arguments
# # explicitly using the base class constructor.
# class Number():
#     def __init__(self, num):
#         self.num = num
#     def display(self):
#         print(self.num)

# class Power(Number):
#     def __init__(self, num, n):
#         super().__init__(num)
#         self.n = n
#     def display(self):
#         super().display()
#         print(self.n)

# p = Power(2, 3)
# p.display()