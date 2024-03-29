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

# # how to create a dictionary
# d = {1: "Ramesh", 2: "Arjun", 3: "Nireekshan"}
# print(d)

# dj = {}
# dj[1] = "Gigamesh"
# dj[2] = "Timothy"
# dj[3] = "Yorkshire"
# print(dj)

# # accessing dictionaries
# d = {1: "Ramesh", 2: "Arjun", 3: "Nireekshan"}
# print(d[1])
# print(d[2])
# print(d[3])
# print(d[10]) # KeyError

# # how to handle KeyError
# d = {1: "Ramesh", 2: "Arjun", 3: "Nireekshan"}
# if 400 in d:
#     print(d[400])
# else:
#     print("key not found")

# # working with dictionary
# d = {}
# n = int(input("Enter number of employees: "))
# i = 1
# while i <= n:
#     name = input("Enter Employee Name: ")
#     salary = input("Enter Employee Salary: ")
#     d[name] = salary
#     i = i + 1
# for x in d:
#     print("The name is:", x, "and the salary is:", d[x])
# print(d)

# # updating a dictionay
# # dictionary[key] = value
# # if the key is not available, it is added to the end of the dictionary
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print("Old dictionary:", d)
# d[10] = "Hari"
# print("Added key-value(10: Hari) pair to dictionary:", d)

# # if the key is existing, the value is replaced
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print("Old dictionary:", d)
# d[3] = "Hari"
# print("Updated value of key 3 pair to dictionary:", d)

# # removing or deleting elements from the dictionary
# # 1. with the del keyword or del() function
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print("Before deleting key from dictionary:", d)
# del d[1]
# print("After deleting key from dictionary:", d)

# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print("Before deleting key from dictionary:", d)
# del(d[1])
# print("After deleting key from dictionary:", d)

# # 2. using the clear() method
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print("Before deleting key from dictionary:", d)
# d.clear()
# print("After deleting key from dictionary:", d)

# # delete total dictionary object
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print("Before deleting key from dictionary:", d)
# del d
# # print("After deleting key from dictionary:", d) # NameError

# # functions and methods of dictionary
# # dict() function,
# d = dict()
# print(d)
# print(type(d))

# # dict({key1: value1, key2: value2}) function,
# d = dict({1: "Ramesh", 2: "Arjun", 3: "Mahesh"})
# print(d)

# # dict([tuple1, tuple2]) function,
# d = dict([(1, "Ramesh"), (2, "Arjun"), (3, "Mahesh")])
# print(d)

# # len() function ---> talks about the number of key-value pairs
# d = dict([(1, "Ramesh"), (2, "Arjun"), (3, "Mahesh")])
# print("length of dictionary:", len(d))

# # get() method ---> returns the value of the specified key
# # it doesn't give any error if the key is not present
# # 1. if the key is present, it returns the value
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print(d.get(1))
# print(d.get(100))
# # 2. if the key is not present, it returns None or the specified default value
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print(d.get(1))
# print(d.get(100, "No key Found"))

# # pop() method can be used to remove the key-value pair from the dictionary and displays it
# # if the specified key is not available, you get a KeyError dic.pop(key)
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print("Before pop:", d)
# d.pop(1)
# print("After pop:", d)
# # print(d.pop(100)) # KeyError
# print(d.pop(100, "No key found")) # No key found
# d.pop()
# # print(d) # TypeError

# # popitem() method returns both the and the value
# # if the dictionary is empty, we get a KeyError
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print("Before popitem:", d)
# d.popitem()
# print("After popitem:", d)

# d = {}
# d.popitem()
# # print(d) # KeyError

# # keys() method extracts all the keys in form of a list.
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print(d)
# for k in d.keys():
#     print(k)

# # values() method extracts all the values in form of a list.
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# print(d)
# for v in d.values():
#     print(v)
# d = {
#     1: ["A", 300, "green"],
#     2: ["B", 400, "blue"],
#     3: ["C", 500, "red"]
# }
# for x, y in d.items():
#     for i in y:
#         print(i, end=" ")

# # items() method gives a key-value pair in the form of tuples
# d = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# for k, v in d.items():
#     print(k, "---", v)

# # copy() method can create an exact cloned copy of the dictionary
# d1 = {1: "Ramesh", 2: "Arjun", 3: "Mahesh"}
# d2 = d1.copy()
# print(d1)
# print(d2)
# print(id(d1))
# print(id(d2))

# # dictionary comprehension
# squares = {a:a*a for a in range(1,6)}
# print(squares)

# l = ["John", "Samuel", "Eke", "Oluwatobi"]
# d = {names[0].upper():names for names in l}
# print(d)

# # write a program which has a list of trainees. The name should be the full name of the person.
# # create a dictionary where the initial is the key and the name is the value
# trainees = ["Naomi Mary Willie", "Ebenezer Samuel Ajayi", "Chiamaka Shileakanwa Ukwuoma"]
# def initial_extractor(names):
#     name = names.split(" ")
#     initial = ""
#     for n in name:
#         initial += n[0].upper()
#     return initial
# d = {initial_extractor(trainee):trainee for trainee in trainees}
# print(d)

# # write a program which enters a string and using dictionary comprehension store the string as the key
# # and the count as the value

# user_input = int(input("Enter number of words: "))
# n = 1
# d = {}
# while n <= user_input:
#     word = input("Enter a word: ")
#     d[word] = len(word)
#     n = n + 1
# print(d)

# write a program to count the repeated characters in the string "thequickbrowfoxjumpsoverthelazydog"
# and store them in a dictionary
# word = "thequickbrownfoxjumpsoverthelazydog"
# d = {}
# letter_to_count = input("Enter the letters you want to count separated by space: ")
# letter = letter_to_count.split(" ")
# for l in letter:
#     d[l] = word.count(l)
# print(d)

# # Class Activity
# # 1. Write a python program to calculate the length of a string
# def string_length(str):
#     count = 0
#     for char in str:
#         count += 1
#     return count
# s = input("Enter a string: ")
# print(string_length(s))

# # 2. Write a python program to count the number of characters (character frequency) in a string.
# # sample string: google.com
# # expected result: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# def char_frequency(str):
#     dict = {}
#     for n in str:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# s = input("Enter a string: ")
# print(char_frequency(s))

# # 3. Write a python program to get a string made of the first 2 and the last 2 chars from a given string.
# # if the string length is less than 2, retrn the empty string instead.
# # Sample string: 'w3resource'
# # expected result: 'w3ce
# # sample string: "w3"
# # expected output: "w3w3"
# # sample string: "w"
# # expected output: ""
# def first_and_las_two(word):
#     if len(word) < 2:
#         return 'this returns an empty string.'
#     return word[0:2] + word[-2:]
# s = input("Enter a string: ")
# print(first_and_las_two(s))

# # Write a python program to get a string from a given string where all occurences of its first char
# # have been changed to '$', except the first char itself
# # sample string: "restart"
# # expected result: 'resta$t'
# def char_change(word):
#     char1 = word[0]
#     swapped = ""
#     for char in word[1:]:
#         if char == char1:
#             swapped += "$"
#         else:
#             swapped += char
#     return char1 + swapped

# s = input("Enter a string: ")
# print(char_change(s))

# # write a python program to get a single string from two given strings, separated by a space and swap
# # the first two characters of each string
# # sample string: "abc", "xyz"
# # expected result: "xyc abz"
# def swap_strings(str1, str2):
#     return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

# s, t = input("Enter a string 1: "), input("Enter a string 2: ")
# print(swap_strings(s, t))

# # Sets ---> used to store unique elements.
# # insertion order is not preserved. they are stored with hashing.
# # indexing and slicing is not allowed.
# # sets can store the same and different types of elements or objects.
# # set objects are mutable because we can add elements to it.
# # set elements are imutable.
# # sets operates both on value and type
# # set() function is a conversion function to convert from list or tuple to set
# # set can be used to store a relation that can be used to compare other sets
# # they are required mainly in some statistical operations

# # creating sets
# s = {10, 20, 30, 40, 40}
# print(s)
# print(type(s))

# # set with different elements
# s1 = {10, '20', 'Rahul', 234.56, True}
# print(s1)
# print(type(s1))

# # creating a set using range function
# s3 = set(range(5))
# s2 = set([1,"1",1.0,2,2,2,3,3,3])
# print(s2)

# # to create an empty set, you need to use the set() function
# s = set()
# print(s)
# print(type(s))

# # Important methods of sets
# # add(x) method to add elements in a set
# s = {10, 20, 30}
# s.add(40)
# print(s)

# # update(x, y) to add multiple elements to a set. Arguments are not individual elements
# # but iterable like range, list, etc.
# s = {10, 20, 30}
# l = [40, 50, 60, 10]
# s.update(l)
# print(s)

# s = {10, 20, 30}
# l = [40, 50, 60, 10]
# s.update(l, range(5))
# print(s)

# # copy() method
# s = {10, 20, 30}
# s1 = s.copy()
# print(s1)

# # pop() method removes and returns some randoom element from the set
# s = {40, 10, 30, 20}
# print(s)
# print(s.pop())
# print(s)

# # remove(x) method removes specific elements from the set. KeyError is returned
# # if the element is not in the set.
# s = {40, 10, 30, 20}
# s.remove(30)
# print(s)

# # s = {40, 10, 30, 20}
# # s.remove(50)
# # print(s) # KeyError

# discard(x) removes the specified element from the set but no error will be returned
# s = {40, 10, 30, 20}
# s.discard(30)
# print(s)

# # s = {40, 10, 30, 20}
# # s.discard(50)
# # print(s)

# # clear() method removes all elements from the set
# s = {10, 20, 30}
# print(s)
# s.clear()
# print(s)
# # del s
# # print(s) # NameError

# # union() or a|b returns all elements present in both sets
# x = {10, 20, 30, 40}
# y = {30, 40, 50, 60}
# print(x.union(y))
# print(x|y)

# # intersection() or a&b returns common elements in both
# x = {10, 20, 30, 40}
# y = {30, 40, 50, 60}
# print(x.intersection(y))
# print(x&y)

# x = {10, 20, 30, 40, "bit-wise"}
# y = {30, 40, 50, 60, "bit-wise"}
# print(x.intersection(y))
# print(x&y)

# bitwise operation
# a = 10
# b = 12
# c = a&b
# d = a|b
# print(c) # 8
# print(d) # 14

# # difference() or a-b method returns elements present in x and not in y
# x = {10, 20, 30, 40}
# y = {30, 40, 50, 60}
# print(x.difference(y))
# print(x-y)
# print(y-x)

# # symmetric_difference() or a^b returns elements present in either x or y but not in both.
# x = {10, 20, 30, 40}
# y = {30, 40, 50, 60}
# print(x.symmetric_difference(y))
# print(x^y)

# # set comprehension
# s = {x * x for x in range(5)}
# print(s)

# # removing duplicate elements from a list in python
# l = [10, 20, 30, 10, 20, 40]
# s = set(l)
# print(s)

# # frozen set -----> is an immutable set.
# # all sets are not meant to be frozen sets.
# vowels = ('a', 'e', 'i', 'o', 'u')
# f_set = frozenset(vowels)
# print(f_set)
# print(type(f_set))
# u_set = set(f_set) # convert frozen set back to a normal set
# print(u_set)
# print(type(u_set))
# n_list = list(u_set) # convert set back to list
# print(n_list)
# print(type(n_list))

# # Error Handling with try and except
# try:
#     print(10/0)
# except ZeroDivisionError as z:
#     print("Exception information:", z)

# try:
#     x = int(input("Enter First Number: "))
#     y = int(input("Enter Second Number: "))
#     print(x / y)
# except ZeroDivisionError:
#     print("Can't Divide with Zero")
# except ValueError:
#     print("Please provide integer value only.")

# try:
#     x = int(input("Enter First Number: "))
#     y = int(input("Enter Second Number: "))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e:
#     print("Please Provide valid numbers only and problem is:", e)

# try:
#     x = int(input("Enter First Number: "))
#     y = int(input("Enter Second Number: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("ZeroDivisionError: Can't divide with zero")
# except:
#     print("Default Except: Please provide valid input only.")

# # finally block executes always
# try:
#     print("try block")
# # except only executes if there's an exception in the try block
# except:
#     print("except block")
# finally:
#     print("finally block")

# try:
#     print('try block')
#     print(10/0)
# except ZeroDivisionError:
#     print("except block")
# finally:
#     print('finally block')

# try:
#     print('try block')
#     print(10/0)
# except NameError: # this is handled by the Python Virtual Machine.
#     print("except block")
# finally:
#     print('finally block')

# # nested try-except-finally blocks
# try:
#     print("outer try block")  # prints
#     print(10/0)
#     try:
#         print("Inner try block")
#     except ZeroDivisionError:
#         print("Inner except block")
#     finally:
#         print("Inner finally block")
# except:
#     print("Outer Except block") # prints
# finally:
#     print("outer finally block") # prints

# try:
#     print("outer try block") # prints
#     try:
#         print("Inner try block") # prints
#         print(10/0)
#     except ZeroDivisionError:
#         print("Inner except block")  # prints
#     finally:
#         print("Inner finally block") # prints
# except:
#     print("Outer Except block")
# finally:
#     print("outer finally block") # prints

# try:
#     print("outer try block") # prints
#     try:
#         print("Inner try block") # prints
#         print(10/0)
#     except NameError:
#         print("Inner except block")
#     finally:
#         print("Inner finally block") # prints
# except:
#     print("Outer Except block") # prints
# finally:
#     print("outer finally block") # prints

# # else block
# try:
#     print("try block")
# except:
#     print("except: Handling code")
# else:
#     print("else block")
# finally:
#     print("finally block")

# try:
#     print("try block")
#     print(10/0)
# except:
#     print("except: Handling code")
# else:
#     print("else block")
# finally:
#     print("finally block")

# # custom exceptions
# try:
#     x = int(input("Eneter a positive integer: "))
#     if x < 0:
#         raise ValueError(x)
# except ValueError as e:
#     print(f"You have provided {e}. Please run the program again and enter a positive integer.")

# # file handling
# # syntax
# # f = open(filename, mode)
# # f.close()
# f = open('demo.txt', 'w')
# print("File Name:", f.name)
# print("File Mode:", f.mode)
# print("Is File Readable:", f.readable())
# print("Is File Writable:", f.writable())
# print("Is File CLosed:", f.closed)
# f.close()
# print("Is File CLosed:", f.closed)

# # writing data to a file
# f = open('demo.txt', 'w')
# f.write("Welcome to python programming.\n")
# f.write("I hope you're having a good time.\n")
# print("Data written successfully to file.")
# f.close()

# # writelines(argument) method
# f = open("demo.txt", "w")
# lists = ["Ramesh\n", "Arjun\n", "Senthni\n", "Vignesh"]
# f.writelines(lists)
# print("Execute Successfully!")
# f.close()

# # reading data from a file
# f = open("poem.txt", "w")
# f.write("Hello everyone!!\nThis Topic is very important\nPlease don't sleep\nOnce this topic is done\nThen happily you can go to sleep\nThanks for cooperating.")
# print("Executed Successfully!")
# f.close

# # read() outputs every data in the file
# f = open("poem.txt", "r")
# data = f.read()
# print(data)
# f.close()

# # read(n) outputs n number of characters
# f = open("poem.txt", "r")
# data = f.read(20)
# print(data)
# f.close()

# # readline() reads one line in the file
# f = open("poem.txt", "r")
# line1 = f.readline()
# print(line1, end='')
# line2 = f.readline()
# print(line2, end='')
# line3 = f.readline()
# print(line3, end='')
# f.close()

# # readlines() reads every line in the file and prints on a newline
# f = open("poem.txt", "r")
# lines = f.readlines()
# for line in lines:
#     print(line, end='')
# f.close()

# # with keyword for opening and closing a file automatically
# with open("text.txt", "w") as f:
#     f.write("Welcome\n")
#     f.write("to\n")
#     f.write("Python\n")
#     print("Is File Closed:", f.closed)
# print("Is File Closed:", f.closed)

# # seek and tell methods
# # tell displays the current position of the cursor or pointer
# # in the file
# # seek moves the cursor or pointer to a desired position
# with open("demo.txt", "r") as f:
#     print(f.tell()) # position 0
#     print(f.read(2))
#     print(f.tell()) # position 2
#     print(f.read(3))
#     print(f.tell()) # position 5
# print("Is file closed?", f.closed)

# # seek has two arguments seek(offset, fromwhere)
# # offset ---> is where you want to get to from start
# data = "Python language is excellent\n"
# f = open("abc.txt", "w")
# f.write(data)
# with open("abc.txt", "r+") as f:
#     text = f.read()
#     print(text) # Python language is excellent
#     print("The current cursor position:", f.tell()) # 30
#     f.seek(30)
#     print("The current cursor position:", f.tell()) # 30
#     f.write("Britania Biscuit")
#     f.seek(0) # start from begining of line
#     text = f.read()
#     print("Data after modification:")
#     print(text) # Python language is excellent\nBritania Biscuit
# print("Is file closed?", f.closed) # True

# # checking for the existence of a file
# import os, sys
# fname = input("Enter a file name: ")
# if os.path.isfile(fname):
#     print("File exists:", fname)
#     f = open(fname, "r")
# else:
#     print("File does not exist:", fname)
#     sys.exit(0)
# print("The content of the file is:")
# data = f.read()
# print(data)

# # working with CSV files
# import csv
# with open("emp.csv", "w", newline='') as f:
#     w = csv.writer(f)
#     w.writerow(["EMP NO", "EMP ANME", "EMP SAL", "EMP ADDR"])
#     n = int(input("Enter Number of employees:"))
#     for i in range(n):
#         eno = input("Enter Employee No:")
#         ename = input("Enter Employee Name:")
#         esal = input("Enter Employee Salary:")
#         eaddr = input("Enter Employee Address:")
#         w.writerow([eno, ename, esal, eaddr])
# print("Total Employee data written to CSV file successfully.")
