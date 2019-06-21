#!/usr/bin/env python

count = int(input('Enter range: '))

numbers = []
for i in range(count):
    number = int(input('Enter number: '))
    numbers.append(int(number))


simple = []
for num in range(2, 10001):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        simple.append(int(num))
        string = ''.join(map(str, simple))

for n in numbers:
    print(string[n - 1:n])
