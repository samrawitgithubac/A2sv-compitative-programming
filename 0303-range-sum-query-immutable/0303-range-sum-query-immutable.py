class NumArray:

    def __init__(self, nums: List[int]):
        cur=0
        self.prefix=[]
        for n in nums:
            cur+=n
            self.prefix.append(cur)

        
        

    def sumRange(self, left: int, right: int) -> int:
        right_sum=self.prefix[right]
        left_sum=self.prefix[left-1] if left>0 else 0
        return  right_sum - left_sum
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)