def average(x, y):
    return (x + y) / 2

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

def sqrt(a):
    print(a)
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        print(x)
        # true or flase from func(approx_eq)
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)
