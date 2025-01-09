class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(map(int, str(num)))
        indices = {}

        for i, n in enumerate(digits):
            indices[n] = i
        
        for i, d in enumerate(digits):
            for n in range(9, d, -1):
                if i < indices.get(n, -1):
                    digits[i], digits[indices[n]] = digits[indices[n]], digits[i]
                    return int(''.join(map(str, digits)))
        
        return num
