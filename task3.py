#!/usr/bin/env python

t = list(map(int, input().split()))

simple = []
for num in range(2, 10001):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        simple.append(int(num))
        string = ''.join(map(str, simple))

for n in t:
    print(string[n - 1:n])
