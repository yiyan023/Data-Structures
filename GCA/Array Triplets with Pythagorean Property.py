"""
Given an integer array of length n, return a result array of length n-2, where result[i] = 1 if:

array[i]^2 + array[i+1]^2 = array[i+2]^2,
array[i+1]^2 + array[i+2]^2 = array[i]^2, and
array[i]^2 + array[i+2]^2 = array[i+1]^2.
Otherwise, result[i] = 0.
"""

def solution(arr: list):
    res = [0] * (len(arr) - 2)

    for i in range(len(res)):
        i_sqr = arr[i] ** 2
        i_one_sqr = arr[i+1] ** 2
        i_two_sqr = arr[i+2] ** 2

        cond1 = i_sqr + i_one_sqr == i_two_sqr 
        cond2 = i_sqr + i_two_sqr == i_one_sqr
        cond3 = i_one_sqr + i_two_sqr == i_sqrt

        if cond1 and cond2 and cond3:
            res[i] = 1
    
    return res

def test_pythagorean_conditions():
    test_cases = [
        {
            "input": [0, 0, 0],
            "expected": [1]
        },
        {
            "input": [3, 4, 5],  # 3² + 4² = 5² → true, but other two are false
            "expected": [0]
        },
        {
            "input": [0, 0, 0, 3, 4, 5],
            "expected": [1, 0, 0, 0]
        },
        {
            "input": [5, 12, 13, 0, 0, 0],
            "expected": [0, 0, 0, 1]
        },
        {
            "input": [1, 1, 1],
            "expected": [0]
        },
        {
            "input": [-3, -4, -5],  # Same as 3,4,5 since squares are same
            "expected": [0]
        },
        {
            "input": [0, 0, 0, 0],
            "expected": [1, 1]
        },
        {
            "input": [9, 40, 41],
            "expected": [0]
        },
        {
            "input": [0],
            "expected": []
        },
        {
            "input": [0, 0],
            "expected": []
        },
        {
            "input": [],
            "expected": []
        }
    ]

    for i, case in enumerate(test_cases):
        result = check_pythagorean(case["input"])
        assert result == case["expected"], f"Test case {i+1} failed: expected {case['expected']}, got {result}"
        print(f"Test case {i+1} passed.")


def check_pythagorean(arr):
    n = len(arr)
    res = []
    for i in range(n - 2):
        a, b, c = arr[i], arr[i + 1], arr[i + 2]
        a2, b2, c2 = a*a, b*b, c*c
        if a2 + b2 == c2 and b2 + c2 == a2 and a2 + c2 == b2:
            res.append(1)
        else:
            res.append(0)
    return res


# Run the tests
test_pythagorean_conditions()
