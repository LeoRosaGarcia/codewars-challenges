import re

def extract_numbers(text):
    regex = "[0-9]+"
    return re.findall(regex, str(text))

string = 'Boston Celtics 112 Philadelphia 76ers 95'
string = string.replace("76ers","") 
numbers = extract_numbers(string)
print(numbers)