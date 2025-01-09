class NumArray:

    def __init__(self, nums: List[int]):
        self.acc = list(itertools.accumulate(nums))
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right] - self.acc[left] + self.nums[left]
