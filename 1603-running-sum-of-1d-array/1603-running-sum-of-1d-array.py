class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            res[i]=prefix
        return res
        