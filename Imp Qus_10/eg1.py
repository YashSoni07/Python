# # Introduction :-

# # Q1 Python Program to Print Hello world!

# print("Hello World!")
#
# # Q2 Python Program to Add Two Numbers

# a = 5
# b = 10
# print(a + b)
#
# # Q3 Python Program to Find the Square Root

# n = float(input("Enter any number :"))
#
#
# def a1():
#     a = n ** 0.5
#     print(a)
#
#
# a1()
#
# # Q4 Python Program to Calculate the Area of a Triangle

# base = int(input("Enter Base :"))
# height = int(input("Enter Height :"))
#
# area = 1 / 2 * base * height
# print(area)
#
# def Area_Triangle():
#     area = 1 / 2 * base * height
#     print(area)
#
#
# Area_Triangle()


# # Q5 Python Program to Solve Quadratic Equation

# # Q6 Python program to swap two variables

# a = 10
# b = 20

# c = a
# a = b
# b = c
# print(a, b)

# OR

# a, b = b, a
# print(a, b)

# # Q7 Python Program to Generate a Random Number

# import random
#
# x = random.randint(1, 10)
# print(x)

# # Q8 Python Program to Convert Kilometers to Miles

# # kilometer = input("Enter Kilometers :"))
# # miles = float(0.62137119)
# kilometer = float(input("Enter Kilometers :"))
#
#
# def convert():
#     # miles = float(kilometer)*0.62137119
#     miles = kilometer * 0.62137119
#     print(miles)
#
#
# convert()
#
# # Q9 Python Program to Convert Celsius To Fahrenheit

# celsius = int(input("Enter Celsius :"))
#
#
# def convert():
#     f = celsius * 9 / 5 + 32
#     print("Celsius is ", f)
#
#
# convert()

# # Q10 Python Program to Print Output Without a Newline

# print("Hello", end=" ")
# print("Python")

# #------------------#

# Object Oriented :-

# Q1 Program to Get the Class Name of an Instance

# class Product:
#
#     def productDitles(self, name):
#         self.name = name
#         print("Product name is", self.name)
#
#
# p = Product()
# # p.productDitles("Apple 14s")
# print(p.__class__.__name__)

# Q2 Program to Differentiate Between type() and isinstance()

# class Parent:
#     def parent(self):
#         print("Hello")
#
#
# class Child(Parent):
#     def child(self):
#         print('Hy')
#
#
# a = Parent()
# b = Child()
#
# print(type(a) == Parent)
# print(type(b) == Parent)
#
# print(isinstance(b, Child))
# print(isinstance(b, Parent))

# #---------------# #

# # Decision Making and Loops :-

# #  Q1 Program to Check if a Number is Positive, Negative or 0

# num = int(input("Enter Any Number :"))
# if num >= 0:
#     print("Its A Positive Number..!")
# elif num <= 1:
#     print("Its A Nagative Number..!")
# else:
#     print("Enter Any Number..!")

# # Q2 Program to Check if a Number is Odd or Even

# num = int(input("Enter Any Number :"))
# if (num % 2) == 0:
#     print(num,"Number is Even...")
# else:
#     print(num,"Number is Odd...")

# # Q3 Program to Check Leap Year

# year = int(input("Enter Any Year :"))
# if year % 4 == 00:
#     print("Its A Leap Year")
# else:
#     print("Its Not A leap Year")

# Q4 Program to Find the Largest Among Three Numbers

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))
#
# if (number1 >= number2) and (number1 >= number3):
#    largest = number1
# elif (number2 >= number1) and (number2 >= number3):
#    largest = number2
# else:
#    largest = number3
#
# print("The largest number is", largest)

# Q5 Program to Check Prime Number

# # taking input from user
# number = int(input("Enter any number: "))
#
# # prime number is always greater than 1
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")
#
# # if the entered number is less than or equal to 1
# # then it is not prime number
# else:
#     print(number, "is not a prime number")

# Q8 Program to Display the multiplication Table

# num = int(input("Enter A Number :"))
#
# for i in range(1, 11):
#     print(num, "*", i, "=", i * num)

# Q15 Program to Reverse a Number

# num = "1234"
# print(num[::-1])
# print(str(num)[::-1])

# -------------------------------------------------------------------#
# Functions
# Q1 Program to Display Powers of 2 Using Anonymous Function


# Q2 Program to Find Numbers Divisible by Another Number

# num = int(input("Enter the number whose divisibility needs to be checked: "))
# div = int(input("Enter the number with which divisibility needs to be checked:"))
# if num % div == 0:
#     print("the number is Divisible")
# else:
#     print("The Number Is not Divisible")

# my_list = eval(input("Enter a list of numbers :"))
# number = int(input("Enter Any Number :"))
#
# # result = list(filter(lambda x: (x % number == 0), my_list))
# def divisible():
#
#
# print("Numbers divisible by", number, "are", result)

# Q3 Program to convert decimal into other number systems

# num = int(input("Enter A Number :"))
#
# print(bin(num), "in binary.")
# print(oct(num), "in octal.")
# print(hex(num), "in hexadecimal.")

# Q4 Program to find the ASCII value of the given character

# ASCII = American Standard Code for Information Interchange.

# l = input("Enter Any Character :")
# print("The ASCII value of '" + l + "' is", ord(l))

# Q5 Function to find HCF the Using Euclidian algorithm

# def hcf(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# hcf = hcf(20, 40)
# print("The HCF is", hcf)

# Q6

# Q7 Program to find the factors of a number

# def print_number(x):
#     for i in range(1, x + 1):
#         if x % i == 0:
#             print(i)
#
#
# num = int(input("Enter the factors of a number :"))
# print_number(num)

# Q8
# This function adds two numbers
# def add(x, y):
#     return x + y
#
#
# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y
#
#
# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y
#
#
# # This function divides two numbers
# def divide(x, y):
#     return x / y
#
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# while True:
#     # take input from the user
#     choice = input("Enter choice(1/2/3/4): ")
#
#     # check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue
#
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#             break
#     else:
#         print("Invalid Input")

# -----------------------------------#

# Native Datatypes

# Q14  Program to Check If a List is Empty

# l = []
# if not l:
#     print("the list is empty")
# else:
#     print("Its Not Empty")

# Q15 Program to Concatenate Two Lists

# l1 = ["Yash Soni"]
# l2 = ["Shashwat Jain"]
# print(l1+l2)

# Q16 Program to Check if a Key is Already Present in a Dictionary
# d = {1: "Yash", 2: "Shashwat", 3: 33}
# if 33 in d:
#     print("YES its Present")
# else:
#     print("NO Its Not Present")

# Q18  Program to Parse a String to a Float or Int

# a = "007"
# b = int(a)
# c = float(a)
#
# print(a)
# print(type(b))
#
# print(a)
# print(type(c))

# Q23 Program to Randomly Select an Element From the List

# l =["yash", 'Soni', 'Shashwat', 'Jain']
# print(l[-1])

# Q25 Program to Count the Occurrence of an Item in a List
# l = ["Yash", 'Soni', "Yash", 'Shashwat', "Yash", 'Jain']
# print(l.count("Yash"))

# Q26 Program to Delete an Element From a Dictionary

# d = {1: "Yash", 2: "Soni"}
# d.pop(2)
# print(d)

# Q29 Program to Trim Whitespace From a String

# print("hello \nHello")

# Q36 Program to Remove Duplicate Element From a List

# l = [10, 20, 10, 30, 10, 40, 10]
# print(list(set(l)))
