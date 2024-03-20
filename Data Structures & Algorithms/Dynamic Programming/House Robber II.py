class Solution(object):
    def rob(self, nums):
        # need to consider the case where we remove the edges since they are connected
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2 
            rob2 = temp
        
        return rob2
        