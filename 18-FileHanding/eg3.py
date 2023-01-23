f = open('tow.txt', 'w')
# l= [10, 20, 30, 40]# TypeError: write() argument must be str, not int
l = ['10', '20']
l = str([10, 20, 30, 40])

f.writelines(l)
print('Data Inserted')
f.close()
