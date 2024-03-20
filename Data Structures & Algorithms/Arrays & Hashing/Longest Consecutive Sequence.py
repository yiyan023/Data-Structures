class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()

        if len(nums) == 0:
            return 0

        tally = 0
        curTally = 0
        prev = 0

        for i in range(len(nums)):
            if i == 0:
                prev = nums[i]
                curTally += 1
            
            elif nums[i] == prev + 1:
                curTally += 1
                prev = nums[i]
            
            elif nums[i] != prev:
                tally = max(curTally, tally)
                prev = nums[i]
                curTally = 1
        
        return max(tally, curTally)
        

#another solution using set
class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums) #to remove duplicates

        tally = 0
        
        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
            
                while (n + length) in numSet:
                    length += 1
                
                tally = max(tally, length)

        return tally