class Solution:
    def minSubArrayLen(self, target: int, nums):
        l = 0
        minLength = float('inf')
        totalSum = 0

        for r in range(len(nums)):
            if nums[r] >= target: #base case
                return 1
            
            elif l == r:
                totalSum += nums[l]
            else:
                totalSum += nums[r]
                
                while totalSum >= target and l < r: #>= not ==
                    currentLength = r - l + 1
                    minLength = min(minLength, currentLength)
                    totalSum -= nums[l]
                    l += 1

        if minLength == float('inf'):
            return 0
            
        return minLength
                
            
            

        