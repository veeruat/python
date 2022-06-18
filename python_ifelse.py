#!/bin/python3

import math
import os
import random
import re
import sys


def is_even(n):
    if n / 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input().strip())
    print(is_even(n))
