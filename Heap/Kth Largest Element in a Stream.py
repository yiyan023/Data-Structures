import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.nums, self.k = nums, k
        heapq.heapify(self.nums) # initialize minHeap

        while len(self.nums) > self.k:
            heapq.heappop(self.nums) # remove elements until length is max k

    def add(self, val):
        heapq.heappush(self.nums, val) #adds val to heap while maintaining heap structure 

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0] # return kth largest