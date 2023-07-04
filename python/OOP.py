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

# # inside the instance method.
# class Pinkman:
#     def meth(breaking_bad):
#         Pinkman.breaking_bad = 146370
#         print(Pinkman.breaking_bad)
# heisenberg = Pinkman()
# heisenberg.meth()
# print(Pinkman.__dict__)

# inside the class method.
# inside the static method.