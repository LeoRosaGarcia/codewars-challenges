"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

"""

a = [1, 2, 2]

def square_sum(numbers):
    return sum(i**2 for i in numbers)

print(square_sum(a))