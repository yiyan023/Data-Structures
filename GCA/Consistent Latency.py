"""
In a network monitoring system, maintaining consistent latency is crucial for ensuring optimal performance. Given an array of integers latencies where each element represents recorded latencies in milliseconds, and a positive integer threshold, your task is to determine the maximum length of a contiguous subarray such that the difference between the maximum and minimum latencies within this subarray does not exceed threshold.

Return the length of the longest such contiguous subarray.
"""

# [9, 4, 1, 6, 8]

# min: 1
# max: 0 1 2

# 2

from collections import deque

def solution(latencies: list, threshold: int):
    min_queue = deque()
    max_queue = deque()
    max_len = 0

    for i, latency in enumerate(latencies):
        while min_queue and latencies[min_queue[-1]] > latency:
            min_queue.pop()

        while max_queue and latencies[max_queue[-1]] < latency:
            max_queue.pop()
        
        min_queue.append(i)
        max_queue.append(i)

        while min_queue and max_queue and latencies[max_queue[0]] - latencies[min_queue[0]] > threshold:
            if max_queue[0] < min_queue[0]: max_queue.popleft()
            else: min_queue.popleft()


        max_len = max(max_len, abs(max(min_queue[-1], max_queue[-1]) - min(min_queue[0], max_queue[0])) + 1)
    
    return max_len

test_cases = [
    # Basic cases
    ([1, 4, 9, 6, 8], 4, 3),
    ([1], 10, 1),
    ([5, 5, 5, 5, 5], 0, 5),
    ([1, 3, 6, 7, 9, 3, 3, 3, 3], 0, 4),
    
    # Edge cases
    ([1, 2, 3, 4, 5], 0, 1),
    ([1, 10, 1, 10, 1], 9, 5),
    ([5, 6, 7, 8, 9], 4, 5),

    # Performance and corner cases
    ([100, 105, 102, 99, 101, 110, 98, 97, 120], 10, 4),
    ([10] * 100000, 0, 100000),
    ([1, 100, 1, 100] * 25000, 0, 1),

    ([1, 100, 1, 100, 1, 100], 0, 1),
    ([1, 2, 3, 100, 4, 5], 3, 3)
]

# Run Test Cases
for idx, (latencies, threshold, expected) in enumerate(test_cases, 1):
    result = solution(latencies, threshold)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    print(f"Test Case {idx}: {status} | Expected: {expected}, Got: {result}")

