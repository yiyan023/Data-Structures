import bisect

def solution(houses: list):
    intervals = []
    res = [0] * len(houses)
    
    def insert_interval(val: int):
        idx = bisect.bisect_left(intervals, [val, val])
        intervals.insert(idx, [val, val])

        if idx + 1 < len(intervals) and intervals[idx+1][0] - 1 == intervals[idx][1]:
            intervals[idx][1] = max(intervals[idx][1], intervals[idx+1][1])
            intervals.pop(idx+1)

        if idx - 1 >= 0 and intervals[idx-1][1] + 1 == intervals[idx][0]:
            intervals[idx][0] = min(intervals[idx][0], intervals[idx-1][0])
            intervals.pop(idx-1)
            return intervals[idx-1][1] - intervals[idx-1][0] + 1
        
        return intervals[idx][1] - intervals[idx][0] + 1

    for i, house in enumerate(houses):
        length = insert_interval(house)
        res[i] = length if i - 1 < 0 else max(length, res[i - 1])
    
    return res


def run_tests(solution):
    tests = [
        # 🔹 Basic example (growing contiguous)
        {
            "queries": [2, 1, 3],
            "expected": [1, 2, 3]
        },
        # 🔹 Merge in middle
        {
            "queries": [1, 3, 2],
            "expected": [1, 1, 3]
        },
        # 🔹 Two separate segments merged later
        {
            "queries": [10, 8, 9],
            "expected": [1, 1, 3]
        },
        # 🔹 Increasing but skipping around
        {
            "queries": [4, 6, 5, 10, 7],
            "expected": [1, 1, 3, 3, 4]
        },
        # 🔹 Left expansion
        {
            "queries": [5, 4, 3, 2, 1],
            "expected": [1, 2, 3, 4, 5]
        },
        # 🔹 Right expansion
        {
            "queries": [1, 2, 3, 4, 5],
            "expected": [1, 2, 3, 4, 5]
        },
        # 🔹 Bridges two isolated points
        {
            "queries": [100, 102, 101],
            "expected": [1, 1, 3]
        },
        # 🔹 Non-consecutive, no merging
        {
            "queries": [1, 3, 5, 7],
            "expected": [1, 1, 1, 1]
        },
        # 🔹 Merge two long chains
        {
            "queries": [1, 2, 3, 10, 9, 8, 4, 5, 6, 7],
            "expected": [1, 2, 3, 3, 3, 3, 4, 5, 6, 10]
        },
        # 🔹 Single house
        {
            "queries": [50],
            "expected": [1]
        }
    ]

    for i, test in enumerate(tests):
        result = solution(test["queries"])
        assert(result == test["expected"])
    
    print("Ok.")

# Example usage:
run_tests(solution)

