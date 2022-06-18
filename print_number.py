#!/bin/python3
import math


def print_num(n):

    for i in range(1, n + 1):
        print(i, end=""),


if __name__ == '__main__':
    n = int(input().strip())

    if 0 < n <= 150:
        print_num(n)
