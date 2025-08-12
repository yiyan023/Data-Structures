class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = Counter(nums1)
        self.nums2 = Counter(nums2)

        self.nums2_arr = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[self.nums2_arr[index]] -= 1
        self.nums2_arr[index] += val 
        self.nums2[self.nums2_arr[index]] += 1

    def count(self, tot: int) -> int:
        res = 0

        for num in self.nums1.keys():
            if tot - num in self.nums2:
                res += (self.nums1[num] * self.nums2[tot - num])
        
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
