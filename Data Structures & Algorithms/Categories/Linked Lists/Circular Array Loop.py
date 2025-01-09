class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visit = set()

        def next(i):
            return (i + nums[i]) % len(nums)
        
        for i in range(len(nums)):
            if i in visit: 
                continue 
            
            slow, fast = i, next(i)
            visit.update([slow, fast])

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow != next(slow):
                        return True 
                    
                    break 
                
                slow = next(slow)
                fast = next(next(fast))
                visit.update([slow, fast])
            
        return False
