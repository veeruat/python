#!/bin/python3
import math
import sys


def is_float(T):
    print(T % 1)


if __name__ == '__main__':
    sentinel = 'x'
    result = '\n'.join(iter(input, sentinel))
    print(result)

