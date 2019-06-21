#!/usr/bin/env python

a = int(input('Enter number A: '))
b = int(input('Enter number B: '))

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

gcd = a + b
print(gcd)
