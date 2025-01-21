class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                upper, lower = mid, mid

                while lower -1 >= 0 and nums[lower - 1] == target:
                    lower -= 1
                
                while upper + 1 < len(nums) and nums[upper + 1] == target:
                    upper += 1
                
                return [lower, upper]
        
        return [-1, -1]
        
