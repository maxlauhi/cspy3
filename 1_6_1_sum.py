"""Functions as Arguments to sum of compound operations"""

"""computes square of Nth natural number"""
def square(k):
    return k * k

"""computes cube of Nth natural number"""
def cube(k):
    return k * k * k

""""""
def formula(k):
    return 8 / ((4*k-3) * (4*k-1))

"""function of calculate the sum of N numbers in a loops,
   the Number is a function that may be a number from
   squares number, Cubic number or other formulas number. 
"""
def sum(n, term):
    k, total = 1, 0
    while k <= n:
        total, k = total + term(k), k + 1
    return total

"""calculate the sum of the square of  N natural numbers by
   defined functions.
"""
def sum_square(n):
    return sum(n, square)

"""calculate the sum of cubic numbers
"""
def sum_cube(n):
    return sum(n, cube)

"""calculate the sum of formula numbers
"""
def sum_formula(n):
    return sum(n, formula)

