#!/bin/python3

import math
import os
import random
import re
import sys


def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        print("True")
    elif (year % 100 == 0) and (year % 400 == 0):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    year = int(input().strip())

    if 1900 <= year <= (10 * 10 * 10 * 10 * 10):
        is_leap_year(year)
