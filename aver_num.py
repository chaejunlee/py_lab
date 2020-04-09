#!/usr/bin/python
import sys

if __name__=='__main__':
    n = int(input('Number of inputs: '))
    a = 0
    for i in range(n):
        a += int(input());
    avr = a / n
    print(avr)