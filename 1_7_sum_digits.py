"""Write a function that sums the digits of a natural number"""

def sum_digits(n):
    """Return the sum of the digits of positive integer n.
    >>> sum_digits(118)
    10
    """
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

