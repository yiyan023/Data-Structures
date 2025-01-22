class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = [0] * (hi + 1)
        dp[1] = 0
        min_heap = []

        for i in range(2, len(dp)):
            if not i % 2:
                dp[i] = dp[i // 2] + 1
            
            else:
                count = 1
                next_num = i * 3 + 1

                while next_num > i or next_num % 2:
                    count += 1
                    if not next_num % 2:
                        next_num //= 2
                    
                    else:
                        next_num = next_num * 3 + 1

                dp[i] = count + dp[next_num]

        for num in range(lo, hi + 1):
            heapq.heappush(min_heap, (-dp[num], -num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return -min_heap[0][1]
