"""Higher-Order Functions with Sequence"""
from operator import mul, add

def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

"""
>>> keep_if(perfect, range(0, 1000))
>>> [1, 6, 28, 496]

Conventional Names:
    common names do not return lists.
    the difinitions above are equivalent to:
        apply_to_all = lambda map_fn, s: list(map(map_fn, s))
        keep_if = lambda filter_fn, s: list(filter_fn, s))
"""
