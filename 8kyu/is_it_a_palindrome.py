"""
Write a function that checks if a given string (case insensitive) is a palindrome.
"""

a = 'Abba'

def is_palindrome(s):
    return s[::-1].lower() == s.lower()



print(is_palindrome(a))