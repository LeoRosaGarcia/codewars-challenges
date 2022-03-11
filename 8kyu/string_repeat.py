"""
Write a function called repeatStr which repeats the given string string exactly n times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
"""

a = 2
b = "I"

def repeat_str(repeat, string):
    return string * repeat


print(repeat_str(a, b))