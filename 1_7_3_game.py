"""OK, It's a Funny Game! Just joking!"""
def alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        bob(n-1)

def bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        alice(n-2)
    else:
        alice(n-1)

def is_even(n):
    if n == 0:
        return True
    else:
        if (n-1) == 0:
            return False
        else:
            return is_even((n-1)-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        if (n-1) == 0:
            return True
        else:
            return is_odd((n-1)-1)
        
