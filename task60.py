#!/usr/bin/env python
def del_func(a, b):
    global gcd
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

        gcd = a + b
    return gcd


if __name__ == "__main__":
    a = int(input('Enter number A: '))
    b = int(input('Enter number B: '))
    print(del_func(a, b))
