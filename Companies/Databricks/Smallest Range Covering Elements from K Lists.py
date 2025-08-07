class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        res = [float('inf'), float('-inf')]

        for i, arr in enumerate(nums):
            heapq.heappush(min_heap, (arr[0], i, 0))
            res[0] = min(res[0], arr[0])
            res[1] = max(res[1], arr[0])

        max_val = res[1]

        while min_heap:
            value, arr, idx = heapq.heappop(min_heap)

            if idx + 1 >= len(nums[arr]): # wont have all k
                break

            heapq.heappush(min_heap, (nums[arr][idx + 1], arr, idx + 1))
            max_val = max(max_val, nums[arr][idx + 1])

            if res[1] - res[0] > max_val - min_heap[0][0]:
                res = [min_heap[0][0], max_val]
                
        return res
