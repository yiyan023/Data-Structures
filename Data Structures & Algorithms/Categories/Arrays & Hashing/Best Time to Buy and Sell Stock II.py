class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        all_time_min = prices[0]
        cur_min = prices[0]
        cur_max = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if prices[i] < cur_max:
                res = max(res + cur_max - cur_min, res - all_time_min)
                cur_min = prices[i]
                cur_max = prices[i]
            
            else:
                all_time_min = min(all_time_min, prices[i])
                cur_min = min(cur_min, prices[i])
                cur_max = max(cur_max, prices[i])
        
        return max(res + cur_max - cur_min, res - all_time_min)
