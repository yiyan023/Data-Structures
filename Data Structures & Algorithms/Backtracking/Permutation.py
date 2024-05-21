class Solution(object):
    def permute(self, nums):
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            cur = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(cur)
            result.extend(perms)
            nums.append(cur)
        
        return result
                
