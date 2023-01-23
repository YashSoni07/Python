employes= [
    {'FistName':'Yash', 'LastName':'Soni', 'age': 22},
    {'FistName':'Shashwat', 'LastName':'Jain', 'age': 25},
    {'FistName':'Harsh', 'LastName':'Soni', 'age': 28},
    {'FistName':'Rohit', 'LastName':'Kumar', 'age': 21}
]
print(employes[0]['FistName']+ employes[0]['LastName'])
print(employes[1]['FistName']+ employes[1]['LastName'])
print(employes[2]['FistName']+ employes[2]['LastName'])
print(employes[3]['FistName']+ employes[3]['LastName'])

a= map(lambda a:a['FistName']+ a['LastName'],employes)
print(a)
print(list(a)) # ['YashSoni', 'ShashwatJain', 'HarshSoni', 'RohitKumar']
