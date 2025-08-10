class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_val = float('inf')
        max_heap = []
        min_range = float('inf')

        for num in nums:
            new_num = num * 2 if num % 2 else num
            min_val = min(min_val, new_num)
            heapq.heappush(max_heap, -new_num)
        
        
        while max_heap and not max_heap[0] % 2:
            cur_max = -heapq.heappop(max_heap)
            min_val = min(min_val, cur_max // 2)

            heapq.heappush(max_heap, -cur_max // 2)
            min_range = min(min_range, -max_heap[0] - min_val)
        
        return min_range
