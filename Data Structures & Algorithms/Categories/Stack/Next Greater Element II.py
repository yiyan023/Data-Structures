class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)

        for i in range(2 * len(nums) - 1):
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                prev = stack.pop()
                res[prev] = nums[i % len(nums)]
            
            stack.append(i % len(nums))
        
        return res
