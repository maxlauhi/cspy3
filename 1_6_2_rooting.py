def square_root(a):
    x = 1
    while x * x != a:
        print(x)
        print(a)
        x = square_root_update(x, a)
    return x

def square_root_update(x, a):
    return ((x + a/x))/2
