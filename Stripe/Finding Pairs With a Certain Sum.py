class FindSumPairs:
    # are they necessarily the same length?
    # is it possible that the numbers are negative?
    # are duplicates possible 
    # what are the constraints of the problem? length of nums1, nums2?
    # are we assuming that all the inputs are valid => index will be in range
    # does add only add to the second array?

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n2_freq = {}
        self.n1, self.n2 = nums1, nums2
        
        for val in self.n2:
            self.n2_freq[val] = 1 + self.n2_freq.get(val, 0)

    def add(self, index: int, val: int) -> None:
        self.n2[index] += val 
        self.n2_freq[self.n2[index] - val] -= 1
        self.n2_freq[self.n2[index]] = 1 + self.n2_freq.get(self.n2[index], 0)

    def count(self, tot: int) -> int:
        pairs = 0

        for val in self.n1:
            complement = tot - val 

            if complement in self.n2_freq:
                pairs += self.n2_freq[complement]
        
        return pairs
