class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.products = []
        self.acc = 1

    def add(self, num: int) -> None:
        self.stream.append(num)

        if not num: #reset cuz of 0
            self.acc = 1
            self.products = []

        else:
            self.acc *= num
            self.products.append(self.acc)

    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return self.products[-1] if k == len(self.products) else 0
        
        return self.products[len(self.products) - 1] // self.products[len(self.products) - k - 1]
