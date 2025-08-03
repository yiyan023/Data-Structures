# what happens when you add a house?
# you are either connecting "islands" or creating a solo 

# when you add a block, check its neighbours 
# if the neighbours exists (aka it has already been built), find the length of the neighbour, sum them + 1 and compare with the max length. 
# the max length will be equal to the max length of the previous query to the length of this addition 

# approach:
# each block will be associated to an island name or identifier 
#   when islands merge, this will be updated 
# each island name is associated with a 

def solution(houses: list):
    intervals = []
    res = [0] * len(houses)
    
    def insert_interval(val: int):
        l, r = 0, len(intervals) - 1

        while l <= r:
            mid = (l + r ) // 2

            if intervals[mid][0] - 1 <= val <= intervals[mid][1] + 1:
                intervals[mid][0] = min(intervals[mid][0], val)
                intervals[mid][1] = max(intervals[mid][1], val)

                if mid - 1 >= 0 and intervals[mid-1][1] == intervals[mid][0] - 1:
                    intervals[mid][0] = intervals[mid-1][0]
                    intervals.pop(mid - 1)
                    
                if mid + 1 < len(intervals) and intervals[mid+1][0] == intervals[mid][1] + 1:
                    intervals[mid][1] = intervals[mid+1][1]
                    intervals.pop(mid + 1)
                
                return intervals[mid][1] - intervals[mid][0] + 1
            
            elif val < intervals[mid][0]:
                r = mid - 1
            
            else:
                l = mid + 1
    
        intervals.insert(l, [val, val])
        return 1

    for i, house in enumerate(houses):
        length = insert_interval(house)
        print(intervals)
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
        assert result == test["expected"], f"Test {i+1} failed: expected {test['expected']}, got {result}"
        print(f"Test {i+1} passed.")

# Example usage:
run_tests(solution)

