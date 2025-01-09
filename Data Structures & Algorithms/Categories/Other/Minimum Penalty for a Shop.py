class Solution:
    def bestClosingTime(self, customers: str) -> int:
        open_h, close_h = {"Y": 0, "N": 0}, {"Y": 0, "N": 0}
        minVal, minIndex = float('inf'), 0

        for c in customers:
            close_h[c] += 1
        
        for i in range(len(customers)+1):
            if minVal > open_h["N"] + close_h["Y"]:
                minVal = open_h["N"] + close_h["Y"]
                minIndex = i
            
            if i < len(customers):
                open_h[customers[i]] += 1
                close_h[customers[i]] -= 1
        
        return minIndex
