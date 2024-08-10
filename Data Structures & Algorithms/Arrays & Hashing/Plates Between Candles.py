class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        nextCandle, prevCandle = [float('inf')] * (len(s) + 1), [0] * (len(s))
        candles = [0] * (len(s) + 1)
        result = []
        
        for i, c in enumerate(s):
            candles[i+1] = candles[i] + (c == "|")
            prevCandle[i] = i if c == "|" else prevCandle[i - 1] 
            # new candle location, otherwise, previous candle remains the same 
        
        for i in range(len(s)-1, -1, -1):
            nextCandle[i] = i if s[i] == "|" else nextCandle[i + 1]
        
        for start, end in queries:
            l, r = nextCandle[start], prevCandle[end]
            result.append(r - l - (candles[r] - candles[l]) if l < r else 0) 
    
        return result

