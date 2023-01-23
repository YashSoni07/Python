import re

# Is used to find the fist latter
pattern = r'Y'
string = 'Yash'
r = re.findall(pattern, string)
print(r)

# Is used to find the small latter
pattern = r'[a-z]+'
string = 'YASH--yash--SONI--soni'
r = re.findall(pattern, string)
print(r)

# Is used to find the small latter
pattern = r'[A-Z]+'
string = 'YASH--yash--SONI--soni'
r = re.findall(pattern, string)
print(r)

# Is used to find the missing latter
pattern = r'Y..h'
string = 'Yash'
r = re.findall(pattern, string)
print(r)

# Is used to change latter or word
pattern = r'love'
string = 'i love car and i also love bikes'
replace = 'like'
r = re.sub(pattern, replace, string)
print(r)

# To find the Capital Element
pattern = r'\S'
string = 'YASH'
r = re.findall(pattern, string)
print(r)

# To find the small Element
pattern = r'\s'
string = 'yash'
r = re.findall(pattern, string)
print(r)

# To find the
pattern = r'[a-xA-Z0-9]+@[a-zA-z]*\.(com|in|net)'
string = 'yashsoni@gmail.com'

if re.search(pattern, string):
    print('Valid')
else:
    print('InFiled')