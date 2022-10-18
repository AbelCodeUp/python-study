#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from module1 import foo
from module2 import foo2


# from ex import PI, get_sum

' a test module '

__author__ = 'Michael Liao'

print(foo())
print(foo2())

# print(PI)
# print(get_sum([1, 2, 3, 4, 5]))

# os.remove('ex.py')
with open('ex.py', 'w') as f:
    f.write("""
PI = 3.14


def get_sum(lst):
    total = 0
    for v in lst:
        total = total + v
    return total
    """)


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


print('__name__', __name__)

if __name__ == '__main__':
    test()
