class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        prefixsum=0
        for i in range(len(nums)):
            prefixsum+=nums[i]
            res.append(prefixsum)
        return res
      
    

