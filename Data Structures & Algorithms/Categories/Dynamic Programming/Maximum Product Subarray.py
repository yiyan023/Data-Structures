class Solution:
    def maxProduct(self, nums):
        result = nums[0]
        maxVal, minVal = 1, 1 # initialize this

        for num in nums:
            values = [num, maxVal * num, minVal * num]
            maxVal, minVal = max(values), min(values)
            result = max(result, maxVal)

        return result
