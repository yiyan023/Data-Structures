class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(int)
        res = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                products[(nums[i] * nums[j])] += 1
        
        for key in products:
            if products[key] > 1:
                res += math.comb(products[key], 2) * 8
        
        return res
