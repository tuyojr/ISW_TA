# print("hello world!")

# # declaring multiple variables in one line
# a, b, c = 1, 2, 3
# print(a, b, c)

# # assigning a single value to multiple variables
# d = e = f = 4
# print(d, e, f)

# emp_id = 11
# name = 'Irfan'
# salary = 2000.40

# print('My employee id is: ', emp_id)
# print('My name is: ', name)
# print('My salary is: ', salary)

# g = range(5, 0, 2)
# for num in g:
#     print(num)

# h = 3
# k = 2
# print(h+k)
# print(h-k)
# print(h*k)
# print(h/k)
# print(h%k)
# print(h**k)
# print(h//k)

# print(15 and 8) # 8
# print(15 or 8) # 15

# m, n = 13, 5
# m += n
# print(m)
# m -= n
# print(m)

# # Memebership operators
# text = "Welcome to python programming"
# print("Welcome" in text) # True
# print("Welcome" not in text) # False
# print("Nireekshan" in text) # False
# print("Han" not in text) # True

# # Identity operator
# j, k = 25, 26
# print(j is k)
# print(j is not k)
# print(id(j))
# print(id(k))

# # Input and Output Operator
# name = input("Enter the name: ")
# age = input("Enter the age: ")
# print("Your name is: ", name)
# print("Your age is: ", age)

# age = int(input("Enter your age: "))
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("Your age is: ", age)
# print("Sum of two values: ", x + y)
# print("Age type is: ", type(age))

# print(eval('10 + 10'))

# from sys import argv

# print(argv[0])
# print(argv[1])
# print(argv[2])
# print(argv)

# loc1 = """XYZ company
# Wjile Field
# Bangalore"""

# loc2 = """XYZ company
# Bangalore
# Human tech park"""

# print(loc1)
# print(loc2)

# # Indexing
# string = "ABCDEFGHI"
# print(string[-1])

# Slicing [start:stop:step]
# alphabets = "ABCDEFGHI "
# print(alphabets[3:6])
# print(alphabets[3:-1])
# print(alphabets[1:-1:2])

# value = 3
# print(value * alphabets)

# # comparing strings
# s1 = "abcd"
# s2 = "abcdefg"
# print(s1 == s2)
# if (s1 == s2):
#     print("Both are equal")
# else:
#     print("Both are not equal")

# s3 = "A"
# s4 = "a"
# print(s3 > s4) # False
# print(s3 < s4) # True

# # String methods
# s = "Welcome to python programming"
# print(s.rstrip()) # removes the spaces at the end of the string
# print(s.lstrip()) # removes the spaces at the beginning of the string
# print(s.strip()) # removes the spaces at the beginning and end of the string

# # find substring
# s = "Welcome to python programming"
# print(s.find("python")) # 11
# print(s.find("java")) # -1
# print(s.index("python")) # 11
# print(s.rfind("o")) # 20 >>> backward search
# print(s.rindex("o")) # 20 >>> backward search
# # find(str, start, end)
# print(s.find("o", 10, 20)) # 15
# # index(str, start, end)
# print(s.index("o", 10, 20)) # 15
# # find multiple occurences of a substring
# print(s.find("o", s.find("o") + 1)) # 9

# # count(str, start, end)
# s = "Welcome to python programming"
# print(s.count("o")) # 4
# print(s.count("o", 10, 20)) # 1
# # replace(old, new, count)
# print(id(s[11]))
# print(s.replace("python", "java")) # Welcome to java programming
# print(id(s[11]))

# # split(str, count) ---> returns a list
# s = "Welcome to python programming"
# # default of split is space
# print(s.split()) # ['Welcome', 'to', 'python', 'programming']

# # "joining-character".join(str) ---> returns a string
# s = ["Welcome", "to", "python", "programming."]
# print(" sigh ".join(s)) # Welcome to python programming

# # capitalize()
# s = "welcome to python programming"
# print(s.capitalize()) # Welcome to python programming

# # title()
# s = "welcome to python programming"
# print(s.title()) # Welcome To Python Programming

# # upper()
# s = "welcome to python programming"
# print(s.upper()) # WELCOME TO PYTHON PROGRAMMING

# # lower()
# s = "WELCOME TO PYTHON PROGRAMMING"
# print(s.lower()) # welcome to python programming

# # swapcase()
# s = "Welcome To Python Programming"
# print(s.swapcase()) # wELCOME tO pYTHON pROGRAMMING

# # format()
# s = "Welcome to {} programming"
# print(s.format("python")) # Welcome to python programming
# print(f"Welcome to {'python'} programming") # Welcome to python programming
# print("Welcome to {0} programming".format("python")) # Welcome to python programming
# print("Welcome to {x} programming".format(x = "python")) # Welcome to python programming

# # Write a program to remove characters that have odd index values in a given string
# # The quick brown fox jumps over the lazy dog
# s = input("Enter a string: ")
# # s[start:stop:step]
# print("Your odd removed string is: ", s[::2]) # index + 2

# # Write a program to count the number of characters (character frequency) in a string
# print(s.count(input("Enter a word to count: ")))

# # Write a program to count repeated characters in a string
# # thequickbrownfoxjumpsoverthelazydog
# print(s.count(input("Enter a letter to count: ")))
# s = "thequickbrownfoxjumpsoverthelazydog"
# w1 = input("letter 1? ")
# print(s.count(w1))
# w2 = input("letter 2? ")
# print(s.count(w2))
# w3 = input("letter 3? ")
# print(s.count(w3))
# wc1 = s.count(w1)
# wc2 = s.count(w2)
# wc3 = s.count(w3)
# print("{}{} {}{} {}{}".format(w1, wc1, w2, wc2, w3, wc3))

# # Conditional statements
# # single if else statement
# salary = int(input("Enter your current salary: "))

# if salary > 65000:
#     new_salary = salary - (salary * 0.05)
#     print("Your new salary is: ", new_salary)
# else:
#     new_salary = salary + (salary * 0.01)
#     print("Your new salary is: ", new_salary)

# # if elif else statement
# choice = int(input("Enter your choice (1 = Python, 2 = Java, 3 = Ruby, 4 = C#): "))
# if choice == 1:
#     print(f"You have selected '{1}' --> Python as your programming language.")
# elif choice == 2:
#     print(f"You have selected '{2}' --> Java as your programming language.")
# elif choice == 3:
#     print(f"You have selected '{3}' --> Ruby as your programming language.")
# elif choice == 4:
#     print(f"You have selected '{4}' --> C# as your programming language.")
# else:
#     print("You have selected a non-existent choice, run the program again.")

# # write a code which takes 3 numbers as input and prints the largest number
# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))
# num_3 = int(input("Enter third number: "))

# if num_1 > num_2 and num_1 > num_3:
#     print(f"{num_1} is the largest number.")
# elif num_2 > num_1 and num_2 > num_3:
#     print(f"{num_2} is the largest number.")
# elif num_3 > num_1 and num_3 > num_2:
#     print(f"{num_3} is the largest number.")
# else:
#     print("All numbers are equal.")

# # tenary operator ---> single line conditional statement
# # this_if_condition_is_true if condition_is_true else print_this_value
# a, b = 10, 20
# min = a if a < b else b
# print(min)

# # ternary operator for three conditions
# # this_if_condition_is_true if condition_is_true else this_if_condition_is_true if condition_is_true else print_this_value
# a, b, c = 10, 20, 30
# min = a if a < b and a < c else b if b < c else c
# print(min)

# Looping ---> iteration
# while loop works on the basis of condition ---> codition initialization (must be true) ---> condition incrementation (must be false)
# x = 1
# while x <= 5:
#     print(x) # 1 2 3 4 5
#     x += 1
# print("End of while loop.")

# #  write a program which enters a string and prints the odd index values of the string
# string = input("Enter a string: ")
# odd_index = 1
# while odd_index < len(string):
#     print(string[odd_index], end="")
#     odd_index += 2

# #  write a program which enters a string and prints the odd index values of the string in reverse order
# string = input("Enter a string: ")
# odd_index = -1
# while odd_index > -len(string):
#     print(string[odd_index], end="")
#     odd_index -= 2

# # for loop works on the basis of sequence
# lists = [10, 20, 30, "Python"]
# for item in lists:
#     print(item) # 10    \n  20  \n  30  \n  Python

# characters = "Python"
# for character in characters:
#     print(character) # P  \n  y  \n  t  \n  h  \n  o  \n  n

# grocery_costs = [10, 20, 30]
# goods = 2
# for grocery in grocery_costs:
#     print(grocery + goods) # 12 \n  22  \n  32

# for num in range(1, 5):
#     print(num)  #   1   \n  2   \n  3   \n  4

# # declare a string and use the range function to print it in reverse order
# s = input("Please enter a string: ")

# for characters in range(len(s) - 1, -1, -1):
#     print(s[characters])

# # accumulation variable
# # sum = 0 ---> because we're adding. if we were multiplying, we'd use 1. if we were dividing, we'd use 0.
# grocery_costs = [10, 20, 30]
# sum = 0
# for grocery in grocery_costs:
#     sum = sum + grocery
# print(sum)

# # Write a program which enters a number and prints the factorial of that number
# number = int(input("Enter a number: "))
# factorial = 1
# for numbers in range(1, number + 1):
#     factorial = factorial * numbers
# print(factorial)

# # write a program and print the power of the number raised to that power
# number = eval(input("Enter a number: "))
# power = eval(input("Enter the power: "))
# result = 1
# for numbers in range(1, power + 1):
#     result = result * number
# print(result)

# # represent a binary number input as a string, in decimal.
# binary = input("Enter a binary number: ")
# decimal = 0
# for index in range(len(binary)):
#     digit = binary[index]
#     decimal = decimal + int(digit) * 2 ** (len(binary) - 1 - index) # first loop ---> decimal = 0 + (1 * 2 ** (6 - 1 - 0)) = 32
# print(decimal)

# # nested loop
# rows = range(1, 5)
# for row in rows:
#     for star in range(1, row + 1):
#         print('* ', end='')
#     print()

# # reverse case
# rows = range(5 - 1, -1, -1)
# for row in rows:
#     for star in range(-1, row - 1):
#         print('* ', end='')
#     print()

# # Break statement
# group = [1, 2, 3, 4]
# search = int(input("Enter the search number between 1 and 4: "))
# for element in group:
#     if search == element:
#         print(f"The element {search} was found in the group {group}.")
#         break
#     else:
#         print(f"The element {search} was not found in the group {group}.")
#         break

# # Continue statement
# cart = [10, 20, 500, 700, 50, 60]
# for item in cart:
#     if item >= 500:
#         continue
#     print("Item:", item)

# # loops with else statements
# # if the for loop executes completely, the else statement will execute
# group = [1, 2, 3, 4]
# search = int(input("Enter the search number between 1 and 4: "))
# for element in group:
#     if search == element:
#         print(f"The element {search} was found in the group {group}.")
#         break
# else:
#     print(f"The element {search} was not found in the group {group}.")

# pass statement ---> used as a placeholder for future code
# for num in range(1, 10):
#     pass

# # do while loop
# total = 0
# while True:
#     num = int(input("Enter a number (or 0 to exit): "))
#     if num == 0:
#         break
#     total += num

# print("Total: ", total)

# thequickbrownfoxjumpsoverthelazydog
# o4 e3 u2 h2 r2 t2
# s = input("Enter a string: ")
# letters = input("Enter the characters you wish to count separated by whitespace: ")

# for letter in letters.strip():
#     if letter in s:
#         print(letter, s.count(letter), end=' ')

# S = input("Enter a string: ")
# check1 = "*"
# check2 = "#"

# if S.count(check1) == S.count(check2):
#     print(0)
# elif S.count(check1) > S.count(check2):
#     print(1)
# else:
#     print(-1)

# # Defining functions
# def sum(a, b):
#     print("Sum of two values =", (a + b))

# sum(int(input("Enter first number: ")), int(input("Enter second number: ")))

# # Write a function that executes based on the operator passed in
# def sum(num1, num2, operator):
#     if operator == '+':
#         print("The sum is: ", (num1 + num2))
#     elif operator == '-':
#         print("The difference is: ", (num1 - num2))
#     elif operator == '*':
#         print("The multiplication is: ", (num1 * num2))
#     elif operator == '/':
#         print("The division is: ", (num1 / num2))

# sum(20, 10, '+')
# sum(20, 10, '-')
# sum(20, 10, '*')
# sum(20, 10, '/')

# # Using the return keyword
# def sum(a, b):
#     c = a + b
#     return c

# x = sum(1, 2)
# print("Sum of two numbers is: ", x)

# # return keyword returning nothing ---> returns "None"
# def m1():
#     print("This function is returning nothing.")

# x = m1()
# print(x)

# # write a function to count the number of vowels in a string
# def vowels(user_input):
#     counter = 0
#     vowel = "aeiou"
#     for letter in user_input:
#         if letter in vowel:
#             counter += 1
#     return counter

# word_to_check = vowels(input("Enter a word you want to count its vowels: "))
# print(word_to_check)

# # write a function to search for a word in a string. Return True or False
# def search(statement, word_to_search):
#     if word_to_search in statement:
#         return True
#     else:
#         return False

# execute = search(input("Enter a sentence: "), input("Enter a word to search: "))
# print(execute)

# # write a program which enters a number and prints the factorial of that number. Use a function.
# def factorial(number):
#     factorial = 1
#     for num in range(1, number + 1):
#         factorial = factorial * num
#     return factorial

# num = factorial(int(input("Enter a positive integer: ")))
# print(num)

# # return multiple values from a python function
# def m1(a, b):
#     c = a + b
#     d = a - b
#     return c, d

# x, y = m1(10,5)
# print("Sum of a and b is: ", x)
# print("Difference of a and b is: ", y)

# # function calling another function
# def m1():
#     print("First function information.")
# def m2():
#     print("Second function information.")
#     m1()
# m2()

"""
write a program which enters the start and end numbers. Pass the
numbers to a function "display". The display function should print
factorial of every number.
"""

# def numbers(start, end):
#     return start, end
# def factorial():
#     num1, num2 = numbers(int(input("Enter the start number: ")), int(input("Enter the end number: ")))
#     for number in range(num1, num2 + 1):
#         factorial = 1
#         for num in range(1, number + 1):
#             factorial = factorial * num
#         print(factorial)
# factorial()

# def factorial(num):
#     factorial = 1
#     for number in range(1, num + 1):
#         factorial = factorial * number
#     return factorial
# def display(start, end):
#     for number in range(start, end + 1):
#         print(factorial(number))
# display(int(input("Enter the start number: ")), int(input("Enter the end number: ")))

# # write a program which displays all spy numbers between 1 and 1000
# # spy number ---> sum of digits == product of digits
# def product(num):
#     total = 1
#     for numbers in str(num):
#         total *= int(numbers)
#     return total
# def sum(num):
#     total = 0
#     for numbers in str(num):
#         total += int(numbers)
#     return total
# def spy_number():
#     for numbers in range(1, 1001):
#         if (product(numbers) == sum(numbers)):
#             print(numbers)
# spy_number()

# # Assign a function to a variable
# def add():
#     print("We assigned function to variable")
# sum = add
# sum()

# # pass a function as a parameter to another function
# def display(x):
#     print("This is display function")
# def message():
#     print("This is message function")
# display(message())

# # defining a function inside another function
# def first():
#     print("This is the outer function")
#     def second():
#         print("This is the inner function")
#     second()
# first()

# # the function can return another function
# def first():
#     def second():
#         print("This function is the return type to the outer function")
#     return second
# x = first()
# x()

# # keyword arguments
# def cart(item, price):
#     print(item, "cost is ${}".format(price))
# cart(item = "DB5", price = 1000000)
# cart(price = 152670, item = "Mustang")

# # default arguments
# def cart(item="MTN 2.5GB for 2days", price=1):
#     print(item, "cost is ${}".format(price))
# cart(item = "DB5", price = 1000000)
# cart(price = 152670, item = "Mustang")
# cart()

# # variable length arguments
# def total_cost(x, *y):
#     sum = 0
#     for i in y:
#         sum += i
#     print(x + sum)
# total_cost(100, 200)
# total_cost(110, 226, 311)
# total_cost(11,)

# # keyword variable-length arguments
# def print_kwargs(**kwargs):
#     print(kwargs)
# print_kwargs(id=1, name="Jack", qualification="MBA")

# def m1(**x):
#     for k, v in x.items():
#         print(k, "=", v)
# m1(a=10, b=20, c=30)
# m1(id=100, name="Subbalaxmi")

# # local variables
# def m():
#     a = 1
#     print(a)
# m()

# # global variables
# b = 10
# def n():
#     print(b)
# n()
# a = 10
# b = 12
# def m():
#     a = 1 # local variable overrides global variable
#     print("a from function m(): ", a)
#     print("b from function m(): ", b)
# m()
# a = 10
# b = 12
# def m():
#     global a # every statement would make use of the new variable for a
#     a = 2 # local variable declared after global a is now the global variable
#     print("a from function m(): ", a)
# def n():
#     a = 20
#     print("a from function n(): ", a)
# m()
# n()

# # globals() buitl-in function
# a = 1
# def m():
#     a = 2
#     print(a)
#     print(globals()["a"])
# m()

# # recursive function to print 1 to 5
# def p(n):
#     if n == 6:
#         return
#     else:
#         print(n)
#         p(n +1)
# p(1)

# # recursive function to get the factorial of a number
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

# # recursive function to get the a number raised to a power
# def power(num, n):
#     if n == 0:
#         return 1
#     else:
#         return num*power(num, n-1)
# print(power(2, 3))

# # recursive function to get the product of a string of numbers '1234'
# def product(string):
#     if len(string) == 0:
#         return 1
#     else:
#         return int(string[0]) * product(string[1:])
# print(product("1234"))

# lambda functions (anonymous functions)
# a = lambda

# # Generators --> functions that give a sequence of values as one iterable
# def m():
#     yield 'Mahesh'
#     yield 'Suresh'
# g = m()
# print(g)
# print(type(g))
# for y in g:
#     print(y)

# def m(x, y):
#     while x <= y:
#         yield x
#         x += 1
# g = m(5, 10)
# for y in g:
#     print(y)

# ASSIGNMENT print even numbers instead for the function above
# def m(x, y):
#     while x <= y:
#         yield x
#         x += 1
# g = m(5, 10)
# for y in g:
#     if y % 2 == 0:
#         print(y)

# # aliasing a module
# import addmultiplication as am

# print(am.x)
# print(am.sum(10,20))
# print(am.multiplication(4,5))

# # reload function
# import addmultiplication
# from imp import reload

# reload(addmultiplication)
# reload(addmultiplication)
# reload(addmultiplication)

# # dir() function ---> lists all members of a current module
# x = 10
# y = 20
# def f1():
#     print("Hello")
# print(dir("os"))
# print(__name__)

# # creating a list with elements
# names = ["Mohan", "Prasad", "Ramesh", "Mohan", 10, 20, True, None]
# print(names)

# # creatin a list using list() function
# r = range(0, 10)
# l = list(r)
# print(l)

# # list mutability
# l = [1, 2, 3, 4, 5]
# print(l)
# print("Before modifying l[0]: ", l[0])
# l[0] = 20
# print("After modifying l[0]: ", l[0])
# print(l)

# # accessing lists by using indexing and slicing
# names = ["Prabhas", "Prashanth", "Sarav", 3, 4, 5]
# print(names)
# print(names[2:5:2])
# print(names[4::2])
# print(names[3:5])

# # accessing lists by using loops
# a = [100, 200, 300, 400]
# for x in a:
#     print(x)

# j = 0
# while j < len(a):
#     print(a[j])
#     j = j + 1

# # important functions or methods of lists
# # len() function
# n = [1, 2, 3, 4, 5]
# print(len(n))

# # count() method
# n = [1, 2, 3, 4, 5, 5, 5, 3]
# print(n.count(5))
# print(n.count(3))
# print(n.count(2))

# # append() method ---> adds elements to the end of the list
# l = []
# l.append("Ramesh")
# l.append("Suresh")
# l.append("Naresh")
# print(l)

# # insert() ---> takes two arguments 1. index || 2. element
# """
# 1. if the specified index is greater than the max index, then the element 
# will be inserted at the last position
# 2. if the specified index is smaller than the min index, then the element
# will be inserter at the first position
# """
# n = [10, 20, 30, 40, 50]
# n.insert(0, 76)
# n.insert(-1, 100)
# # n.insert(101) # returns TypeError, you must provide two arguments
# print(n)

# x = [10, 20, 30, 40]
# print(x) # [10, 20, 30, 40]
# x.insert(1, 111)
# print(x) # [10, 111, 20, 30, 40]
# x.insert(-1,222)
# print(x) # [10, 111, 20, 30, 222, 40]
# x.insert(10,333)
# print(x) # [10, 111, 20, 30, 222, 40, 333]
# x.insert(-10, 444)
# print(x) # [444, 10, 111, 20, 30, 222, 40, 333]

# # extend() method ---> items in one list can be added to another
# # 1.
# j1 = [1, 2, 3]
# j2 = ["Rahul", "Rakesh", "Regina"]
# print("Before extend, j1 is:", j1)
# print("Before extend, j2 is:", j2)
# j2.extend(j1)
# print("Afetr extend, j1 is:", j1)
# print("After extend, j2 is:", j2)
# # 2.
# august_txns = [100, 200, 500, 600, 400, 500, 900]
# sept_txns = [111, 222, 333, 600, 790, 100, 200]
# print("August month transactions are:", august_txns)
# print("September transactions are:", sept_txns)
# sept_txns.extend(august_txns)
# print("August and September total transactions amount:", sum(sept_txns))

# # remove() method ---> removes a specific item from a list. returns a ValueError
# # if the item is not present in the list.
# # it removes only the first occurence of that value
# value = [1, 2, 3]
# value.remove(1)
# print(value)

# value1 = [1, 2, 3, 1]
# value1.remove(1)
# print(value1)

# # returns a Value Error
# # value2 = [1, 2, 3, 1]
# # value2.remove(10)
# # print(value2)

# # pop() method
# # 1. takes the index of a value and returns it.
# # 2. if an argument is not passed, the last element of the list is removed.
# # 3. if an index is wrong, an IndexError pops up.

# numbers = [1, 2, 3, 4, 5]
# print(numbers.pop(1))
# print(numbers)
# print(numbers.pop())
# print(numbers)
# # print(numbers.pop(10)) # IndexError

# # reverse() method
# n = [1, 2, 3, 4, 'two']
# print(n)
# n.reverse()
# print(n)

# # sort() method
# nums = [1, 4, 5, 2, 3]
# nums.sort()
# print(nums)

# names = ["Suresh", "Ramesh", "Arjun"]
# names.sort()
# print(names)

# # list aliasing and cloning
# # aliasing
# x = [10, 20, 30]
# y = x
# print(x)
# print(y)
# print(id(x))
# print(id(y))
# x[1] = 99
# print(x)
# print(y)
# print(id(x))
# print(id(y))

# # cloning using slicing
# x = [10, 20, 30]
# y = x[:]
# print(x)
# print(y)
# print(id(x))
# print(id(y))
# x[1] = 99
# print(x)
# print(y)
# print(id(x))
# print(id(y))

# # cloning using copy() method
# x = [10, 20, 30]
# y = x.copy()
# print(x)
# print(y)
# print(id(x))
# print(id(y))

# # mathematical operators (the '+' operator is used for lists to concatenate lists)
# # they must be of the same type
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# # multiplication operator works to repeat elements in the list by said number of times
# a = [1, 2, 3]
# print(a)
# print(2*a)

# # comparison operators
# # for int
# # first, the type of values are checked, 
# # second the elements are counted, 
# # third one-by-one, the elements are checked
# print([1, 2, 3] < [2, 2, 3]) # True
# print([1, 2, 3] < [1, 2, 3]) # False
# print([1, 2, 3] <= [1, 2, 3]) # True
# print([1, 2, 3] < [1, 2, 4]) # True
# print([1, 2, 3] < [0, 2, 3]) # False
# print([1, 2, 3] == [1, 2, 3]) # True

# # for strings
# # case sensitive comparison 
# # +ve LHS is behind RHS
# # -ve LHS is ahead of RHS
# # 0 LHS = RHS
# # capitalized letters come before lowercase letters
# # 1. the number of elements
# # 2. the order of elements
# # 3. the content of elements (case sensitive)
# x = ["abc", "def", "ghi"]
# y = ["abc", "def", "ghi"]
# z = ["ABC", "DEF", "GHI"]
# a = ["abc", "def", "ghi", "jkl"]
# print(x == y) # True
# print(x == z) # False
# print(x == a) # False

# # use of membership operator in lists
# # in and not in
# x = [10, 20, 30, 40, 50]
# print(20 in x) # True
# print(20 not in x) # False
# print(90 in x) # False
# print(90 not in x) # True

# # nested list
# a = [80, 90]
# b = [10, 20, 30, a]
# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])

# nums = [[1, 2, 3, 4], [5, 6, 7, 8]]
# for i in nums:
#     for j in i:
#         print(j, end=" ")

# # lambda functions ---> they take two arguments LHS has what is returned, 
# # RHS is the operation performed
# # it is a single line definition of a function
# #  it is applied in 3 methods which work with a list. (filter, map, reduce)
# # 1.
# x = lambda n : n + 2
# print(x(6))
# # 2.
# y = lambda m, k : m + k
# print(y(2, 3))
# # 3.
# z = lambda a, b, c : a + b - c
# print(z(2, 3, 4))

# # filter() method. It takes a function and a sequence and filters values from a sequence of values
# # it takes a logic as a first argument and the second argument is a list
# item_cost = [999, 888, 1100, 1200, 1300, 777]
# gt_thousand = filter(lambda x : x > 1000, item_cost)
# g = list(gt_thousand) # converted to a list because the default output is just a type 'filter'
# print("Eligible for discount:", g)

# # get all the values divisible by 3 from the item_cost
# item_cost = [999, 888, 1100, 1200, 1300, 777]
# gt_divisible = filter(lambda x : x % 3 == 0, item_cost)
# costs = list(gt_divisible)
# print(costs)

# # get those elements which contain 1 as a digit
# item_cost = [999, 888, 1100, 1200, 1300, 777]
# gt_num = filter(lambda item_cost : '1' in str(item_cost), item_cost)
# nums = list(gt_num)
# print(nums)

# # map() method is used to map a particular function onto the sequence of elements.
# # It returns a new set of values. It takes a function and a sequence
# without_gst_cost = [100, 200, 300, 400]
# with_gst_cost = map(lambda x : x + 10, without_gst_cost)
# x = list(with_gst_cost)
# print("Without GST items costs:", without_gst_cost)
# print("With GST items costs", x)

# # reduce() function adds all the elememts of a list and returns just the sum.
# from functools import reduce
# each_items_cost = [111, 222, 333, 444]
# total_cost = reduce(lambda x, y : x + y, each_items_cost)
# print(total_cost)

# # list comprehension
# # They are a precise way of creating a list using iterable objects like tubles,
# # strings, lists. It is a concise way of creating a list.
# x = [1, 2, 3, 4]
# y = []
# for i in x:
#     y.append(i*2)
# print(y)

# g = [1, 2, 3, 4]
# h = [i * 2 for i in g]
# print(h)

# s = range(1, 20, 3)
# for i in s:
#     print(i)
# m = [x for x in s if x % 2 == 0]
# print(m)

# # write a list comprehension that extracts every element in the list with the letter "k" or "K"
# a = ["Mick", "Jack", "Mohan", "Kelly"]
# b = [i for i in a if "k" in i.lower()]
# print(b)

# # write a list comprehension that uses the reduce function to add each element to itself
# from functools import reduce
# c = [123, 475, 333, 111]
# d = [reduce(lambda x, y: int(x) + int(y), str(i)) for i in c]
# print(d)

# # Tuples
# # Empty tuple
# # Single value tuple
# # Tuple with group of values
# # By using tuple() function
# employee_ids = (1, 2, 3, 4, 5)
# print("same type of objects:", employee_ids)
# print(type(employee_ids))

# employee_ids_2 = 1, 2, 3, 4, 5
# print("same type of objects:", employee_ids_2)
# print(type(employee_ids_2))

# employee_details = (1, "RGV", 1000.123)
# print("different type of objects:", employee_details)

# name = ("Sushanth")
# print(type(name)) # int

# num = (11)
# print(type(num)) # int

# name1 = ("Sushanth",)
# print(type(name1)) # tuple

# num1 = (11,)
# print(type(num1)) # tuple

# emp_id = ()
# print(type(emp_id))

# t = tuple(range(1, 10, 2))
# print(t)

# # we ca access tuples by indexing, slicing, and looping.
# # tuples cannot be modified
# t = (10, 20, 30, 40, 50, 60)
# print(t[0])
# print(t[-1])
# # print(t[100]) # tuple index out of range error

# t = (10, 20, 30, 40, 50, 60)
# print(t[2:5])
# print(t[2:100])
# print(t[::2])

# for i in t:
#     print(i)

# # concatenation of tuples
# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# t3 = t1 + t2
# print(t3)

# t4 = (10, 20, 30)
# t5 = t4*3
# print(t5)

# # important methods and functions of tuples
# # len, count, index, sorted, min, max
# t = (10, 20, 30, 40)
# print(len(t))

# # Q1. Concatenate two lists index-wise
# # Expected output ---> ["My", "name", "is", "Kelly"]
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# # # list3 = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]
# list3 = map(lambda x, y: x + y, list1, list2)
# list4 = list(list3)
# print(list4)

# # Q2. Remove all occurences of a specific item from a list
# # Expected output ---> [5, 15, 25, 50]
# list1 = [5, 20, 15, 20, 25, 50, 20]
# list2 = [i for i in list1 if i != 20]
# print(list2)

# # Q3. Create a string made of the middle three characters
# # Expected output ---> 1. Dip  2. Son
# str1 = "JhonDipPeta"
# str2 = "JaSonAy"
# def mid_string(word):
#     return word[int(len(word)/2)-1:int(len(word)/2)+2]
# print(mid_string(str1))
# print(mid_string(str2))

# # Q4. Write a program to create a recursive function to calculate the sum of numbers from 0 to 10
# # Expected Output ---> 55
# def num_sum(num):
#     if num == 0:
#         return 0
#     else:
#         return num + num_sum(num - 1)
# print(num_sum(10))

# # Q5.Find the largest item from a given list using list comprehension
# # Expected output ---> 24
# x = [4, 6, 8, 24, 12, 2]
# # [filter(lambda x : x > 12, x)]
# y = [i for i in x if i > 12]
# # print(y)

# # important methods and functions of tuples
# # len, count, index, sorted, min, max CONTD
# t = (10, 20, 10, 20)
# print(t.count(10))
# print(t.index(10))
# # print(t.index(30)) # ValueError
# tup = (40, 10, 30, 20)
# tup2 = sorted(tup)
# tup3 = sorted(tup, reverse=True)
# print(tup)
# print(tup2)
# print(tup3)

# # write a program which enters 5 names in a list. Sort the list based on the string length.
# names = []
# for i in range(5):
#     names.append(input("Enter a name: "))
# print(names)
# names.sort(key=len)
# print(names)

# t = (40, 10, 30, 20)
# print(min(t))
# print(max(t))

# # tuple packing and unpacking
# a, b, c, d = 10, 20, 30, 40
# t = a, b, c, d
# print(t)
# tup = (10, 20, 30, 40)
# e, f, g, h = tup
# print("e=", e, "f=", f, "g=", g, "h=", h)

# # tuple comprehenshion ---> it is not suported in python
# t = (x ** 2 for x in range(1,6)) # returns a generator object in 't'. We need to run it using a loop
# print(t)
# for x in t:
#     print(x)

# list objects are mutable and tuple objects are immutable