class Cashier:
    # only considering positive numbers? 
    # do I have to consider the case where n is 0?
    # do I have to consider the case where there are no products?
    # product Ids are unique

    # discount => 0 discount, normal discount 
    # n => any two values just to make sure that your logic works
    # calculating subtotal => testing multiple values to make sure that the logic is correct

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.acc = 0
        self.n = n
        self.discount = discount / 100 
        self.product_hash = {}

        for i, p_id in enumerate(products):
            self.product_hash[p_id] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.subtotal = 0
        self.acc += 1
        
        for i, p_id in enumerate(product):
            self.subtotal += self.product_hash[p_id] * amount[i]
        
        if not self.acc % self.n:
            return self.subtotal * (1 - self.discount)
        
        return self.subtotal


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
