"""
Given an integer n and an array a of length n, your task is to apply the following mutation to a:

Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be solution(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the resulting array after the mutation will be [4, 5, -1, 2, 1].
"""

# 0 => 0 + 1 = 4
# 1 => 0 + 1 + 2 = 4 + 0 + 1 = 5
# 2 => 1 + 2 + 3 = 1 - 2 + 

# seems like a sliding window 

def solution(n: int, a: list):
    # set up for 0
    b = [0] * len(a)

    for r in range(len(a)):
        left = a[r-1] if r - 1 >= 0 else 0 
        right = a[r+1] if r + 1 < len(a) else 0 

        b[r] = a[r] + left + right
    
    return b


def test_solution():
    test_cases = [
        # Basic example from prompt
        {
            "input": (5, [4, 0, 1, -2, 3]),
            "expected": [4, 5, -1, 2, 1]
        },
        # Single element
        {
            "input": (1, [7]),
            "expected": [7]
        },
        # Two elements
        {
            "input": (2, [1, 2]),
            "expected": [3, 3]
        },
        # All zeros
        {
            "input": (4, [0, 0, 0, 0]),
            "expected": [0, 0, 0, 0]
        },
        # All negative
        {
            "input": (3, [-1, -2, -3]),
            "expected": [-3, -6, -5]
        },
        # Increasing values
        {
            "input": (6, [1, 2, 3, 4, 5, 6]),
            "expected": [3, 6, 9, 12, 15, 11]
        },
        # Decreasing values
        {
            "input": (4, [10, 7, 4, 1]),
            "expected": [17, 21, 12, 5]
        },
        # Large numbers
        {
            "input": (3, [10**6, 10**6, 10**6]),
            "expected": [2_000_000, 3_000_000, 2_000_000]
        }
    ]

    for i, case in enumerate(test_cases):
        n, a = case["input"]
        result = solution(n, a)
        assert result == case["expected"], f"Test case {i+1} failed: expected {case['expected']}, got {result}"
        print(f"Test case {i+1} passed.")

# Example usage of test runner:
def solution(n: int, a: list) -> list:
    b = []
    for i in range(n):
        left = a[i - 1] if i - 1 >= 0 else 0
        mid = a[i]
        right = a[i + 1] if i + 1 < n else 0
        b.append(left + mid + right)
    return b

# Run tests
test_solution()
