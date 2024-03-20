class Solution:
    def topKFrequent(self, nums):
        count = {}
        tally = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0) # set up count hash 

        for n, c in count.items():
            tally[c].append(n)
        
        print(tally)
        result = []

        for i in range(len(tally) - 1, 0, -1):
            for n in tally[i]:
                result.append(n)

                if len(result) == k:
                    return result 
        
        