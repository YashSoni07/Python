# Group Dictionary Methode

import re
string = 'yashsoni@gmail.com'
pattern = r'(?P<username>\w+)@(?P<mail>\w+)\.(?P<extension>\w+)'
j = re.match(pattern,string)
print(j)
print(j.groupdict())
