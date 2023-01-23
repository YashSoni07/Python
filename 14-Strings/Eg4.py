# Join Method
name = ['Yash', 'Harsh', 'Shashewat', 'Nandini']
print(name)  # ['Yash', 'Harsh', 'Shashewat', 'Nandini']

print(','.join(name))  # Yash,Harsh,Shashewat,Nandini

print('-'.join(name))

print(':'.join(name))

# If you use join in List

# l1 = [1, 2, 3, 4, 5]
# print('/'.join(l1)) #TypeError: sequence item 0: expected str instance, int found

l1 = ['1', '2', '3', '4', '5']
print(','.join(l1))  # 1,2,3,4,5
