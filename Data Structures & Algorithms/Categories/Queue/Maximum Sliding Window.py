class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        l = 0
        
        for r in range(len(nums)):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)

            if queue[0] < l:
                queue.popleft()
            
            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1
                
        
        return res
