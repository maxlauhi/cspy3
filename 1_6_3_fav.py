"""Function as value"""

def make_adder(n):
    """Return a function that takes on argument
    K and return K + N.

    >>> add_three = make_adder(3)
    >>> add_x =add_three(4)
    >>> add_x(3)
    10
    """
    def adder(k):
        def adder2(x):
            return k + n + x
        return adder2
    return adder
