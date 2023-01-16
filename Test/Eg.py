# Q1

# a = input("Insert vale a: ")
# b = input("Insert vale b: ")
# sum = int(a)+int(b)
# print(sum)

# With Function
# a = input("Input A Value: ")
# b = input("Input B Value: ")
# def a1():
 # sum = int(a)+ int(b)
  # print(sum)
# a1()

# Q2
# rupees = input("Enter Rupees :")
# def Rupees():
#     paise = int(rupees)*100
#     print('Paise :', paise)
#
# Rupees()

# Q3
# principle = input("Inter Principle: ")
# time = input("Inter Time: ")
# rate = input("Inter Rate: ")
# sum = int(principle) * int(time) * int(rate) / 100
# print("Simple Interest", sum)

# priciple = input("Inter Principle :")
# time = input("Inter Time : ")
# rate = input("Enter Time : ")

# def SimpleInteret():
    # sum = int(priciple)* int(time)* int(rate)/ 100
    # print(sum)

# SimpleInteret()

# Q4
# fahrenheit = input("Temperature in Fahrenheit :")
#  #degree = input("Temperature in Degree")
# def temperature():
#     degree = int(fahrenheit)-32 * 5 / 9
#     print("Drgree = ",degree)
#
# temperature()

#Q5

# def A1():
#     number = int(input("Enter the value :"))
#     print(number)
#     if number > 10 and number < 24:
#         print('Yes Its There..')
#     else:
#         print('Sorry Its Not there')
# A1()

# Q6
# def number():
#     no_1 = int(input("Inter 1st Number :"))
#     no_2 = int(input("Inter 2nd Number :"))
#     no_3 = int(input("Inter 3nd Number :"))
#     print(no_1, no_2, no_3)
#     if no_1 > no_2 and no_1 > no_3:
#         print("1st Number is Greatest")
#     elif no_2 > no_1 and no_2 > no_3:
#         print("2nd Number is Greatest")
#     else:
#         print("3nd Number is Greatest")
# number()

# Q7
# def factorial():
#      num = int(input("Enter Any Number :"))
#      f = 1
#
#      if num < 0:
#          print("not possible")
#      elif num == 0:
#          print("nothing")
#      else:
#          for i in range(1, num + 1):
#              f = f * i
#          print("the factorial of:", num,"is", f)
#
# factorial()

# Q8
# def table():
#     num = int(input("Enter any Number :))
#     for i in range(1,13):
#           print( num *i)
#
# table()

# Q9
# a = int(input('Enter the no :'))
#
#
# def a1(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return a1(n - 1) + a1(n - 2)
#
#
# for i in range(a):
#     print(a1(i))
