class NumArray:
    
    def __init__(self, nums: List[int]):
        self.nums=nums
        self.res=[0]*len(self.nums)
        prefix=0
        for i in range(len(self.nums)):
            prefix+=self.nums[i]
            self.res[i]=prefix

            
        
        
        
    def sumRange(self, left: int, right: int) -> int:
        for i in range(len(self.nums)):
            if left == 0:
                return self.res[right] 
             
            return self.res[right] - self.res[left - 1]

        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)