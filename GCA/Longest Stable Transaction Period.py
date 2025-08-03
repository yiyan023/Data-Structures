"""
In a financial monitoring system, you are responsible for detecting stable periods in transaction records.

You are given:

An array of non-negative integers transactions, where each element represents the net transaction value for a day.

A positive integer k, called the stability factor. 
"""

from itertools import accumulate

def solution(arr: list, k: int):
    prefix_sum = list(accumulate(arr))
    prefix_mod = [num % k for num in prefix_sum]
    first_idx = {0:-1}
    max_len = 0

    for i, mod in enumerate(prefix_mod):
        if mod not in first_idx:
            first_idx[mod] = i
    
    for i, mod in enumerate(prefix_mod):
        max_len = max(max_len, i - first_idx[mod])
    
    return max_len 

def run_tests(solution):
    tests = [
        {
            "transactions": [2, 3, 1, 4, 1, 5, 9],
            "k": 3,
            "expected": 4  # [3,1,4,1] sum = 9
        },
        {
            "transactions": [3],
            "k": 2,
            "expected": 0
        },
        {
            "transactions": [1, 2, 3, 4, 5, 6],
            "k": 5,
            "expected": 5  # [1,2,3,4,5] = 15
        },
        {
            "transactions": [5, 10, 15],
            "k": 5,
            "expected": 3  # All divisible by 5
        },
        {
            "transactions": [1, 2, 3, 1],
            "k": 7,
            "expected": 4  # No subarray divisible by 7
        },
        {
            "transactions": [0, 0, 0, 0],
            "k": 1,
            "expected": 4  # Sum of any subarray is 0 → divisible by any k
        },
        {
            "transactions": [7, 2, 3, 4, 1],
            "k": 5,
            "expected": 4  # [2,3,4,1] = 10
        },
        {
            "transactions": [1] * 100000,
            "k": 1000,
            "expected": 100000  # First 1000 ones → sum = 1000
        },
        {
            "transactions": [1, 2, 3, 4, 6, 7],
            "k": 6,
            "expected": 3  # [3,4,6,7] = 20
        }
    ]

    for i, test in enumerate(tests):
        result = solution(test["transactions"], test["k"])
        assert result == test["expected"], f"Test {i+1} failed: expected {test['expected']}, got {result}"
        print(f"Test {i+1} passed.")

# Example usage:
run_tests(solution)

