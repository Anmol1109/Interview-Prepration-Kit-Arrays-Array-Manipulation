#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for i in queries:
        start, end, amt = i
        arr[start - 1] += amt
        arr[end] -= amt
    mv = -1
    running = 0
    for i in arr:
        running += i
        if running > mv:
            mv = running
            
    return mv

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
