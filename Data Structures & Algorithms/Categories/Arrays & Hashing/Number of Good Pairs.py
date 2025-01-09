class Solution:
    def numIdenticalPairs(self, nums):
        array = [0] * 101

        for num in nums:
            array[num] += 1
        
        acc = 0

        for n in array:
            if n >= 2:
                acc += n * (n - 1) / 2
        
        return int(acc)


        