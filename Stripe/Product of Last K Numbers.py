class ProductOfNumbers:
    # of having a zero =>"resets" the whole product because every leading product will just be equal to zero [3, 0, 0, 0, 0]
    # being able to test the algorithm or getting the prodcut itself => multiple k values 
    # we are returning the product of length n numbers
    # returning the products of length greater than current array

    def __init__(self):
        self.products = []

    def add(self, num: int) -> None:
        self.products.append(num if not self.products else num * self.products[-1])

        if self.products and not self.products[-1]:
            self.products = []
        
    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return 0 if k > len(self.products) else self.products[-1]
        
        r = len(self.products) - 1
        return self.products[r] // self.products[r-k]
