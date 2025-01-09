class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def getSum(value, index, n):
            acc = 0

            if index < value:
                acc += (value + value - index) * (index + 1) // 2
            
            else:
                acc += (value) * (value + 1) // 2 + (index - value + 1) 
            
            if value > n - index:
                acc += (2 * value - n + 1 + index) * (n - index) // 2
            
            else: 
                acc += (value) * (value + 1) // 2 + n - value - index

            return acc - value
        
        start, finish = 1, maxSum 
        result = 0

        while start <= finish:
            mid = start + (finish - start) // 2

            if getSum(mid, index, n) > maxSum:
                finish = mid - 1
            
            else:
                result = max(result, mid)
                start = mid + 1
        
        return result

