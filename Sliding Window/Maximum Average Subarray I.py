class Solution:
    def findMaxAverage(self, nums, k):
        maxAvg = float('-inf')

        for i in range(len(nums) - k + 1 ):
            curAvg = sum(nums[i:i+k]) / k #this method is not as efficient because you are recalculating the sum
            maxAvg = max(maxAvg, curAvg)
        
        return maxAvg

        