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