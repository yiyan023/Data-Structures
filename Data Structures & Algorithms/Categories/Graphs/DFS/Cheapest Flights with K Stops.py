class Solution:
    def findCheapestPrice(self, n: int, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices[:]

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue 
                
                elif  p + prices[s] < temp[d]:
                    temp[d] = p + prices[s]
                
            prices = temp 
        
        return prices[dst] if prices[dst] != float('inf') else -1