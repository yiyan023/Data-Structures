"""
You are given two arrays of integers a and b, which are both sorted in an ascending order and contain unique elements (i.e., no duplicates). You can take several (possibly zero) numbers from the array b and add them to a at any positions in any order. You want the array a to be an arithmetic progression after this. Your task is to find the maximal length of the resulting arithmetic progression represented by array a that can be achieved. If it is impossible to obtain an array forming an arithmetic progression, return -1.

Example:
For a = [0, 4, 8, 16] and b = [0, 2, 6, 12, 14, 20], the output should be solution(a, b) = 6. You can add b[3] = 12 and b[5] = 20 to a and obtain array [0, 4, 8, 12, 16, 20], which is an arithmetic progression of length 6 (the sequence increases by 4 from each element to the next). It is impossible to obtain a longer arithmetic progression, so the answer is 6.
"""

# can use binary search to see if we want to add a certain element, where would we add it?
# create a set of b to check if an element exists inside b without needing to iterate through the array 
# also keep a visited set so that as we are iterating through the b list, if we have already checked that value, we will skip it 

# after that, find the difference between its neighbours 
# if the distance is not equal (or if one of them is 0)
# keep increasing the value until we reach a point until we can't find any more multiples (neighbours)

# find the max length (compare current length to value stored) if the last checked value is not less than the last element in b 

import bisect
import unittest

def solution(a: list, b: list):

    def is_sequence(lst):
        if len(lst) <= 1:
            return True
        
        diff = lst[1] - lst[0]
        return all(lst[i] - lst[i-1] == diff for i in range(1, len(lst)))
    
    res = -1
    b_set = set(b)
    a_set = set(a)
    visited = set()
    
    if is_sequence(a): res = max(res, len(a))
    if not a and is_sequence(b): return len(b)

    for val in b:
        if val in visited:
            continue 
        
        visited.add(val)

        idx = bisect.bisect_left(a, val)
        diff = val - a[idx-1] if idx - 1 >= 0 else a[idx] - val if idx < len(a) else val

        print(val, diff)
        
        if not diff:
            continue
        
        cur = min(val, a[0])
        cur_len = 0

        while cur in a_set or cur in b_set:
            visited.add(cur)
            print(cur)
            cur_len += 1
            cur += diff 

        if cur >= a[-1]: res = max(res, cur_len)
    
    return res

a = [3, 7]
b = [1, 5, 9]
print(solution(a,b))

class TestArithmeticProgression(unittest.TestCase):

    def test_example_case(self):
        print("Test 1")
        a = [0, 4, 8, 16]
        b = [0, 2, 6, 12, 14, 20]
        self.assertEqual(solution(a, b), 6)

    def test_no_b_needed(self):
        a = [3, 6, 9]
        b = [1, 2, 5]
        self.assertEqual(solution(a, b), 3)

    def test_all_b_needed(self):
        a = [2, 10]
        b = [4, 6, 8]
        self.assertEqual(solution(a, b), 5)  # [2, 4, 6, 8, 10]

    def test_ap_impossible(self):
        a = [1, 4, 10]
        b = [2, 3, 5, 6]
        self.assertEqual(solution(a, b), -1)  # Can't form AP that includes all of a

    def test_empty_b(self):
        a = [1, 3, 6]
        b = []
        self.assertEqual(solution(a, b), -1)  # No way to fix the gap between 3 and 6

    def test_empty_a(self):
        a = []
        b = [2, 4, 6, 8]
        self.assertEqual(solution(a, b), 4)  # Any AP is fine since a is empty

    def test_single_element(self):
        a = [5]
        b = [1, 2, 3, 4]
        self.assertEqual(solution(a, b), 2)  # Only 5 is required

    def test_large_ap(self):
        a = list(range(0, 100, 20))  # [0, 20, 40, 60, 80]
        b = [i for i in range(0, 101, 10) if i not in a]
        self.assertEqual(solution(a, b), 11)  # [0,10,20,...,100]

    def test_disjoint_sets(self):
        a = [1, 5, 9]
        b = [2, 3, 6, 7]
        self.assertEqual(solution(a, b), 5)  # [1, 3, 5, 7, 9]

    def test_b_has_useless_elements(self):
        a = [0, 6]
        b = [1, 2, 3, 10]
        self.assertEqual(solution(a, b), 2)  # Can't form AP from 0 to 6 with valid spacing
    
    def test_1(self):
        a = [3, 7]
        b = [1, 5, 9]
        self.assertEqual(solution(a, b), 5)
    
    def test_2(self):
        a = [0]
        b = [2, 4, 6]
        self.assertEqual(solution(a, b), 4)

if __name__ == '__main__':
    unittest.main()
    print("start")
