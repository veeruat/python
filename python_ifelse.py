#!/bin/python3

import math
import os
import random
import re
import sys


def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False


def get_message(n):
    message = ["Weird", "Not Weird"]
    return message[n]


def print_num_cat(n):
    if is_even(n) == False:
        print(get_message(0))
    elif is_even(n) == True and (2 <= n <= 5):
        print(get_message(1))
    elif is_even(n) == True and (6 <= n <= 20):
        print(get_message(0))
    else:
        print(get_message(1))


if __name__ == '__main__':
    n = int(input().strip())

    if 0 < n <= 100:
        print_num_cat(n)
