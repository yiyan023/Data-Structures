class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            
            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        res = [next_greater[num] for num in nums1]
        return res