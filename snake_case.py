import re

name = 'Decipher this!'
name = re.sub(r' ', '_', name).lower()+ ".py"
print(name) 