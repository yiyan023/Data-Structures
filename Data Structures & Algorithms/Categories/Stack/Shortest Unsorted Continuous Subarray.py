class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # cases where we need to swap -> left + 1 < left, right - 1 > right, min or max is not in place
        l, r = len(nums) - 1, 0
        forward, backward = [], []

        for i in range(len(nums)):
            while forward and nums[forward[-1]] > nums[i]:
                l = min(l, forward.pop())
            forward.append(i)
        
        for i in range(len(nums) - 1, -1, -1):
            while backward and nums[backward[-1]] < nums[i]:
                r = max(r, backward.pop())
            backward.append(i)
        
        return 0 if r <= l else r - l + 1
