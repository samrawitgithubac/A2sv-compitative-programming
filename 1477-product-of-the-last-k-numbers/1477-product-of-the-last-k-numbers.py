class ProductOfNumbers:

    def __init__(self):
        # self.stream = [1]
        self.prefix = [1]
        self.length = 0
        self.zero_index = None

    def add(self, num: int) -> None:
        # self.stream.append(num)
        self.length += 1

        if num == 0:
            self.zero_index = self.length
            self.prefix.append(1)
        else:
            self.prefix.append(self.prefix[-1]*num)
            
    def getProduct(self, k: int) -> int:
        left = self.length - k + 1

        if self.zero_index and left <= self.zero_index:
            return 0
        else:
           return self.prefix[-1] // self.prefix[left-1]
            
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
