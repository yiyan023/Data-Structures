class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def binary_search(total):
            groups = 0
            acc = 0

            for num in nums:
                if num > total:
                    return float('inf')
                
                if acc + num > total:
                    acc = num 
                    groups += 1
                
                else:
                    acc += num
            
            return groups + 1
        
        l, r = 0, sum(nums)
        res = float('inf')

        while l <= r:
            mid = (l + r) // 2

            groups = binary_search(mid)

            if groups > k:
                l = mid + 1
            
            else:
                r = mid - 1
                res = min(res, mid)
        
        return res
