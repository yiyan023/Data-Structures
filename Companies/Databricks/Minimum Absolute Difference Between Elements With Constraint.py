from sortedcontainers import SortedList 

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sorted_list = SortedList()
        min_diff = float('inf')
        l = 0

        for i, num in enumerate(nums):
            if i >= x:
                sorted_list.add(nums[l])
                l += 1
            
            idx = sorted_list.bisect(num)
            left = sorted_list[idx - 1] if idx >= 1 else float('-inf')
            right = sorted_list[idx] if idx < len(sorted_list) else float('inf')
            min_diff = min(min_diff, right - num, num - left)
                
        
        return min_diff


            
