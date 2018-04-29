def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return all_but_last + digit_double_update(last)

def digit_double_update(n):
    two_digits = 2 * n
    if two_digits < 10:
        return two_digits
    else:
        return sum_digits(two_digits)
