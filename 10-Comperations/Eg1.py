# what is comprehension you can compare the code and wright in one line
# By using comprehensions. We can generate new list from the existing list.

# Types of comprehension :-
# list comprehension
# Set comprehension
# Dict comprehension
# Generator comprehension


# Find the Range using list Construction
l1 = list(range(1, 10))
print(l1)

# Find the Square Root using the list  Construction
for i in list(range(1, 10)):
    print(i ** 2)

# Find the Square Root using list Construction and Compensations
# Syntax [expression(i**2) for item(i) in iterable()list(range(1,10)]

l1 = [i ** 2 for i in list(range(1, 10))]
print(l1)

# Find the Square root and Even numbers
# Syntax [Expression(i**2) for item(i) in iterable(list(range(1,10))) if conditions(i%2==0) ]
a = [i ** 2 for i in list(range(1, 10)) if i % 2 == 0]
print(a)

# Find the Square root and Odd numbers
a = [i ** 2 for i in list(range(1, 10)) if i % 3 == 0]
print(a)