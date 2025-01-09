
class Solution:
    def findMaxAverage(self, nums, k):
        curSum = sum(nums[:k])
        maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i - k]
            maxSum = max(curSum, maxSum)
        
        return maxSum / k

        

# my original solution
class Solution:
    def findMaxAverage(self, nums, k):
        maxAvg = float('-inf')

        for i in range(len(nums) - k + 1 ):
            curAvg = sum(nums[i:i+k]) / k #this method is not as efficient because you are recalculating the sum
            maxAvg = max(maxAvg, curAvg)
        
        return maxAvg

        