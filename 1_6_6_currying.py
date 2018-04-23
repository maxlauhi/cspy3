"""
这样就能很容易的把多参数函数map到单参数函数上，论文和证明写起来会容易很多
"""
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
"""
>>> from operator import add
>>> curry2 = lambda g: lambda h: lambda f: g(h, f)
>>> m = curry2(add)
>>> m(3)(4)
7
"""
