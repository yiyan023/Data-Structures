class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        acc, res = 0, 0
        even, odd = 0, 0
        MOD = (10 ** 9 + 7)

        for i, num in enumerate(arr):
            acc += num

            if acc % 2:
                res = (res + even + 1) % MOD
                odd += 1
            
            else:
                res = (res + odd) % MOD
                even += 1

        return res

