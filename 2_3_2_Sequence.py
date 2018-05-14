def count(s, value):
    """Count the number of occurrences of value in sequence s.
    """
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total

"""
structure of FOR statment:
    for <name> in <expression>:
        <suite>
    * <expression> must yield an iterable value.
    * Bind <name> to that value in the current frame.
    * Excute the <suite> statment each loop. 
"""
