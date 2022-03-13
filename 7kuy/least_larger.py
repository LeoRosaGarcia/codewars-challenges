"""
Task
Given an array of numbers and an index, return the index of the least number larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

Notes
Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.

Example
least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
"""

def least_larger(a, i):
    try:
        return a.index(min(x for x in a if x > a[i]))
    except ValueError:
        return -1


print(least_larger([4, 1, 3, 5, 6], 0 ))