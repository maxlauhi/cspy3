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
        return digit_double_update(all_but_last) + last

def digit_double_update(n):
    all_but_last, last = split(n)
    sum_even = sum_digits(2 * last)
    if n < 10:
        return sum_even
    else:
        return luhn(all_but_last) + sum_even
