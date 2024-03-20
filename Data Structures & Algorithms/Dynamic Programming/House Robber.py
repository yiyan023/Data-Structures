class Solution:
    def rob(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(rob1 + num, rob2) #not (rob1 + n) bc it does not necessarily need to be alternating
            rob1 = rob2 
            rob2 = temp
        
        return rob2 #this will automatically return the max
        
        