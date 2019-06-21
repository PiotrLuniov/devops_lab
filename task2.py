#!/usr/bin/env python

import math
sumMain = 0
sumSecond = 0
lens = int(input('Enter range: '))
arr = []
for i in range(lens):
    arr.append(list(map(int, input('Enter matrix string: ').split())))
print(arr)
for i in range(lens):
    sumMain += arr[i][i]
    sumSecond += arr[i][lens - i - 1]
print(math.fabs(sumMain-sumSecond))
