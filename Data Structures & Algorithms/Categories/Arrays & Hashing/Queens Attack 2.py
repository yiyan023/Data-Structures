#!/bin/python3

import math
import os
import random
import re
import sys
import collections 
import heapq

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    
    # the obstacles block off the path for the queen 
    # what we want to check for -> same row (left-side and right-side)
    # same column -> (up and down)
    # diagonal -> abs(x1 - x2) == abs(y1 - y2)
    
    # use a heap for each case where we sort by minimum distance from the queen then check for each category at the end 
    
    # if that category is empty, then we go all the way until the end (doing the proper math)
    
    # otherwise, then we take the number of places from the queens current position and the obstacle (their distance - 1)
    
    # use a hashmap or defaultdict where the value is equal to an array (will treat it as a heap)
    # keys - rr (row, right), rl (row, left), cr (column, right), cl (column, left), dru (diagonal, right-up), drd (diagonal, right-down), dlu (diagonal, left-up), dld (diagonal, left-down)
    
    obstacle_sort = collections.defaultdict(list)
    res = 0
    
    for r, c in obstacles: 
        x = "l" if c < c_q else "r" 
        y = "d" if r < r_q else "u"
            
        if r == r_q:
            heapq.heappush(obstacle_sort[f"r{x}"], abs(c - c_q))
        
        elif c == c_q:
            heapq.heappush(obstacle_sort[f"c{y}"], abs(r - r_q))
        
        elif abs(c - c_q) == abs(r - r_q):
            heapq.heappush(obstacle_sort[f"d{x}{y}"], abs(r - r_q))
            
    # rows
    res += (obstacle_sort["rr"][0]- 1) if len(obstacle_sort["rr"]) else n - c_q
    res += (obstacle_sort["rl"][0] - 1) if len(obstacle_sort["rl"]) else c_q - 1
    
    # columns
    res += (obstacle_sort["cu"][0] - 1) if len(obstacle_sort["cu"]) else n - r_q
    res += (obstacle_sort["cd"][0] - 1) if len(obstacle_sort["cd"]) else r_q - 1
    
    # diagonals 
    res += (obstacle_sort["dru"][0] - 1) if len(obstacle_sort["dru"]) else n - max(c_q, r_q)
    res += (obstacle_sort["drd"][0] - 1) if len(obstacle_sort["drd"]) else min(n - c_q, r_q - 1)
    res += (obstacle_sort["dld"][0] - 1) if len(obstacle_sort["dld"]) else min(r_q, c_q) - 1
    res += (obstacle_sort["dlu"][0] - 1) if len(obstacle_sort["dlu"]) else min(n - r_q, c_q - 1)
    
    return res
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
