class Solution:
    def jump(self, nums):
        maxReach, maxPos, num = 0, 0, 0

        for s in range(len(nums) - 1):
            maxReach = max(maxReach, s + nums[s]) # farthest step we can go 

            if s == maxPos: # we are at the last possible position, have to make a jump
                maxPos = maxReach # we can reach the farthest possible step 
                num += 1 # number of stairs needed increases by one
            
        return num