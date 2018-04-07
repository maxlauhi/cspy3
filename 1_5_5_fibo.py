"""compute Nth Fibonacci number,for n >= 2.
    >>> fibo(8)
    13
"""

def fibo(n):
    pred, curr = 0, 1 # Fibonacci number 1th and 2th
    k = 2             # No more less
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr
