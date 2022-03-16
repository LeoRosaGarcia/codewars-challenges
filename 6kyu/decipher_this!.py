"""
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
"""

import re

result = []
fin = []
def decipher_this(string):
    list = re.split('(\d+)',string)
    for i in list:
        if i.isnumeric():
            result.append(chr(int(i)))
        else:
            result.append(i)
    result2 = ''.join(result)
    list2 = result2.split()
    for x in list2:
        if len(x) > 2:
            fin.append((x[0] + x[-1] + x[2:-1] + x[1]))
        else:
            fin.append(x)
    return ' '.join(fin)

print(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"))