class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum=abs(nums[0])
        currsum=0
        j=0
       
        res=[0]
        for i in  nums:
            currsum+=i
            res.append(currsum)
        a=min(res)
        b=max(res)
        return b-a
        

           