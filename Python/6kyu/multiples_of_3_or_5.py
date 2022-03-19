"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)
"""

"""
Todos los multiplos de 3 o 5 debajo de n. 

si n = 10

3 = 3x1 
6 = 3x2
9 = 3x3 
5 = 5x1 

La suma de estos es 23. 

Si el numero es negativo, regreso 0

"""

def solution(n):
    lis = []
    if n < 0:
        return 0
    else:
        for i in range(1,n):
            cin = i * 5
            tre = i * 3
            if cin < n:
                lis.append(cin)
            if tre < n:
                lis.append(tre)
        return sum(set(lis))
            
def solution_pythonic_way(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)   

print(solution(10))
print(solution_pythonic_way(10))