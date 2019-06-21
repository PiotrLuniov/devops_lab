#!/usr/bin/env python
marksheet = []
for _ in range(0, int(input('Enter range: '))):
    marksheet.append([input('Enter name: '), float(input('Enter mark: '))])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
