class StockSpanner:
    # is it possible that the numbers or stock prices are negative?
    # based on the example, that means that there can be duplicates, the stocks are not in chroonological order 
    # it is <= to the current value, so inclusive
    # do we need to account for any invalid inputs 
    # it is also inclusive of the current day?

    # test cases:
    # two equal stocks in a row (test inclusivity) => [100, 100] should return 1, 2
    # previous stock is less than today's stock => [90, 100] should return 1, 2
    # previous stock is MORE than today's stock => [100, 90], should return 1, 2

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        counter = 1
        while self.stack and self.stack[-1][0] <= price:
            counter += self.stack.pop()[1]
        self.stack.append((price,counter))
        return counter
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
