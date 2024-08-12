class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []

        def bs():
            l, r = 0, len(result) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if result[mid] == num:
                    result[mid] = num
                    return
                
                elif result[mid] > num:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            result[l] = num
            return

        for num in nums:
            if result and result[-1] >= num:
                bs()

            else:
                result.append(num)
        
        return len(result)
