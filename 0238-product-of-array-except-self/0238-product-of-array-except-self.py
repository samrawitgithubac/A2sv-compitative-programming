from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftproduct=1
        rightproduct=1
        ans=[1]*n
        for i in range(len(nums)):
            ans[i]=leftproduct
            leftproduct*=nums[i]
        for i in range(len(nums)-1,-1,-1):
           
            ans[i]*=rightproduct
            rightproduct*=nums[i]
        return ans

            