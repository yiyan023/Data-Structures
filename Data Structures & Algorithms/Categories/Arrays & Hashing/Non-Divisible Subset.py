#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    modulo_k = collections.defaultdict(int)
    res = 0
    
    for num in s:
        modulo_k[num % k] += 1
    
    for n in range(k // 2 + 1):
        if n != k - n and n > 0:
            res += max(modulo_k[n], modulo_k[k-n])
        
        elif modulo_k[n]:
            res += 1
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
