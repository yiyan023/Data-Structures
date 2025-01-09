class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
            minVal = len(nums) // 3
            freq = {}
            result = []
            dup = set()
            
            for num in nums:
                freq[num] = 1 + freq.get(num, 0)
                
                if freq[num] > minVal and num not in dup:
                    dup.add(num)
                    result.append(num)
            
            return result
