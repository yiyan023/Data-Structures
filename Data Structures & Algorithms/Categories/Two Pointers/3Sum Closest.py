class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestSum = float('inf')

        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if abs(target - threeSum) < abs(target - closestSum):
                    closestSum = threeSum
                
                if threeSum == target:
                    return target
                elif threeSum < target:
                    l += 1
                else:
                    r -= 1
        
        return closestSum