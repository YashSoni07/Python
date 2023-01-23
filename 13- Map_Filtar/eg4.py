# Filter Function
# Even and Odd Number using Lambda Function

number = lambda x: True if x%2==0 else False
even = number(4) # Which are Divisible by 2
print('Even Number')
odd = number(5) # Which are Divisible by 2
print('Odd Number')

# Even and Odd Number using Lambda Function and Filter() with Function
def a1(x):
    return x%2==0
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
result =filter(lambda x:x%2==0, lst)
print(result) # <filter object at 0x0000021B8EE5BEE0>
print(list(result)) #[0, 2, 4, 6, 8, 0, 2]

# Case Study 01
employes =[
    {'FistName': 'Sai', 'LastName':'Kiran', 'Age':27},
    {'FistName': 'Pradeep', 'LastName':'Reddy', 'Age':29},
    {'FistName': 'Praneeth', 'LastName':'Reddy', 'Age':35},
    {'FistName': 'Ranjith', 'LastName':'Yadav', 'Age':30}
]
print(employes)


f = filter(lambda x:x['Age']<30, employes)
print(list(f))

# Case Study 02

from functools import reduce

lst =[12, 14, 16, 4, 18]

# Find the sum of all Numbers

r = reduce(lambda x,y:x+y, lst)
print(r) # 64 why,
# 12 + 14 = 26
# 26 + 16 = 42
# 42 + 4  = 46
# 46 + 18 = 64

# Find the lowest Number
r = reduce(lambda x,y:x if(x<y) else y, lst)
print(r) # 4
