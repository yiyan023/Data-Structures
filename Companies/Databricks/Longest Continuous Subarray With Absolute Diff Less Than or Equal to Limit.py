class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        res = 0
        l = 0

        for i, num in enumerate(nums):
            while min_queue and nums[min_queue[-1]] > num:
                min_queue.pop()
            
            while max_queue and nums[max_queue[-1]] < num:
                max_queue.pop()
            
            min_queue.append(i)
            max_queue.append(i)

            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                popped = max_queue.popleft() if max_queue[0] < min_queue[0] else min_queue.popleft()

                if popped >= l:
                    l = popped + 1
                    
            
            res = max(res, i - l + 1)
        
        return res
