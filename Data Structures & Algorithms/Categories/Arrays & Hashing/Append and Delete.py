#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    
    # first, we must replace the existing characters between s and t that are not equal 
    
    # equal to length of smaller string from first discrepancy to the end times 2
    # if their lengths are not the same, then we add the difference between their lengths to the result 
    
    # filler operations 
    # add then delete (or vice versa) -> remaining actions (k - res) needs to be even 
    
    if len(s) + len(t) <= k:
        return "Yes"
    
    res = abs(len(s) - len(t))
    overlap = min(len(s), len(t))
    
    for i in range(overlap):
        if s[i] != t[i]:
            res += (overlap - i) * 2
            break
    
    return "Yes" if res <= k and not (k - res) % 2 else "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())
    

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
