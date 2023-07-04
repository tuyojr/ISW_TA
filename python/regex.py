import re

# compile() function returns a regex object if the pattern is valid
# re.compile(pattern)
# finditer() method returns an iterator containing all the match objects
# re.finditer(pattern, string)

# # working with modules compile() and finditer()
# # first create the pattern object and compile it
# count = 0
# pattern = re.compile('ab')
# # next, create a matcher to find the pattern in the string\\s 
# matcher = pattern.finditer('abaababa')
# for match in matcher:
#     count += 1
#       # start() --> returns the start index
#       # end() --> returns the end + 1 index
#       # group() --> returns the matched pattern
#     print(match.start(), "...", match.end(), "...", match.group())
# print("The number of occurrences:", count)

# # method 2
# count = 0

# # create the matcher in one line with finditer()
# matcher = re.finditer('ab', 'abaababa')

# for match in matcher:
#     count += 1
#     print(match.start(), "...", match.end(), "...", match.group())
# print("The number of occurrences:", count)

# # character classes
# # [abc] --> either a or b or c
# # [^abc] --> except a and b and c
# # [a-z] --> any lower case alphabet symbol
# # [A-Z] --> any upper case alphabet symbol
# # [a-zA-Z] --> any alphabet symbol
# # [0-9] --> any digit from 0 to 9
# # [^a-zA-Z0-9] --> any special symbol
# # [0-9a-zA-Z] --> any alphanumeric character

# #  1.
# matcher = re.finditer('[abc]', 'a7b@k9z')
# for match in matcher:
#     print("One", match.start(), "...", match.end(), "...", match.group())

# #  2.
# matcher2 = re.finditer('[a-z]', 'a7b@k9z')
# for match2 in matcher2:
#     print("Two", match2.start(), "...", match2.end(), "...", match2.group())

# # 3.
# matcher3 = re.finditer('[a-zA-Z0-9]', 'a7b@k9z')
# for match3 in matcher3:
#     print("Three", match3.start(), "...", match3.end(), "...", match3.group())

# # 4.
# matcher4 = re.finditer('[^a-zA-Z0-9]', 'a7b@k9z')
# for match4 in matcher4:
#     print("Four", match4.start(), "...", match4.end(), "...", match4.group())

# # 5.
# matcher5 = re.finditer('[^abc]', 'a7b@k9z')
# for match5 in matcher5:
#     print("Five", match5.start(), "...", match5.end(), "...", match5.group())

# # 6.
# matcher6 = re.finditer('[0-9]', 'a7b@k9z')
# for match6 in matcher6:
#     print("Six", match6.start(), "...", match6.end(), "...", match6.group())

# # pre-defined character classes
# # \s --> space character
# # \S --> except space character
# # \d --> any digit from 0 to 9
# # \D --> except digit
# # \w --> any word character
# # \W --> except word character

# #  1.
# matcher = re.finditer('\s', 'a7b@k9z') # matches space character
# for match in matcher:
#     print("One", match.start(), "...", match.end(), "...", match.group()) # no space, returns nothing

# #  2.
# matcher2 = re.finditer('\S', 'a7b@k9z') # matches except space character
# for match2 in matcher2:
#     print("Two", match2.start(), "...", match2.end(), "...", match2.group()) # returns all characters except space

# # 3.
# matcher3 = re.finditer('\w', 'a7b@k9z') # matches any word character
# for match3 in matcher3:
#     print("Three", match3.start(), "...", match3.end(), "...", match3.group()) # returns all word characters a-z 0-9

# # 4.
# matcher4 = re.finditer('\W', 'a7b@k9z') # matches except word character
# for match4 in matcher4:
#     print("Four", match4.start(), "...", match4.end(), "...", match4.group()) # returns all characters except word characters (@)

# # 5.
# matcher5 = re.finditer('\d', 'a7b@k9z') # matches any digit
# for match5 in matcher5:
#     print("Five", match5.start(), "...", match5.end(), "...", match5.group()) # returns all digits 0-9

# # 6.
# matcher6 = re.finditer('\D', 'a7b@k9z') # matches except digit
# for match6 in matcher6:
#     print("Six", match6.start(), "...", match6.end(), "...", match6.group()) # returns all characters except digits (a b @ k z)

# #  quantifiers
# # a --> exactly one 'a'
# # a+ --> at least one 'a'
# # a* --> any number of 'a' including zero number of 'a'
# # a? --> at most one 'a' i.e. either one 'a' or zero number of 'a'
# # a{m} --> exactly m number of 'a'
# # a{m, n} --> minimum m and maximum n number of 'a'

# #  1.
# matcher = re.finditer('a', 'abaabaab') # matches exactly one 'a'
# for match in matcher:
#     print("One", match.start(), "...", match.end(), "...", match.group())

# #  2.
# matcher2 = re.finditer('a+', 'abaabaab') # matches at least one 'a'
# for match2 in matcher2:
#     print("Two", match2.start(), "...", match2.end(), "...", match2.group())

# # 3.
# matcher3 = re.finditer('a?', 'abaabaab') # matches at most one 'a' i.e either one 'a' or zero number of 'a'
# for match3 in matcher3:
#     print("Three", match3.start(), "...", match3.end(), "...", match3.group())

# # 4.
# matcher4 = re.finditer('a{3}', 'abaabaab') # matches exactly 3 number of 'a'
# for match4 in matcher4:
#     print("Four", match4.start(), "...", match4.end(), "...", match4.group()) # returns all characters except word characters (@)

# # 5.
# matcher5 = re.finditer('a{2,4}', 'abaabaab') # matches minimum 2 and maximum 4 number of 'a'
# for match5 in matcher5:
#     print("Five", match5.start(), "...", match5.end(), "...", match5.group())

# # 6.
# matcher6 = re.finditer('a*', 'abaabaab') # matches any number of 'a' including zero number of 'a'
# for match6 in matcher6:
#     print("Six", match6.start(), "...", match6.end(), "...", match6.group())

# regex methods.
# # match() --> checks for a match only at the beginning of the string

# s = input("Enter pattern to check: ")
# m = re.match(s, "abcabdefg")
# if m != None:
#     print("Match is available at the beginning of the string")
#     print("Start Index:", m.start(),"and End Index:", m.end())
# else:
#     print("Match is not available at the beginning of the string")
    
# # fullmatch() --> checks for a match only if the whole string matches
# s = input("Enter pattern to check: ")
# m = re.fullmatch(s, "abab")
# if m != None:
#     print("Full string matched")
# else:
#     print("Full string not matched")

# # search() --> checks for a match anywhere in the string
# s = input("Enter pattern to check: ")
# m = re.search(s, "abaaaaba")
# if m != None:
#     print("Match is available")
#     print("First occurence of match with start index:", m.start(), "and end index:", m.end())
# else:
#     print("Match is not available")

# # findall() --> returns a list containing all matches
# l = re.findall("[0-9]", "a7b9c5kz")
# print(l)

# # sub() --> replaces one or many matches with a string
# s = re.sub("[a-z]", "#", "a7b9c5k8z")
# print(s)

# # subn() --> replaces one or many matches with a string and returns the number of replacements
# sn = re.subn("[a-z]", "#", "a7b9c5k8z")
# print(sn)
# print("The result string:", sn[0])
# print("The number of replacements:", sn[1])

# # split() --> returns a list where the string has been split at each match
# sp = re.split(',', "KGF,BB1,BB2")
# print(sp)
# for s in sp:
#     print(s)

# write a program to extract all mobile numbers present in the input file where numbers are mixed with normal text
# with open('input.txt', "r") as f1, open('output.txt', "w") as f2:
#     for line in f1:
#         items = re.findall("[7-9]\d{9}", line)
#         for n in items:
#             f2.write(n + "\n")
#     print("Extracted all mobile numbers into output.txt")

# with open('input.txt', 'r') as f1:
#     with open('output.txt', 'w') as f2:
#         for line in f1:
#             items = re.findall('[7-9]\d{9}', line)
#             for n in items:
#                 f2.write(n + "\n")
#     print("Extracted all mobile numbers into output.txt")

# # write a program to check whether the given mail is valid id or not.
# s = input("Enter a Mail id: ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# if m != None:
#     print("Valid Mail id")
# else:
#     print("Invalid Mail id") 

# finditer() --> returns an iterator containing all matches
# compile() --> returns a regex object if the pattern is valid