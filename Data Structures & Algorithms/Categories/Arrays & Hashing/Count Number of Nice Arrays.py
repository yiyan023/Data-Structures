class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        q = deque()
        acc = [0] * len(nums)
        odd = 0

        for r, num in enumerate(nums):
            if num % 2:
                odd += 1
                q.append(r)
            
            if odd >= k:
                while l < len(nums) and odd > k:
                    if nums[l] % 2:
                        odd -= 1
                        q.popleft()
                    
                    l += 1
                
            
                acc[r] += (q[0] - l + 1)
            
            acc[r] += acc[r-1] if r - 1 >= 0 else 0
        
        return acc[-1]
