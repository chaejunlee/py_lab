#!/usr/bin/python
import sys

if __name__ == '__main__':
    n = int(input('fibonacci number? '))
    f1 = f2 = 1
    for i in range(n):
        if (i == 0):
            print('1', end='')
        elif (i == 1):
            print(',1', end='')
        else:
            f3 = f1 + f2
            f2 = f1
            f1 = f3
            print(','+str(f3), end="")
    print('\nF'+str(n)+' = '+str(f3))
